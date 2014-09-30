# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412042306.917228
_enable_loop = True
_template_filename = '/home/chodges/lager-pylons/lager/lager/lager/templates/display.mako'
_template_uri = 'display.mako'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        __M_writer(u'\r\n\r\n<table>\r\n<tr><td>Case number:</td><td>')
        __M_writer(escape(c.case))
        __M_writer(u'</td></tr>\r\n<tr><td>Customer:</td><td>')
        __M_writer(escape(c.customer))
        __M_writer(u'</td></tr>\r\n<tr><td>Engineer:</td><td>')
        __M_writer(escape(c.email))
        __M_writer(u'</td></tr>\r\n</table>\r\n')
        for filename in c.filenames:
            __M_writer(u'\t<img src="/')
            __M_writer(escape(filename))
            __M_writer(u'" />\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n   <head>\r\n      <title>LAGER - Output for case ')
        __M_writer(escape(c.case))
        __M_writer(u'</title>\r\n   </head>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 1, "34": 7, "35": 10, "36": 10, "37": 11, "38": 11, "39": 12, "40": 12, "41": 14, "42": 15, "43": 15, "44": 15, "50": 3, "55": 3, "56": 5, "57": 5, "27": 0, "63": 57}, "uri": "display.mako", "filename": "/home/chodges/lager-pylons/lager/lager/lager/templates/display.mako"}
__M_END_METADATA
"""
