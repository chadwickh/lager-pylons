<%inherit file="/base.mako" />

<%def name="head_tags()">
   <head>
      <title>LAGER - Cache Usage</title>
   </head>
</%def>

This is the cache usage report, from Tuning Manager.  For this type of report we plot three data series, as follows:

<ul>
<li> Cache Usage Percent</li>
<li> Cache Sidefile Percent</li>
<li> Cache Write Pending Percent</li>
</ul>

<form name="cache_usage_plot" method="POST" action="/graphme/plot_cache_usage" enctype="multipart/form-data">
<table>
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
