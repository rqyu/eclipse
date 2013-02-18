<?
// -----------------------------------------------------------
// R_PHP_Online
// Made by Steve Chen - version 0.2
// GPL licensed
//
// Web site = http://steve-chen.net/R_PHP/
// e-mail   = steve@stat.tku.edu.tw
//
//   Version History :
//     v0.1 (10 June 2003)  : initial release
//     v0.2 (13 June 2003)  : security fix
// -----------------------------------------------------------

require "security.php";
?>
<HTML>
<HEAD>
<TITLE>R_PHP</TITLE>
</HEAD>
<BODY>
&nbsp;<P>
<CENTER>
<B><FONT size=5>R_PHP_Online</FONT><FONT size=3>&nbsp;
-- Online PHP CGI for R program</FONT><P>
by <A HREF="mailto:steve@stat.tku.edu.tw"><font size=2>Steve Chen</font></a>
in <A HREF="http://www.stat.tku.edu.tw" target=_blank>Department of Statistics</
A>,
<A HREF="http://www.tku.edu.tw" target=_blank>TKU</A>,
Taipei, Taiwan<p>

</CENTER>
<HR align=center width=80%>
<P>
<TABLE align=center><TR><TD>
<a href=doR.html>Back to Demo</a> <P>

Here is a list of R functions that are not permitted in this server:<P>
<blockquote>
<?
sort($bad_cmd);
reset($bad_cmd);
foreach ($bad_cmd as $bad)
  echo $bad."<BR>";
?>
</blockquote>
</TD><TR></TABLE>
</BODY></HTML>
