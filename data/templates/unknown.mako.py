# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412041480.130899
_enable_loop = True
_template_filename = '/home/chodges/lager-pylons/lager/lager/lager/templates/unknown.mako'
_template_uri = 'unknown.mako'
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
        __M_writer(u'\r\n\r\nI\'m sorry, I don\'t understand this file type.  If you\'d like this added as a feature please contact <a href="mailto:chad.hodges@lumenate.com">Chad Hodges.</a>\r\n\r\n<table>\r\n<tr><td>File:</td><td>')
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
        __M_writer(u'\r\n   <head>\r\n      <title>LAGER - Unknown file type</title>\r\n   </head>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 1, "34": 7, "35": 12, "36": 12, "37": 13, "38": 13, "39": 14, "40": 14, "41": 15, "42": 15, "48": 3, "52": 3, "58": 52, "27": 0}, "uri": "unknown.mako", "filename": "/home/chodges/lager-pylons/lager/lager/lager/templates/unknown.mako"}
__M_END_METADATA
"""
