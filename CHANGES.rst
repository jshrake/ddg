Release history
###############


0.2.2 (2012-12-20)
==================

* Fixed the error handling for printing results with special characters

0.2.1 (2012-12-18)
==================

* When an exception is raised in the duckduckgo module, report the error
  and then return None. This allows ddg.py to continue to the next query
  rather than performing a sys.exit(1).
* Updated README
* Fixed formatting in LICENSE file
* Changed CHANGES to an rst file
* Updated the setup.py file
* Updated the help for all the input arguments

0.2.0 (2012-12-17)
==================

* Changed the behavior of the -d flag. Rather than prefixing the query with 
  `define`, now just prioritize the definition result when searching for an
  answer to the query.
* Updated README with more examples.

0.1.7 (2012-12-16)
==================

* Added a new trove classifier and made code more PEP8 compliant

0.1.6 (2012-12-16)
==================

* Fixed an issue with the -b prefix, please upgrade to the latest version 
  with pip install --upgrade ddg

0.1.5 (2012-12-15)
==================

* Updated license to MIT

0.1.4 (2012-12-15)
==================

* Using webbrowser rather than os dependent Popen commands

0.1.1 (2012-12-15)
==================

* First working version, initial release

