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

$lines = file("security.txt");
$total = count($lines);

$j = 0;
for ($i=0;$i < $total;$i++)
{
  $line = trim($lines[$i]);

  if (!strrchr($line,"#"))
  {
    $j = $j + 1;
    
    if (strrchr($line,"|"))
    {
      $terms = explode("|",$line);
      $bad_0 = trim($terms[0]);
      $bad_op = trim($terms[1]);

      $bad_cmd[$j]= $bad_0;
      $bad_option[$bad_0] = $bad_op;
    }
    else
       $bad_cmd[$j]= $line;
  }
  else
    continue;
}
     

function check_bad($text,$j)
{
  global $bad_cmd,$bad_option;

  $is_bad = 0;
 
  foreach ($bad_cmd as $bad)
  {
    $bad1 = str_replace(".","\.",$bad);

    if (ereg($bad1,$text))
    {
      if (strrchr($bad,".") && (strlen($bad) > 3))
        $is_bad = 1;
      else
      {
        // get remaining string after targer key word
        $terms = explode($bad,$text);
        // get rid of spaces before a possible following "("
        $term1 = ltrim($terms[1]);

        if ($bad_option[$bad] != "")
        {
           if (eregi($bad_option[$bad],$term1))
           // if (strstr($term1,$bad_option[$bad]))
             $is_bad = 1;
        }
        else
        {
           if (substr($term1,0,1) == "(")
             $is_bad = 1;
        }
      }

      if ($is_bad == 1)
      {
         if ($bad_option[$bad] != "")
         {
           echo "<font color=red>$bad</font> function";
           echo " with <font color=red>".$bad_option[$bad]."</font>";
           echo " option is NOT permitted ";
         }
         else
           echo "<font color=red>$bad</font> function is NOT permitted ";
         echo "in Line <font color=red>$j</font><BR>";
         echo "<blockquote>$text</blockquote>";
         echo "Program Stopped!<BR>";
         exit;
      }
    }
 }
 // if ($is_bad == 0)
 //    echo $text."<BR>";
 // return true;
}

// $text = "cat   (\"file=   ";
// check_bad($text,2);

// Use: check_bad($text,2);
?>
