=====
ddg
===== 
`Duck Duck Go`_ zero-click api for your command-line

Install
=======
::

    $ pip install ddg

or from the source:
::

    $ python setup.py install

Usage
======
www.duckduckgo.com zero-click api for your command-line [-h] [-b] [-d] [-j] [-l] [-s] [-u] [query [query ...]]  

positional arguments:  
  query         the search query  

optional arguments:  
  -h, --help    show this help message and exit  
  -b, --bang    prefix query with ! and launch the redirect url  
  -d, --define  return the definition  
  -j, --json    returns the raw json output  
  -l, --lucky   launch the first url found  
  -s, --search  launch a search on www.duckduckgo.com  
  -u, --url     return the url of the result found  

Examples
========= 
Call ddg from your command line to access the `Duck Duck Go Zero-Click Info API`_ ::
    
    $ddg red-black tree
    A red–black tree is a type of self-balancing binary search tree, a data structure 
    used in computer science, typically used to implement associative arrays.

Get the url of the answer source ::

    $ ddg red-black tree -u
    https://en.wikipedia.org/wiki/Red-black_tree

Combinining flags behaves as expected ::

    $ ddg schnauzer -d -u
    http://www.merriam-webster.com/dictionary/schnauzer

Launch a `!Bang redirect`_ in your web browser with the `-b` flag

Launch a query on `Wolfram Alpha`_ ::

    $ ddg wa integral of sin x / x from negative inf to inf -b

Launch a search on `Stack Overflow`_ ::

    $ ddg so [c++11] lambda return values -b

Launch a `search on Duck Duck Go`_ with the `-s` flag ::

    $ ddg Lord of the Rings -s

Launch `the answer url`_ directly with `-l` ::

    $ ddg python webbrowser -l

ddg plays nice with other utilities in your shell ::

   $ echo "shark" | ddg -dl

::

  $ ddg welsh corgi -u | pbcopy

:: 
  
  $ ls | ddg -du

Use `-j` to output the `json response`_ from the API :: 

    $ ddg simpsons characters -j >> file.txt


Thanks
=======
| The duckduckgo module is a modification from http://github.com/crazedpsyc/python-duckduckgo.  
| Original duckduckgo module source from http://github.com/mikejs/python-duckduckgo (outdated)  

.. _Duck Duck Go: http://www.duckduckgo.com
.. _Duck Duck Go Zero-Click Info API: http://api.duckduckgo.com/
.. _!Bang redirect: http://duckduckgo.com/bang.html
.. _Stack Overflow: http://stackoverflow.com/search?q=%5Bc%2B%2B11%5D%20lambda%20return%20values
.. _Wolfram Alpha: http://www.wolframalpha.com/input/?i=integral%20of%20sin%20x%20%2F%20x%20from%20negative%20inf%20to%20inf
.. _the answer url: http://docs.python.org/2/library/webbrowser.html
.. _search on Duck Duck Go: https://duckduckgo.com/?q=Lord%20of%20the%20Rings
.. _json response: http://api.duckduckgo.com/?q=simpsons+characters&format=json&pretty=1
