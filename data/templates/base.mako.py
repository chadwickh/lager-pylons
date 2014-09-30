# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412041326.883988
_enable_loop = True
_template_filename = u'/home/chodges/lager-pylons/lager/lager/lager/templates/base.mako'
_template_uri = u'/base.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\r\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html>\r\n  <head>\r\n    <link rel="stylesheet" type="text/css" href="/lumenate_style.css" />\r\n    ')
        __M_writer(escape(self.head_tags()))
        __M_writer(u'\r\n  </head>\r\n  <body>\r\n    ')
        __M_writer(escape(self.body()))
        __M_writer(u'\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "16": 0, "22": 2, "23": 7, "24": 7, "25": 10, "26": 10}, "uri": "/base.mako", "filename": "/home/chodges/lager-pylons/lager/lager/lager/templates/base.mako"}
__M_END_METADATA
"""
