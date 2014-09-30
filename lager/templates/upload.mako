<%inherit file="/base.mako" />

<%def name="head_tags()">
   <head>
      <title>LAGER - Home</title>
   </head>
</%def>

<p>Welcome to <b>LAGER</b>, the Lumenate Advanced Graphing Engine and Repository

<p>This application takes the output from common performance monitoring tools and produces graphs.

<p>At present it understands the output from HDS' Tuning Manager.  Future enhancements will include HDS Performance Monitor
and SAR data.  

<p>For feature enhancements, including new reports, please contact <a href="mailto:chad.hodges@lumenate.com">Chad Hodges</a>
<br />

<form name="lager" method="POST" action="/graphme/upload" enctype="multipart/form-data">
<table>
<tr><td>Email Address:</td><td>  <input type="text" name="email" /></td></tr>
<tr><td>Customer Name:</td><td>  <input type="test" name="customer" /></td></tr>
<tr><td>File to Upload:</td><td> <input type="file" name="myfile" /></td></tr>
<tr><td></td><td>                <input type="submit" name="submit" value="Submit" /></td></tr>
</table>
</form>
