from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1256338852.5241649
_template_filename='/lager/lager/lager/templates/array_group.mako'
_template_uri='array_group.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
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
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        range = context.get('range', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(u'\r\n\r\nThis is an Array Group report, from Tuning Manager.  For this type of report we generate four plots, as follows:\r\n\r\n<ul>\r\n<li> Top X parity groups by Maximum IOPS</li>\r\n<li> Top X parity groups by Average IOPS</li>\r\n<li> Top X parity groups by Maximum MB/s</li>\r\n<li> Top X parity groups by Average MB/s</li>\r\n</ul>\r\n\r\n<bold>NOTE:</bold>  There is a maximum of 30 parity groups for these plots<br />\r\n\r\nYou may choose the number of parity groups to report on below:\r\n\r\n<form name="array_group_plot" method="POST" action="/graphme/plot_array_group" enctype="multipart/form-data">\r\n<table>\r\n<tr><td>Number of parity groups to plot</td><td><select NAME="num_of_parity_groups">\r\n')
        # SOURCE LINE 25
        for i in range(30,0,-1):
            # SOURCE LINE 26
            __M_writer(u'   <option>')
            __M_writer(escape(i))
            __M_writer(u'\r\n')
        # SOURCE LINE 28
        __M_writer(u'</td></tr>\r\n<tr><td></td><td><input type="submit" name="submit" value="Submit" /></td></tr>\r\n</table>\r\n<input type="hidden" style="display:none" name="filename" value="')
        # SOURCE LINE 31
        __M_writer(escape(c.filename))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="case" value="')
        # SOURCE LINE 32
        __M_writer(escape(c.case))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="customer" value="')
        # SOURCE LINE 33
        __M_writer(escape(c.customer))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="email" value="')
        # SOURCE LINE 34
        __M_writer(escape(c.email))
        __M_writer(u'" />\r\n</form>\r\n\r\n\r\n<table>\r\n<tr><td>File:</td><td>')
        # SOURCE LINE 39
        __M_writer(escape(c.filename))
        __M_writer(u'</td></tr>\r\n<tr><td>Engineer:</td><td>')
        # SOURCE LINE 40
        __M_writer(escape(c.email))
        __M_writer(u'</td></tr>\r\n<tr><td>customer:</td><td>')
        # SOURCE LINE 41
        __M_writer(escape(c.customer))
        __M_writer(u'</td></tr>\r\n<tr><td>Case number:</td><td>')
        # SOURCE LINE 42
        __M_writer(escape(c.case))
        __M_writer(u'</td></tr>\r\n</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n   <head>\r\n      <title>LAGER - Array Group Report</title>\r\n   </head>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


