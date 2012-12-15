import urllib
import urllib2
import json as j


def search(query, **kwargs):
    """
    Abstract: topic summary (can contain HTML, e.g. italics)
    AbstractText: topic summary (with no HTML)
    AbstractSource: name of Abstract source
    AbstractURL: deep link to expanded topic page in AbstractSource
    Image: link to image that goes with Abstract
    Heading: name of topic that goes with Abstract

    Answer: instant answer
    AnswerType: type of Answer, e.g. calc, color, digest, info, ip, iploc, phone, pw, rand, regexp, unicode, upc, or zip (see goodies & tech pages for examples).

    Definition: dictionary definition (may differ from Abstract)
    DefinitionSource: name of Definition source
    DefinitionURL: deep link to expanded definition page in DefinitionSource

    RelatedTopics: array of internal links to related topics associated with Abstract
      Result: HTML link(s) to related topic(s)
      FirstURL: first URL in Result
      Icon: icon associated with related topic(s)
        URL: URL of icon
        Height: height of icon (px)
        Width: width of icon (px)
      Text: text from first URL

    Results: array of external links associated with Abstract
      Result: HTML link(s) to external site(s)
      FirstURL: first URL in Result
      Icon: icon associated with FirstURL
        URL: URL of icon
        Height: height of icon (px)
        Width: width of icon (px)
      Text: text from FirstURL

    Type: response category, i.e. A (article), D (disambiguation), C (category), N (name), E (exclusive), or nothing.

    Redirect: !bang redirect URL
    """

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
        json = j.loads(response.read())
        response.close()
        return Results(json)
    except urllib2.HTTPError, err:
        print 'HTTPError = ' + str(err.code)
    except urllib2.URLError, err:
        print 'URLError = ' + str(err.reason)
    except urllib2.HTTPException:
        print 'HTTPException'
    except Exception:
        import traceback
        print traceback.format_exec()
    import sys
    sys.exit()


class Results(object):
    def __init__(self, json):
        self.json = j.dumps(json, indent=2)
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
