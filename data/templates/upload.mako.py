# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412041326.879393
_enable_loop = True
_template_filename = '/home/chodges/lager-pylons/lager/lager/lager/templates/upload.mako'
_template_uri = 'upload.mako'
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
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        __M_writer(u'\r\n\r\n<p>Welcome to <b>LAGER</b>, the Lumenate Advanced Graphing Engine and Repository\r\n\r\n<p>This application takes the output from common performance monitoring tools and produces graphs.\r\n\r\n<p>At present it understands the output from HDS\' Tuning Manager.  Future enhancements will include HDS Performance Monitor\r\nand SAR data.  \r\n\r\n<p>For feature enhancements, including new reports, please contact <a href="mailto:chad.hodges@lumenate.com">Chad Hodges</a>\r\n<br />\r\n\r\n<form name="lager" method="POST" action="/graphme/upload" enctype="multipart/form-data">\r\n<table>\r\n<tr><td>Email Address:</td><td>  <input type="text" name="email" /></td></tr>\r\n<tr><td>Customer Name:</td><td>  <input type="test" name="customer" /></td></tr>\r\n<tr><td>File to Upload:</td><td> <input type="file" name="myfile" /></td></tr>\r\n<tr><td></td><td>                <input type="submit" name="submit" value="Submit" /></td></tr>\r\n</table>\r\n</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\r\n   <head>\r\n      <title>LAGER - Home</title>\r\n   </head>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 1, "33": 7, "39": 3, "43": 3, "49": 43, "27": 0}, "uri": "upload.mako", "filename": "/home/chodges/lager-pylons/lager/lager/lager/templates/upload.mako"}
__M_END_METADATA
"""
