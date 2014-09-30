<%inherit file="/base.mako" />

<%def name="head_tags()">
   <head>
      <title>LAGER - Array Group Report</title>
   </head>
</%def>

This is an Array Group report, from Tuning Manager.  For this type of report we generate four plots, as follows:

<ul>
<li> Top X parity groups by Maximum IOPS</li>
<li> Top X parity groups by Average IOPS</li>
<li> Top X parity groups by Maximum MB/s</li>
<li> Top X parity groups by Average MB/s</li>
</ul>

<bold>NOTE:</bold>  There is a maximum of 30 parity groups for these plots<br />

You may choose the number of parity groups to report on below:

<form name="array_group_plot" method="POST" action="/graphme/plot_array_group" enctype="multipart/form-data">
<table>
<tr><td>Number of parity groups to plot</td><td><select NAME="num_of_parity_groups">
% for i in range(30,0,-1):
   <option>${i}
%endfor
</td></tr>
<tr><td></td><td><input type="submit" name="submit" value="Submit" /></td></tr>
</table>
<input type="hidden" style="display:none" name="filename" value="${c.filename}" />
<input type="hidden" style="display:none" name="case" value="${c.case}" />
<input type="hidden" style="display:none" name="customer" value="${c.customer}" />
<input type="hidden" style="display:none" name="email" value="${c.email}" />
</form>


<table>
<tr><td>File:</td><td>${c.filename}</td></tr>
<tr><td>Engineer:</td><td>${c.email}</td></tr>
<tr><td>customer:</td><td>${c.customer}</td></tr>
<tr><td>Case number:</td><td>${c.case}</td></tr>
</table>
