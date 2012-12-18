===== 
ddg
===== 
`Duck Duck Go`_ zero-click api for your command-line

Install
=======

    pip install ddg

or from the source:

    python setup.py install


Usage
======

www.duckduckgo.com zero-click api for your command-line [-h] [-b] [-d] [-j] [-l] [-s] [-u] [query [query ...]]  

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

Call ddg from your command line to access the `Duck Duck Go Zero-Click Info API`_

:: 
    
    $ ddg my ip
    Your IP address is <ip> in <location>

:: 

    $ ddg 2*10+3*0
    2 * 10 + 3 * 0 = 20

::
    
    $ ddg schnauzer
    A schnauzer is a dog breed that originated in Germany in the 15th and 16th centuries.

If you want the url of the answer source you can use the `-u` flag

:: 

    $ ddg schnauzer -u
    https://en.wikipedia.org/wiki/Schnauzer

Or you can use the `-l` flag which will launch the url in a new tab of your browser

::

    $ ddg schnauzer -l

You can use the -b (--bang) flag to launch a `!Bang redirect`_ in your browser

Launch the `Python'_ documentation page for the webbrowser module
::

    $ ddg py webbrowser -b

Launch a query on `Wolfram Alpha`_
::

    $ ddg wa integral of sin x / x from negative inf to inf -b

Launch a search on `Stack Overflow`_
::

    $ ddg so [c++11] lambda return values -b

You can search directly on `Duck Duck Go`_ with the `-s` flag
::
    $ ddg The Simpsons -s

ddg plays nice with all the unix-like utilities you know and love

::

   $ echo "shark" | ddg -l
   Launches `https://en.wikipedia.org/wiki/Shark <https://en.wikipedia.org/wiki/Shark>` in your web browser

    $ ddg Abraham Lincoln -j >> file.txt
    Returns the 'raw json output <http://api.duckduckgo.com/?q=Abraham+Lincoln&format=json&pretty=1>` from the duckduckgo zero-click api query and inserts it to a file

Thanks
=======
| The duckduckgo module is a modification from http://github.com/crazedpsyc/python-duckduckgo.  
| Original duckduckgo module source from http://github.com/mikejs/python-duckduckgo (outdated)  

.. _Duck Duck Go: http://www.duckduckgo.com
.. _Duck Duck Go Zero-Click Info API: http://http://api.duckduckgo.com/
.. _!Bang redirect: http://duckduckgo.com/bang.html
.. _Python: http://www.python.com
.. _Rotten Tomatoes: http://www.rottentomatoes.com
.. _Stack Overflow: http://www.stackoverflow.com
.. _Wolfram Alpha: http://www.wolframalpha.com
.. _https://en.wikipedia.org/wiki/Schnauzer: https://en.wikipedia.org/wiki/Schnauzer
