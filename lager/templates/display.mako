<%inherit file="/base.mako" />

<%def name="head_tags()">
   <head>
      <title>LAGER - Output for case ${c.case}</title>
   </head>
</%def>

<table>
<tr><td>Case number:</td><td>${c.case}</td></tr>
<tr><td>Customer:</td><td>${c.customer}</td></tr>
<tr><td>Engineer:</td><td>${c.email}</td></tr>
</table>
%for filename in c.filenames:
	<img src="/${filename}" />
%endfor
