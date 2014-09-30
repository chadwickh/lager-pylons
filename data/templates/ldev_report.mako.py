# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412041739.486044
_enable_loop = True
_template_filename = '/home/chodges/lager-pylons/lager/lager/lager/templates/ldev_report.mako'
_template_uri = 'ldev_report.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        range = context.get('range', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        __M_writer(u'\r\n\r\nThis is an LDEV report, from Tuning Manager.  For this type of report we generate four plots, as follows:\r\n\r\n<ul>\r\n<li> Top X LDEVs by Maximum IOPS</li>\r\n<li> Top X LDEVs by Average IOPS</li>\r\n<li> Top X LDEVs by Maximum MB/s</li>\r\n<li> Top X LDEVs by Average MB/s</li>\r\n</ul>\r\n\r\n<bold>NOTE:</bold>  There is a maximum of 30 LDEVs for these plots<br />\r\n\r\nYou may choose the number of LDEVs to report on below:\r\n\r\n<form name="ldev_plot" method="POST" action="/graphme/plot_ldev" enctype="multipart/form-data">\r\n<table>\r\n<tr><td>Number of LDEVs to plot</td><td><select NAME="num_of_ldevs">\r\n')
        for i in range(30,0,-1):
            __M_writer(u'   <option>')
            __M_writer(escape(i))
            __M_writer(u'\r\n')
        __M_writer(u'</td></tr>\r\n<tr><td></td><td><input type="submit" name="submit" value="Submit" /></td></tr>\r\n</table>\r\n<input type="hidden" style="display:none" name="filename" value="')
        __M_writer(escape(c.filename))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="case" value="')
        __M_writer(escape(c.case))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="customer" value="')
        __M_writer(escape(c.customer))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="email" value="')
        __M_writer(escape(c.email))
        __M_writer(u'" />\r\n</form>\r\n\r\n\r\n<table>\r\n<tr><td>File:</td><td>')
        __M_writer(escape(c.filename))
        __M_writer(u'</td></tr>\r\n<tr><td>Engineer:</td><td>')
        __M_writer(escape(c.email))
        __M_writer(u'</td></tr>\r\n<tr><td>customer:</td><td>')
        __M_writer(escape(c.customer))
        __M_writer(u'</td></tr>\r\n<tr><td>Case number:</td><td>')
        __M_writer(escape(c.case))
        __M_writer(u'</td></tr>\r\n</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\r\n   <head>\r\n      <title>LAGER - LDEV Report</title>\r\n   </head>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 7, "36": 25, "37": 26, "38": 26, "39": 26, "40": 28, "41": 31, "42": 31, "43": 32, "44": 32, "45": 33, "46": 33, "47": 34, "48": 34, "49": 39, "50": 39, "51": 40, "52": 40, "53": 41, "54": 41, "55": 42, "56": 42, "62": 3, "66": 3, "72": 66}, "uri": "ldev_report.mako", "filename": "/home/chodges/lager-pylons/lager/lager/lager/templates/ldev_report.mako"}
__M_END_METADATA
"""
