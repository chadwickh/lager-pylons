<%inherit file="/base.mako" />

<%def name="head_tags()">
   <head>
      <title>LAGER - Unknown file type</title>
   </head>
</%def>

I'm sorry, I don't understand this file type.  If you'd like this added as a feature please contact <a href="mailto:chad.hodges@lumenate.com">Chad Hodges.</a>

<table>
<tr><td>File:</td><td>${c.filename}</td></tr>
<tr><td>Engineer:</td><td>${c.email}</td></tr>
<tr><td>customer:</td><td>${c.customer}</td></tr>
<tr><td>Case number:</td><td>${c.case}</td></tr>
</table>
