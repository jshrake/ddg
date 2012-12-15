ddg
===
www.duckduckgo.com zero click api for your shell

Usage
===
www.duckduckgo.com zero click api for your shell [-h] [-b] [-d] [-j]
                                                 [-l] [-s] [-u]
                                                 [query [query ...]]
  
positional arguments:  
  query         the search query
  
optional arguments:  
  -h, --help    show this help message and exit  
  -b, --bang    prefixes your query with !  
  -d, --define  prefixes your query with define  
  -j, --json    returns the raw json output  
  -l, --lucky   launches the first url found  
  -s, --search  launch a search on www.duckduckgo.com  
  -u, --url     returns urls found rather than text  

Examples
===
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

ddg Barack Obama -j >> file.txt
  Returns the json output of the search and inserts it to a file


Requires
===
Python 2.7.3 or greater


