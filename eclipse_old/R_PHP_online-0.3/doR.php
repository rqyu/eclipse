<?
// -----------------------------------------------------------
// R_PHP_Online
// Made by Steve Chen - version 0.3
// GPL licensed
// 
// Web site = http://steve-chen.net/R_PHP/
// e-mail   = steve@stat.tku.edu.tw
// 
//   Version History :
//     v0.1 (10 June 2003)  : initial release
//     v0.2 (13 June 2003)  : security fix
//     v0.3 (14 June 2003)  : improved banned-function input
// -----------------------------------------------------------

require "security.php";

// -------------------------------- Configuration
// The temorary directory for generated files under current directory
$temp_dir = "tmp";

// Unix system:

$R_path = "/usr/local/lib/R/bin/R";
$R_options_1 = "BATCH --slave --no-save";
$R_options_2 = "";
$graphic = "bitmap";

// for Windows system: 
//
//      $R_path = "c:/R/rw1070/bin/Rterm.exe";
//    or
//      $R_path = "c:\\R\\rw1070\\bin\\Rterm.exe";
// 
//    $R_options_1 ="--quiet --no-restore --no-save  < ";
//    $R_options_2 =" > ";
// 
//    $graphic = "jpeg";
// -------------------------------- end of Configuration
?>
<HTML>
<HEAD>
<TITLE>R_PHP</TITLE>
</HEAD>
<BODY>
&nbsp;<P>
<CENTER>
<B><A href=index.html><FONT size=5>R_PHP_Online</FONT></A><FONT size=3>&nbsp;
-- Online PHP CGI for R program</FONT><P>
by <A HREF="mailto:steve@stat.tku.edu.tw"><font size=2>Steve Chen</font></a>
in <A HREF="http://www.stat.tku.edu.tw" target=_blank>Department of Statistics</A>,
<A HREF="http://www.tku.edu.tw" target=_blank>TKU</A>,
Taipei, Taiwan<p>                               


<A href=doR.html>Input R code again</A></CENTER>
<P>
<TABLE align=center><TR><TD>

<?
function random_str($size) 
{ 
        $randoms = array( 
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, 
                c, d, e, f, g, h, i, j, k, l, m, n, 
                o, p, q, r, s, t, u, v, w, x, y, z 
        ); 

        srand ((double) microtime() * 1000000); 

        for($i = 1; $i <= $size; $i++) 
            $text .= $randoms[(rand(0,35))]; 

        return $text; 
} 

function get_file_name($text)
{
  // Unix   : bitmap(file="something.jpg")
  // Windows: jpeg(file="something.jpg")

  $temp1 = explode("file=\"",$text);
  $fname = explode("\"",$temp1[1]);

  return $fname[0];
}
$r_code = $_POST["r_code"];
if (!$r_code || $r_code == "")
{
  echo "<font color=red>No program code enterred!</font><p>";
  echo "</TD></TR></TABLE></BODY></HTML>";
  exit;
}

$old_code = explode(chr(10),$r_code);
$total = count($old_code);
$new_code = "";

for ($i=0;$i < $total; $i++)
{
  // replace original graphic file name with a random name
  // Windows system if (ereg("jpeg",$old_code[$i]))

  // if (ereg("bitmap",$old_code[$i]))

  $j = $i+1;
  $old = $old_code[$i];

  check_bad($old,$j);

  if (ereg("$graphic",$old_code[$i]))
  {
     $gfile_name = get_file_name($old_code[$i]);
     $gfile_name = random_str(4).$gfile_name;
     
     // $new_code .= "bitmap(file=\"$temp_dir/$gfile_name\") \n";
     $new_code .= $graphic."(file=\"$temp_dir/$gfile_name\") \n";
  }
  else
     $new_code .= $old_code[$i]."\n";
}

$r_name = random_str(10);
$r_input = $temp_dir."/".$r_name.".R";
$r_output = $temp_dir."/".$r_name.".Rout";

$fp = fopen($r_input,"w");
fwrite($fp,$new_code);
fclose($fp);

// $rsoft = "/usr/local/lib/R/bin/R";
$rsoft = $R_path;

// Unix :
//    R BATCH --slave --no-save $r_input $r_output
//
// Windows :
//    Rterm.exe --quiet --no-restore --no-save < test.R > test.Rout

// $command = "$rsoft BATCH --slave --no-save $r_input $r_output";

$command = "$rsoft $R_options_1 $r_input $R_options_2 $r_output";
$exec_result = exec($command,$result,$error);

$lines = file($r_output);
$total = count($lines);

if ($error)
{
  echo "<font color=red>Error: Something wrong! Please check output!</font>";
  echo "<HR>Output of R program : <P><HR>";

  for ($i=0;$i < $total;$i++)
    echo $lines[$i]."<BR>";

  exit;
}

echo "Output of R program¡G<P><HR>";

$to_do_plot = 0;

for ($i=0;$i < $total;$i++)
{
  $line = $lines[$i];

  // Unix   : if (ereg("bitmap",$line))
  // Windows: if (ereg("jpeg",$line))

  if (ereg("$graphic",$line))
  {
    echo $line."<BR>";

    $gfile_name = get_file_name($line);
    $to_do_plot = 1;
    // echo "<P><IMG SRC=\"$file_name\"><P>";
  }
  else if (ereg("dev.off",$line))
  {
    echo $line."<BR>";

    if ($to_do_plot == 1)
    { 
      echo "<P><IMG SRC=\"$gfile_name\"><P>";
      $to_do_plot = 0;
    }
  }
  else if (ereg("null device",$line))
    continue;
  else if (ereg("          1",$line))
    continue;
  else
    echo $line."<BR>";
}

?>
</TD><TR></TABLE>
</BODY>
</HTML>
