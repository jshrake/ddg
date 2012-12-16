#!/usr/bin/env python
"""www.duckduckgo.com zero-click api for your command-line"""

import sys
import webbrowser
import argparse
import duckduckgo


def main():
    """Controls the flow of the ddg application"""

    'Build the parser and parse the arguments'
    parser = argparse.ArgumentParser('www.duckduckgo.com zero-click api for your command-line')
    parser.add_argument('query', nargs='*', help='the search query')
    parser.add_argument('-b', '--bang', action='store_true', help='prefix query with ! and launch the redirect url')
    parser.add_argument('-d', '--define', action='store_true', help='prefix query with define')
    parser.add_argument('-j', '--json', action='store_true', help='returns the raw json output')
    parser.add_argument('-l', '--lucky', action='store_true', help='launch the first url found')
    parser.add_argument('-s', '--search', action='store_true', help='launch a search on www.duckduckgo.com')
    parser.add_argument('-u', '--url', action='store_true', help='return the url of the result found')
    args = parser.parse_args()

    'Get the queries'
    if args.query:
        queries = [' '.join(args.query)]
    elif not sys.stdin.isatty():
        queries = sys.stdin.read().splitlines()
    else:
        parser.print_help()
        return

    'Determine if we need to add any prefixes based on user flags'
    prefix = 'define ' if args.define else ''

    if args.search:
        prefix = '!ddg ' + prefix
    elif args.bang:
        prefix = '! ' + prefix

    'Loop through each query'
    for query in queries:
        'Prefix the query'
        query = prefix + query

        'Get a response from www.duckduck.com using the duckduckgo module'
        results = duckduckgo.search(query)

        'If the user requested the raw JSON output, print it now and continue to the next query'
        if args.json:
            print results.json
            continue

        'Define a response priority to determine what order to look for an answer'
        redirect_mode = args.bang or args.search or args.lucky
        results_priority = ['redirect', 'result', 'abstract'] if redirect_mode else ['answer',  'abstract', 'result']

        'Insert the definition priority at the front or second to last depending on the -d flag'
        results_priority.insert(0 if args.define else len(results_priority) - 1, 'definition')

        'Search for an answer and respond accordingly based on user input args'
        failed_to_find_answer = True
        for r in results_priority:
            result = getattr(getattr(results, r), 'url' if (redirect_mode or args.url) else 'text')
            if result:
                webbrowser.open_new_tab(result) if (redirect_mode and not args.url) else print_result(result)
                failed_to_find_answer = False
                break

        'Let the user know if no answer was found'
        if failed_to_find_answer:
            if results.type == 'disambiguation':
                print 'Your query was ambiguous, please be more specific'
            else:
                print 'No results found'


def print_result(result):
    """Print the result, ascii encode if necessary"""
    try:
        print result
    except RuntimeError:
        print result.encode('ascii', 'ignore')
    except:
        print "Unexpected error attempting to print result"


if __name__ == "__main__":
    main()
