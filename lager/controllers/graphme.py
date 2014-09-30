import logging
import os
import sys
import numpy
import matplotlib
matplotlib.use('Agg')
import pylab
import threading
import PIL, PIL.Image
from heapq import nlargest
from operator import itemgetter
import datetime
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from matplotlib.font_manager import fontManager, FontProperties
import uuid

import shutil
import re
from matplotlib import rcParams
rcParams.update( {
    'font.family' : 'century gothic',
    'font.style' : 'normal',
    'font.variant' : 'normal',
    'font.size' : 6,
    })


from pylons import request, response, session, tmpl_context as c
# Commented out 20140929 - blogging about the past
#from pylons.controllers.util import abort, redirect_to
from pylons.controllers.util import abort, redirect

from lager.lib.base import BaseController, render

log = logging.getLogger(__name__)
imageThreadLock = threading.Lock()
timesRequested = 0

permanent_store='/home/chodges/lager-pylons/lager/lager/lager/public'

class GraphmeController(BaseController):

    def lager(self):
        return render('upload.mako')

    def upload(self):
        c.case=str(uuid.uuid4())
        print c.case
        filetype=0
        myfile = request.POST['myfile']
        customer_directory=os.path.join(permanent_store, request.POST['customer'])
        if not os.path.isdir(customer_directory):
            os.mkdir(customer_directory)
        case_directory=os.path.join(customer_directory ,c.case)
        if not os.path.isdir(case_directory):
            os.mkdir(case_directory)
        filename = os.path.join(case_directory, myfile.filename.lstrip(os.sep))
        c.filename=filename
        c.customer=request.POST['customer']
        c.email=request.POST['email']
        permanent_file = open(filename, 'w')
        shutil.copyfileobj(myfile.file, permanent_file)
        myfile.file.close()
        permanent_file.close()
        outputfile=open(filename,'r')
        firstline=outputfile.readline()
        while (not(re.search("[a-zA-Z]", firstline))):
            firstline=outputfile.readline()
        firstline=firstline.replace("\n","")
        firstline=firstline.replace("\r","")
        if (re.search("Array Group Performance Details", firstline)):
            filetype="array_group.mako"
        if (re.search("Subsystem Cache Memory Usage Details", firstline)):
            filetype="cache_usage.mako"
        if (re.search("CHP Busy Rate Details", firstline)):
            filetype="ctrl_report.mako"
        if (re.search("DKP Busy Rate Details", firstline)):
            filetype="ctrl_report.mako"
        if (re.search("Logical Device Performance Details", firstline)):
            filetype="ldev_report.mako"
        if (re.search("SATA Logical Device Performance Details", firstline)):
            filetype="ldev_report.mako"
        if (not(filetype)):
            filetype="unknown.mako"
        return render(filetype)

    def plot_ldev(self):
        timesRequested=0
        global timesRequestd
        global imageThreadLock
        largest=int(request.POST['num_of_ldevs'])
        case=str(request.POST['case'])
        customer=str(request.POST['customer'])
        email=str(request.POST['email'])
        case_directory=os.path.join(permanent_store, customer, case)
        inputfile = request.POST['filename']
        c.customer=customer
        c.case=case
        c.email=email
        if not os.path.isdir(case_directory):
            os.mkdir(case_directory)
        status_file=os.path.join(case_directory, "status")
        status=open(status_file, 'w')
        status.write(customer+"\n")
        status.write(email+"\n")
        status.write(inputfile+"\n")
        status.close()

        dates=set()
        percent_busy = dict()
        read_iops = dict()
        write_iops = dict()
        total_random_iops=dict()
        total_sequential_iops=dict()
        read_xfer=dict()
        write_xfer=dict()
        total_random_xfer=dict()
        total_sequential_xfer=dict()
        read_hit_percent=dict()
        write_hit_percent=dict()
        read_response=dict()
        write_response=dict()
        total_response=dict()

        total_iops = []
        total_xfer = []
        max_percent_busy = dict()
        avg_percent_busy = dict()
        max_iops = dict()
        avg_iops = dict()
        max_xfer = dict()
        avg_xfer = dict()
        ldev_iops = dict()
        ldev_xfer = dict()
        #
        print "Processing file", inputfile
        f = open(inputfile,'r')
        linecount=int(0)
        datecount=int(-1)
        datecount=int(datecount)
        tempdate=0
        for line in f:
            line=line.rstrip("\n")
            #print "line:  ",linecount
            if (linecount < 5):
                linecount+=1
            elif (linecount == 5):
               series = line.split(",")
               print series
               linecount+=1
            else:
               data = line.split(",")
               date=data[0]
               if (tempdate != date):
                   datecount=int(datecount + 1)
                   #print "Tempdate: ", tempdate, "Date: ", date, "Datecount: ", datecount
               (month, day, year, time) = date.split()
               (hour, minute, second) = time.split(":")
               month=int(month)
               day=int(day)
               year=int(year)
               hour=int(hour)
               minute=int(minute)
               second=int(second)
               #print year, month, day, hour, minute, second
               #print data
               dates.add(matplotlib.dates.date2num(datetime.datetime(year, month, day, hour, minute, second)))
               ldev_number=data[1]
               read_iops[ldev_number]=read_iops.get(ldev_number, [])+[float(data[2])]
               write_iops[ldev_number]=write_iops.get(ldev_number, [])+[float(data[3])]
               total_random_iops[ldev_number]=total_random_iops.get(ldev_number, [])+[float(data[4])]
               total_sequential_iops[ldev_number]=total_sequential_iops.get(ldev_number, [])+[float(data[5])]
               read_xfer[ldev_number]=read_xfer.get(ldev_number, [])+[float(data[6])]
               write_xfer[ldev_number]=write_xfer.get(ldev_number, [])+[float(data[7])]
               total_random_xfer[ldev_number]=total_random_xfer.get(ldev_number, [])+[float(data[8])]
               total_sequential_xfer[ldev_number]=total_sequential_xfer.get(ldev_number, [])+[float(data[9])]
               read_hit_percent[ldev_number]=read_hit_percent.get(ldev_number, [])+[float(data[10])]
               write_hit_percent[ldev_number]=write_hit_percent.get(ldev_number, [])+[float(data[11])]
               read_response[ldev_number]=read_response.get(ldev_number, [])+[float(data[12])]
               write_response[ldev_number]=write_response.get(ldev_number, [])+[float(data[13])]
               total_response[ldev_number]=total_response.get(ldev_number, [])+[float(data[14])]
               ldev_iops[ldev_number]=ldev_iops.get(ldev_number, [])+[float(data[2])+float(data[3])]
               ldev_xfer[ldev_number]=ldev_xfer.get(ldev_number, [])+[float(data[6])+float(data[7])]
               try:
                   total_iops[datecount]+=(float(data[2])+float(data[3]))
               except IndexError:
                   total_iops.append(float(data[2])+float(data[3]))
               try:
                   total_xfer[datecount]+=(float(data[6])+float(data[7]))
               except IndexError:
                   total_xfer.append(float(data[6])+float(data[7]))
               #print "Date: ", date, "Total Iops: ", total_iops[datecount], "Total Xfer: ", total_xfer[datecount]
               linecount+=1
               tempdate=date
        #
        #print ldev_number, percent_busy[ldev_number], write_hit_percent[ldev_number]
        dates=list(dates)
        dates.sort()
        for key in read_iops.keys():
            #print "Key:", key
            #print "ldev_iops:", max(ldev_iops[key])
            max_iops[key] = max(ldev_iops[key])
            avg_iops[key] = float(sum(ldev_iops[key])/len(ldev_iops[key]))
            max_xfer[key] = max(ldev_xfer[key])
            avg_xfer[key] = float(sum(ldev_xfer[key])/len(ldev_xfer[key]))
            print "LDEV: ", key, "Max IOPS: ", max_iops[key], "Average IOPS: ", avg_iops[key], "Max Xfer: ", max_xfer[key], "Average Xfer: ", avg_xfer[key]
        largest_iops = nlargest(largest, max_iops, max_iops.__getitem__)
        largest_average_iops = nlargest(largest, avg_iops, avg_iops.__getitem__)
        largest_xfer = nlargest(largest, max_xfer, max_xfer.__getitem__)
        largest_average_xfer = nlargest(largest, avg_xfer, avg_xfer.__getitem__)

        print "Getting lock"
        imageThreadLock.acquire()
        print "Got Lock"

        c.filenames=[]
        
        pylab.figure (1)
        pylab.suptitle("Top "+str(largest)+" LDEVs by Maximum IOPS",fontsize=16)
        count=int(1)
        for ldev_number in largest_iops:
            pylab.subplot(largest,1,count)
            pylab.plot_date(dates, ldev_iops[ldev_number], fmt='b-',label=str(ldev_number))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_iops[largest_iops[0]]])
            count+=1
        filename = os.path.join(case_directory,"ldevs_max_iops.png")
        c.filenames = c.filenames+[os.path.join(customer,case,"ldevs_max_iops.png")]
        pylab.savefig(filename)
        pylab.clf()
        
        pylab.figure (2)
        pylab.suptitle("Top "+str(largest)+" LDEVs by Average IOPS",fontsize=16)
        count=int(1)
        for ldev_number in largest_average_iops:
            pylab.subplot(largest,1,count)
            pylab.plot_date(dates, ldev_iops[ldev_number], fmt='b-',label=str(ldev_number))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_iops[largest_iops[0]]])
            count+=1
        filename = os.path.join(case_directory,"ldevs_avg_iops.png")
        c.filenames = c.filenames+[os.path.join(customer,case,"ldevs_avg_iops.png")]
        pylab.savefig(filename)
        pylab.clf()
    
    
        pylab.figure (3)
        pylab.suptitle("Top "+str(largest)+" LDEVs by Maximum Transfer (MB/s)",fontsize=16)
        count=int(1)
        for ldev_number in largest_xfer:
            pylab.subplot(largest,1,count)
            #if (len(dates) != len(ldev_xfer[ldev_number])):
                #print "LDEV: ",ldev_number
                #print "Date count: ",len(dates)
                #print "LDEV count: ",len(ldev_xfer[ldev_number])
                #print dates
                #print ldev_xfer[ldev_number]
            pylab.plot_date(dates, ldev_xfer[ldev_number], fmt='b-',label=str(ldev_number))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_xfer[largest_xfer[0]]])
            count+=1
        filename = os.path.join(case_directory,"ldevs_max_transfer.png")
        c.filenames = c.filenames+[os.path.join(customer,case,"ldevs_max_transfer.png")]
        pylab.savefig(filename)
        pylab.clf()
    
        
        pylab.figure (4)
        pylab.suptitle("Top "+str(largest)+" LDEVs by Average Transfer (MB/s)",fontsize=16)
        count=int(1)
        for ldev_number in largest_average_xfer:
            pylab.subplot(largest,1,count)
            pylab.plot_date(dates, ldev_xfer[ldev_number], fmt='b-',label=str(ldev_number))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_xfer[largest_xfer[0]]])
            count+=1
        filename = os.path.join(case_directory,"ldevs_avg_transfer.png")
        c.filenames = c.filenames+[os.path.join(customer,case,"ldevs_avg_transfer.png")]
        pylab.savefig(filename)
        pylab.clf()
    
        print "Releasing Lock"
        imageThreadLock.release()
        print "Released Lock"
        return render('display.mako')


        
    def plot_array_group(self):
        timesRequested=0
        global timesRequestd
        global imageThreadLock
        largest=int(request.POST['num_of_parity_groups'])
        case=str(request.POST['case'])
        customer=str(request.POST['customer'])
        email=str(request.POST['email'])
        case_directory=os.path.join(permanent_store, customer, case)
        inputfile = request.POST['filename']
        c.customer=customer
        c.case=case
        c.email=email
        if not os.path.isdir(case_directory):
            os.mkdir(case_directory)
        status_file=os.path.join(case_directory, "status")
        status=open(status_file, 'w')
        status.write(customer+"\n")
        status.write(email+"\n")
        status.write(inputfile+"\n")
        status.close()
        
        dates=set()
        percent_busy = dict()
        read_iops = dict()
        write_iops = dict()
        random_read_iops = dict()
        random_write_iops = dict()
        total_random_iops=dict()
        sequential_read_iops=dict()
        sequential_write_iops=dict()
        total_sequential_iops=dict()
        read_xfer=dict()
        write_xfer=dict()
        random_read_xfer=dict()
        random_write_xfer=dict()
        total_random_xfer=dict()
        sequential_read_xfer=dict()
        sequential_write_xfer=dict()
        total_sequential_xfer=dict()
        read_hit_percent=dict()
        write_hit_percent=dict()
        total_iops = []
        total_xfer = []
        max_percent_busy = dict()
        avg_percent_busy = dict()
        max_iops = dict()
        avg_iops = dict()
        max_xfer = dict()
        avg_xfer = dict()
        rg_iops = dict()
        rg_xfer = dict()
        #
        
        #print "Processing file", inputfile
        f = open(inputfile)
        linecount=int(0)
        datecount=int(-1)
        datecount=int(datecount)
        tempdate=0
        for line in f:
            line=line.rstrip("\n")
            #print "line:  ",linecount
            if (linecount < 5):
                linecount+=1
            elif (linecount == 5):
               series = line.split(",")
               print series
               linecount+=1
            else:
               data = line.split(",")
               date=data[0]
               if (tempdate != date):
                   datecount=int(datecount + 1)
               #print "Tempdate: ", tempdate, "Date: ", date, "Datecount: ", datecount
               (month, day, year, time) = date.split()
               (hour, minute, second) = time.split(":")
               month=int(month)
               day=int(day)
               year=int(year)
               hour=int(hour)
               minute=int(minute)
               second=int(second)
               #print year, month, day, hour, minute, second
               #print data
               dates.add(matplotlib.dates.date2num(datetime.datetime(year, month, day, hour, minute, second)))
               raid_group=data[1]
               percent_busy[raid_group]=percent_busy.get(raid_group, [])+[float(data[2])]
               read_iops[raid_group]=read_iops.get(raid_group, [])+[float(data[3])]
               write_iops[raid_group]=write_iops.get(raid_group, [])+[float(data[4])]
               random_read_iops[raid_group] = random_read_iops.get(raid_group, [])+[float(data[5])]
               random_write_iops[raid_group] = random_write_iops.get(raid_group, [])+[float(data[6])]
               total_random_iops[raid_group]=total_random_iops.get(raid_group, [])+[float(data[7])]
               sequential_read_iops[raid_group]=sequential_read_iops.get(raid_group, [])+[float(data[8])]
               sequential_write_iops[raid_group]=sequential_write_iops.get(raid_group, [])+[float(data[9])]
               total_sequential_iops[raid_group]=total_sequential_iops.get(raid_group, [])+[float(data[10])]
               read_xfer[raid_group]=read_xfer.get(raid_group, [])+[float(data[11])]
               write_xfer[raid_group]=write_xfer.get(raid_group, [])+[float(data[12])]
               random_read_xfer[raid_group]=random_read_xfer.get(raid_group, [])+[float(data[13])]
               random_write_xfer[raid_group]=random_write_xfer.get(raid_group, [])+[float(data[14])]
               total_random_xfer[raid_group]=total_random_xfer.get(raid_group, [])+[float(data[15])]
               sequential_read_xfer[raid_group]=sequential_read_xfer.get(raid_group, [])+[float(data[16])]
               sequential_write_xfer[raid_group]=sequential_write_xfer.get(raid_group, [])+[float(data[17])]
               total_sequential_xfer[raid_group]=total_sequential_xfer.get(raid_group, [])+[float(data[18])]
               read_hit_percent[raid_group]=read_hit_percent.get(raid_group, [])+[float(data[19])]
               write_hit_percent[raid_group]=write_hit_percent.get(raid_group, [])+[float(data[20])]
               rg_iops[raid_group]=rg_iops.get(raid_group, [])+[float(data[3])+float(data[4])]
               rg_xfer[raid_group]=rg_xfer.get(raid_group, [])+[float(data[11])+float(data[12])]
               try:
                   total_iops[datecount]+=(float(data[3])+float(data[4]))
               except IndexError:
                   total_iops.append(float(data[3])+float(data[4]))
               try:
                   total_xfer[datecount]+=(float(data[11])+float(data[12]))
               except IndexError:
                   total_xfer.append(float(data[11])+float(data[12]))
               #print "Date: ", date, "Total Iops: ", total_iops[datecount], "Total Xfer: ", total_xfer[datecount]
               linecount+=1
               tempdate=date
        #
        #print raid_group, percent_busy[raid_group], write_hit_percent[raid_group]
        f.close()
        dates=list(dates)
        dates.sort()
        for key in read_iops.keys():
            #print "Key:", key
            #print "RG_IOPS:", max(rg_iops[key])
            max_iops[key] = max(rg_iops[key])
            avg_iops[key] = float(sum(rg_iops[key])/len(rg_iops[key]))
            max_xfer[key] = max(rg_xfer[key])
            avg_xfer[key] = float(sum(rg_xfer[key])/len(rg_xfer[key]))
            #print "Raid Group: ", key, "Max IOPS: ", max_iops[key], "Average IOPS: ", avg_iops[key], "Max Xfer: ", max_xfer[key], "Average Xfer: ", avg_xfer[key]
            print "Raid Group: ", key
        largest_iops = nlargest(largest, max_iops, max_iops.__getitem__)
        largest_average_iops = nlargest(largest, avg_iops, avg_iops.__getitem__)
        largest_xfer = nlargest(largest, max_xfer, max_xfer.__getitem__)
        largest_average_xfer = nlargest(largest, avg_xfer, avg_xfer.__getitem__)
     
        print "Getting lock"
        imageThreadLock.acquire()
        print "Got Lock"

        c.filenames=[]
        pylab.figure (1)
        print "Figure 1"
        pylab.suptitle("Top "+str(largest)+" Parity Groups by Maximum IOPS",fontsize=16)
        count=int(1)
        for raid_group in largest_iops:
            pylab.subplot(largest,1,count)
            pylab.plot_date(dates, rg_iops[raid_group], fmt='b-',label=str(raid_group))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_iops[largest_iops[0]]])                              
            count+=1
        filename = os.path.join(case_directory, "parity_groups_max_iops.png")
        c.filenames=c.filenames+[os.path.join(customer, case, "parity_groups_max_iops.png")]
        pylab.savefig(filename)
        pylab.clf()
               
        pylab.figure (2)
        pylab.suptitle("Top "+str(largest)+" Parity Groups by Average IOPS",fontsize=16)
        count=int(1)
        for raid_group in largest_average_iops:
            pylab.subplot(largest,1,count)
            pylab.plot_date(dates, rg_iops[raid_group], fmt='b-',label=str(raid_group))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_iops[largest_iops[0]]])
            count+=1
        filename = os.path.join(case_directory, "parity_groups_ave_iops.png")
        c.filenames=c.filenames+[os.path.join(customer, case, "parity_groups_ave_iops.png")]
        pylab.savefig(filename)
        pylab.clf()
        
        pylab.figure (3)
        pylab.suptitle("Top "+str(largest)+" Parity Groups by Maximum Transfer (MB/s)",fontsize=16)
        count=int(1)
        for raid_group in largest_xfer:
            pylab.subplot(largest,1,count)
            pylab.plot_date(dates, rg_xfer[raid_group], fmt='b-',label=str(raid_group))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_xfer[largest_xfer[0]]])
            count+=1
        filename = os.path.join(case_directory, "parity_groups_max_transfer.png")
        c.filenames=c.filenames+[os.path.join(customer, case, "parity_groups_max_transfer.png")]
        pylab.savefig(filename)
        pylab.clf()
    
        pylab.figure (4)
        pylab.suptitle("Top "+str(largest)+" Parity Groups by Average Transfer (MB/s)",fontsize=16)
        count=int(1)
        for raid_group in largest_average_xfer:
            pylab.subplot(largest,1,count)
            pylab.plot_date(dates, rg_xfer[raid_group], fmt='b-',label=str(raid_group))
            pylab.legend(loc=0,prop=FontProperties(size=10))
            pylab.axis([min(dates),max(dates),0,max_xfer[largest_xfer[0]]])
            count+=1
        filename = os.path.join(case_directory, "parity_groups_ave_transfer.png")
        c.filenames=c.filenames+[os.path.join(customer, case, "parity_groups_ave_transfer.png")]
        pylab.savefig(filename)
        pylab.clf()
        
        print "Releasing Lock"
        imageThreadLock.release()
        print "Released Lock"
        return render('display.mako')

    def plot_cache_usage(self):
        c.filenames=[]
        timesRequested=0
        global timesRequestd
        global imageThreadLock
        case=str(request.POST['case'])
        customer=str(request.POST['customer'])
        email=str(request.POST['email'])
        case_directory=os.path.join(permanent_store, customer, case)
        inputfile = request.POST['filename']
        c.customer=customer
        c.case=case
        c.email=email
        if not os.path.isdir(case_directory):
            os.mkdir(case_directory)
        status_file=os.path.join(case_directory, "status")
        status=open(status_file, 'w')
        status.write(customer+"\n")
        status.write(email+"\n")
        status.write(inputfile+"\n")
        status.close()
        dates=set()
        cache_usage_percent = dict()
        cache_sidefile_percent = dict()
        cache_write_pending_percent = dict()
        print "Processing file", inputfile
        f = open(inputfile,'r')
        linecount=0
        for line in f:
            line=line.rstrip("\n")
            if (linecount < 5):
                linecount+=1
            elif (linecount == 5):
               series = line.split(",")
               print series
               linecount+=1
            else:
               data = line.split(",")
               (month, day, year, time) = data[2].split()
               (hour, minute, second) = time.split(":")
               month=int(month)
               day=int(day)
               year=int(year)
               hour=int(hour)
               minute=int(minute)
               second=int(second)
               #print year, month, day, hour, minute, second
               #print data
               dates.add(matplotlib.dates.date2num(datetime.datetime(year, month, day, hour, minute, second)))
               serial=data[0]
               cache_usage_percent[serial]=cache_usage_percent.get(serial, [])+[float(data[5])]
               cache_sidefile_percent[serial]=cache_sidefile_percent.get(serial, [])+[float(data[7])]
               cache_write_pending_percent[serial]=cache_write_pending_percent.get(serial, [])+[float(data[9])]
               linecount+=1
        #
        dates=list(dates)
        dates.sort()
        #print dates
        
        print "Getting lock"
        imageThreadLock.acquire()
        print "Got Lock"

        pylab.figure(1)
        pylab.subplot(311)
        pylab.title("Cache Usage %")
        pylab.plot_date(dates, cache_usage_percent[serial], fmt='b-', label="Cache Usage %")
        pylab.axis([min(dates),max(dates),-10,110])
        pylab.subplot(312)
        pylab.title("Cache Sidefile %")
        pylab.plot_date(dates, cache_sidefile_percent[serial], fmt='r-', label="Cache Sidefile %")
        pylab.axis([min(dates),max(dates),-10,100])
        pylab.subplot(313)
        pylab.title("Cache Write Pending %")
        pylab.plot_date(dates, cache_write_pending_percent[serial], fmt='g-', label="Cache Write Pending %")
        pylab.axis([min(dates),max(dates),-10,110])
        filename = os.path.join(case_directory, "cache_usage.png")
        c.filenames=c.filenames+[os.path.join(customer, case, "cache_usage.png")]     
        pylab.savefig(filename)
        pylab.subplot(311)
        pylab.cla()
        pylab.subplot(312)
        pylab.cla()
        pylab.subplot(313)
        pylab.cla()
        pylab.clf()

        print "Releasing Lock"
        imageThreadLock.release()
        print "Released Lock"
        return render('display.mako')

    def plot_ctrl_report(self):
        c.filenames=[]
        timesRequested=0
        global timesRequestd
        global imageThreadLock
        case=str(request.POST['case'])
        customer=str(request.POST['customer'])
        email=str(request.POST['email'])
        case_directory=os.path.join(permanent_store, customer, case)
        inputfile = request.POST['filename']
        c.customer=customer
        c.case=case
        c.email=email
        if not os.path.isdir(case_directory):
            os.mkdir(case_directory)
        status_file=os.path.join(case_directory, "status")
        status=open(status_file, 'w')
        status.write(customer+"\n")
        status.write(email+"\n")
        status.write(inputfile+"\n")
        status.close()

        dates=set()
        percent_busy = dict()
        print "Processing file", inputfile
        f = open(inputfile,'r')
        linecount=0
        for line in f:
            line=line.rstrip("\n")
            #print "line:  ",linecount
            if (linecount < 5):
                linecount+=1
            elif (linecount == 5):
               series = line.split(",")
               print series
               linecount+=1
            else:
               data = line.split(",")
               (month, day, year, time) = data[0].split()
               (hour, minute, second) = time.split(":")
               month=int(month)
               day=int(day)
               year=int(year)
               hour=int(hour)
               minute=int(minute)
               second=int(second)
               #print year, month, day, hour, minute, second
               #print data
               dates.add(matplotlib.dates.date2num(datetime.datetime(year, month, day, hour, minute, second)))
               controller=data[1]+"-"+data[2]
               percent_busy[controller]=percent_busy.get(controller, [])+[float(data[4])]
               linecount+=1
        #
        dates=list(dates)
        dates.sort()
        #print dates

        print "Getting lock"
        imageThreadLock.acquire()
        print "Got Lock"

        for key in percent_busy.keys():
            pylab.figure(1)
            pylab.title("Controller "+key+" Processor Utilization")
            pylab.plot_date(dates, percent_busy[key],fmt='b-', label=key)
            pylab.axis([min(dates),max(dates),0,100])
            filename = os.path.join(case_directory, "ctrl_report"+key+".png")
            c.filenames=c.filenames+[os.path.join(customer, case, "ctrl_report"+key+".png")]
            pylab.savefig(filename)
            pylab.clf()

        print "Releasing Lock"
        imageThreadLock.release()
        print "Released Lock"
        return render('display.mako')

                    
    def form(self):
        return render('form.mako')

    def email(self):
        return 'Your email is: %s' % request.params['email']

    def index(self):
        # Return a rendered template
        #return render('/hello.mako')
        # or, return a response
        return render('hello.mako')

