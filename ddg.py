#!/usr/bin/env python2
"""www.duckduckgo.com zero-click api for your command-line"""

import sys
import webbrowser
import argparse
import duckduckgo


def main():
    """Controls the flow of the ddg application"""

    'Build the parser and parse the arguments'
    parser = argparse.ArgumentParser(
        description='www.duckduckgo.com zero-click api for your command-line'
    )
    parser.add_argument('query', nargs='*', help='the search query')
    parser.add_argument('-b', '--bang', action='store_true',
                        help='open the !bang redirect url in a new browser tab')
    parser.add_argument('-d', '--define', action='store_true',
                        help='return the definition result')
    parser.add_argument('-j', '--json', action='store_true',
                        help='return the zero-click info api json response')
    parser.add_argument('-l', '--lucky', action='store_true',
                        help='open the result url in a new browser tab')
    parser.add_argument('-s', '--search', action='store_true',
                        help='launch a DuckDuckGo search in a new browser tab')
    parser.add_argument('-u', '--url', action='store_true',
                        help='return the result url')
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
    prefix = '!ddg ' if args.search else '!' if args.bang else ''

    'Loop through each query'
    for query in queries:
        'Prefix the query'
        query = prefix + query

        'Get a response from api.duckduck.com using the duckduckgo module'
        results = duckduckgo.search(query)

        'If results is null, continue to the next query'
        if not results:
            continue

        'Print the raw json output and return'
        if args.json:
            print_result(results.json)
            continue

        'a list of where to look for an answer first'
        results_priority = get_results_priority(args)

        'do we want the text or url output of the answer found'
        var = get_text_or_url(args)

        'action to perform when an answer is found'
        action = get_action(args)

        'Search for an answer and perform an action'
        failed_to_find_answer = True
        for r in results_priority:
            result = getattr(getattr(results, r), var)
            if result:
                action(result)
                failed_to_find_answer = False
                break

        'Let the user know if no answer was found'
        if failed_to_find_answer:
            if results.type == 'disambiguation':
                print 'Your query was ambiguous, please be more specific'
            else:
                print 'No results found'


def get_results_priority(args):
    """Return a result priority list based on user input"""
    redirect_mode = args.bang or args.search or args.lucky
    if redirect_mode:
        results_priority = ['redirect', 'result', 'abstract']
    else:
        results_priority = ['answer',  'abstract', 'result']

    insert_pos = 0 if args.define else len(results_priority)
    results_priority.insert(insert_pos, 'definition')
    return results_priority


def get_action(args):
    """Return a function to launch the web browser or print a result"""
    redirect_mode = args.bang or args.search or args.lucky
    if redirect_mode and not args.url:
        return webbrowser.open_new_tab
    else:
        return print_result


def get_text_or_url(args):
    """Determine if we need text or url output"""
    redirect_mode = args.bang or args.search or args.lucky
    if redirect_mode or args.url:
        return 'url'
    else:
        return 'text'


def print_result(result):
    """Print the result, ascii encode if necessary"""
    try:
        print result
    except UnicodeEncodeError:
        if sys.stdout.encoding:
            print result.encode(sys.stdout.encoding, 'replace')
        else:
            print result.encode('utf8')
    except:
        print "Unexpected error attempting to print result"


if __name__ == "__main__":
    main()
