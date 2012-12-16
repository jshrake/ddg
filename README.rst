===== 
ddg
===== 
duck duck go zero click api for your command-line

=======
Install
=======
pip install ddg

======
Usage
======

www.duckduckgo.com zero click api for your command-line [-h] [-b] [-d] [-j] [-l] [-s] [-u] [query [query ...]]
  
positional arguments:  
  query         the search query
  
optional arguments:  
  -h, --help    show this help message and exit  
  -b, --bang    prefixes your query with ! and launches the redirect in your browser  
  -d, --define  prefixes your query with define  
  -j, --json    returns the raw json output  
  -l, --lucky   launches the first url found in your browser  
  -s, --search  launch a search on www.duckduckgo.com  
  -u, --url     returns a url rather than text  

========= 
Examples
========= 

ddg Ryan Gosling
    Ryan Thomas Gosling is a Canadian actor and musician.

ddg rt Drive -b
    Equivalent to doing !rt Drive on www.duckduckgo.com, redirecting to the rotten tomatoes Drive page

ddg my ip
    Your IP address is <ip> in <location>

ddg 2*10+3*0
    2 * 10 + 3 * 0 = 20

echo "shark" | ddg -u
    https://en.wikipedia.org/wiki/Shark

ddg Abraham Lincoln -j >> file.txt
    Returns the raw json output from the duckduckgo zero-click api query and inserts it to a file