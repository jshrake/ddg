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

You can use the `-b` flag to launch a `!Bang redirect`_ in your browser

Launch a query on `Wolfram Alpha`_
::

    $ ddg wa integral of sin x / x from negative inf to inf -b

Launch a search on `Stack Overflow`_
::

    $ ddg so [c++11] lambda return values -b

Launch a search on `Python`_ for the webbrowser module
::

    $ ddg py webbrowser -b

Feeling lucky? Launch the `Python webbrowser documentation`_ directly with `-l`
::

    $ ddg python webbrowser -l

You can launch a `search on Duck Duck Go`_ with the `-s` flag
::
    $ ddg Lord of the Rings -s

ddg plays nice with all the unix-like utilities you know and love
::

   $ echo "shark" | ddg -l

Use `-j` to output the `json response`_ from the API
::

    $ ddg simpsons characters -j >> file.txt

You can even do a silly thing such as
::

    $ ls | ddg -u

Thanks
=======
| The duckduckgo module is a modification from http://github.com/crazedpsyc/python-duckduckgo.  
| Original duckduckgo module source from http://github.com/mikejs/python-duckduckgo (outdated)  

.. _Duck Duck Go: http://www.duckduckgo.com
.. _Duck Duck Go Zero-Click Info API: http://api.duckduckgo.com/
.. _!Bang redirect: http://duckduckgo.com/bang.html
.. _Python: http://docs.python.org/2/search.html?q=webbrowser&check_keywords=yes&area=default
.. _Stack Overflow: http://stackoverflow.com/search?q=%5Bc%2B%2B11%5D%20lambda%20return%20values
.. _Wolfram Alpha: http://www.wolframalpha.com/input/?i=integral%20of%20sin%20x%20%2F%20x%20from%20negative%20inf%20to%20inf
.. _Python webbrowser documentation: http://docs.python.org/2/library/webbrowser.html
.. _search on Duck Duck Go: https://duckduckgo.com/?q=Lord%20of%20the%20Rings
.. _json response: http://api.duckduckgo.com/?q=simpsons+characters&format=json&pretty=1
