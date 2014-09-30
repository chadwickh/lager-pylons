from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1256339306.0115399
_template_filename='/lager/lager/lager/templates/cache_usage.mako'
_template_uri='cache_usage.mako'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(u'\r\n\r\nThis is the cache usage report, from Tuning Manager.  For this type of report we plot three data series, as follows:\r\n\r\n<ul>\r\n<li> Cache Usage Percent</li>\r\n<li> Cache Sidefile Percent</li>\r\n<li> Cache Write Pending Percent</li>\r\n</ul>\r\n\r\n<form name="cache_usage_plot" method="POST" action="/graphme/plot_cache_usage" enctype="multipart/form-data">\r\n<table>\r\n<tr><td></td><td><input type="submit" name="submit" value="Submit" /></td></tr>\r\n</table>\r\n<input type="hidden" style="display:none" name="filename" value="')
        # SOURCE LINE 21
        __M_writer(escape(c.filename))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="case" value="')
        # SOURCE LINE 22
        __M_writer(escape(c.case))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="customer" value="')
        # SOURCE LINE 23
        __M_writer(escape(c.customer))
        __M_writer(u'" />\r\n<input type="hidden" style="display:none" name="email" value="')
        # SOURCE LINE 24
        __M_writer(escape(c.email))
        __M_writer(u'" />\r\n</form>\r\n\r\n\r\n\r\n<table>\r\n<tr><td>File:</td><td>')
        # SOURCE LINE 30
        __M_writer(escape(c.filename))
        __M_writer(u'</td></tr>\r\n<tr><td>Engineer:</td><td>')
        # SOURCE LINE 31
        __M_writer(escape(c.email))
        __M_writer(u'</td></tr>\r\n<tr><td>customer:</td><td>')
        # SOURCE LINE 32
        __M_writer(escape(c.customer))
        __M_writer(u'</td></tr>\r\n<tr><td>Case number:</td><td>')
        # SOURCE LINE 33
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
        __M_writer(u'\r\n   <head>\r\n      <title>LAGER - Cache Usage</title>\r\n   </head>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


