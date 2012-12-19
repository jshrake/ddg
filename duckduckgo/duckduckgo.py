"""python wrapper for the duck duck go zero-click api"""

import urllib
import urllib2
import json as jsonlib


def search(query, **kwargs):
    useragent = 'py-ddg'
    params = {
        'q': query,
        'format': 'json',
        'pretty': '1',
        'no_redirect': '1',
        'no_html': '1',
        'skip_disambig': '1',
        }
    params.update(kwargs)
    enc_params = urllib.urlencode(params)
    url = 'http://api.duckduckgo.com/?' + enc_params

    try:
        request = urllib2.Request(url, headers={'User-Agent': useragent})
        response = urllib2.urlopen(request)
        json = jsonlib.loads(response.read())
        response.close()
        return Results(json)
    except urllib2.HTTPError, err:
        print 'Query failed with HTTPError code ' + str(err.code)
    except urllib2.URLError, err:
        print 'Query failed with URLError ' + str(err.reason)
    except Exception:
        print 'Unhandled exception'
        raise
    return None


class Results(object):
    def __init__(self, json):
        self.json = jsonlib.dumps(json, indent=2)
        self.type = {'A': 'article', 'D': 'disambiguation',
                     'C': 'category', 'N': 'name',
                     'E': 'exclusive', '': 'nothing'}[json['Type']]
        self.answer = Answer(json)
        self.result = Result(json.get('Results', None))
        self.abstract = Abstract(json)
        self.definition = Definition(json)
        self.redirect = Redirect(json)


class Result(object):
    def __init__(self, json):
        self.html = json[0].get('Result', '') if json else ''
        self.text = json[0].get('Text', '') if json else ''
        self.url = json[0].get('FirstURL', '') if json else ''


class Abstract(object):
    def __init__(self, json):
        self.html = json['Abstract']
        self.text = json['AbstractText']
        self.url = json['AbstractURL']
        self.source = json['AbstractSource']
        self.heading = json['Heading']


class Answer(object):
    def __init__(self, json):
        self.text = json['Answer']
        self.type = json['AnswerType']
        self.url = None


class Definition(object):
    def __init__(self, json):
        self.text = json['Definition']
        self.url = json['DefinitionURL']
        self.source = json['DefinitionSource']


class Redirect(object):
    def __init__(self, json):
        self.url = json['Redirect']
