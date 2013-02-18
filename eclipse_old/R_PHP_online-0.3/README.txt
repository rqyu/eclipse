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

R_PHP_Online version 0.3

by Steve Chen (steve@stat.tku.edu.tw)


R_PHP_Online is a PHP CGI web interface to run R program online, 
including graphic output. 

R_PHP_Online is released under GPL license

R_PHP_Online can be used in both Unix and Windows OS

You can check out a more complicated application on Net-Stat 
in Dept. of Statistics, TKU (http://netstat.tku.edu.tw), 
which will be released as GPL as soon as modulization codes 
are completed. 

You can download recent version of R_PHP_Online on
http://steve-chen.net/R_PHP

Installation:

 1.To show graphics, your UNIX system must have ghostscript installed 
   For Windows system, you need only a web server and PHP installed.

 2.Uncompress the whole file under some directory in your web page

 3.Create a sub-directory "tmp" on that directory with 
   web writable permissions

 4.Modify the first few lines in doR.php according to your setup. 

 5.Modify security.txt for not-allowed R functions (security check). 
   Starting from version 0.3, you can now ban ONLY an option in a function.
   For example, in security.txt:

   cat | file=

   will ban cat function ONLY when "file=" option is present

 6.Set up a cron job to clear junks in tmp directory. For example,

   # check every 10 minutes to delete *.jpg files older than 10 min
   # the following 2 lines should be written as 1 line
   */10 * * * * /usr/bin/find /myWeb/R_PHP/tmp  -name '*.jpg' -cmin +10 -exec rm '{}' ';' > /dev/null 2>&1 

