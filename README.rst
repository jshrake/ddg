===== 
ddg
===== 
duck duck go zero-click api for your command-line

Install
=======

>>>pip install ddg

Usage
======

usage: www.duckduckgo.com zero-click api for your command-line [-h] [-b] [-d] [-j] [-l] [-s] [-u] [query [query ...]]  

positional arguments:  
  query         the search query  

optional arguments:  
  -h, --help    show this help message and exit  
  -b, --bang    prefix query with ! and launch the redirect url  
  -d, --define  prefix query with define  
  -j, --json    returns the raw json output  
  -l, --lucky   launch the first url found  
  -s, --search  launch a search on www.duckduckgo.com  
  -u, --url     return the url of the result found  

Examples
========= 

ddg abelian group

    In abstract algebra, an abelian group, also called a commutative group, is a group in which the result of applying the group operation to two group elements does not depend on their order (the axiom of commutativity).

ddg rt Drive -b

    Equivalent to doing !rt Drive on www.duckduckgo.com
    Launches your browser and opens to the Rotten Tomatoes page for *Drive*

ddg py webbrowser -b

    Equivalent to doing !py webbrowser on www.duckduckgo.com
    Launches your browser and opens the Python documenation page for the webbrowser module

ddg my ip

    Your IP address is <ip> in <location>

ddg 2*10+3*0

    2 * 10 + 3 * 0 = 20

echo "shark" | ddg -u

    https://en.wikipedia.org/wiki/Shark

ddg Abraham Lincoln -j >> file.txt

    Returns the raw json output from the duckduckgo zero-click api query and inserts it to a file

Thanks
=======
The duckduckgo module is a modification from http://github.com/crazedpsyc/python-duckduckgo.
Original source: http://github.com/mikejs/python-duckduckgo (outdated)
Copyright Michael Stephens <me@mikej.st>, released under a BSD-style license.