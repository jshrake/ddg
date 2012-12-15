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

    request = urllib2.Request(url, headers={'User-Agent': useragent})
    response = urllib2.urlopen(request)
    json = j.loads(response.read())
    response.close()

    return Results(json)


class Results(object):
    def __init__(self, json):
        self.json = j.dumps(json, indent=2)
        self.type = {'A': 'article', 'D': 'disambiguation',
                     'C': 'category', 'N': 'name',
                     'E': 'exclusive', '': 'nothing'}[json.get('Type', '')]
        self.answer = Answer(json)
        self.related = [Result(elem) for elem in json.get('RelatedTopics', [])]
        self.results = [Result(elem) for elem in json.get('Results', [])]
        self.abstract = Abstract(json)
        self.definition = Definition(json)
        self.redirect = Redirect(json)


class Result(object):
    def __init__(self, json):
        self.html = json.get('Result')
        self.text = json.get('Text')
        self.url = json.get('FirstURL')


class Abstract(object):
    def __init__(self, json):
        self.html = json.get('Abstract', '')
        self.text = json.get('AbstractText', '')
        self.url = json.get('AbstractURL', '')
        self.source = json.get('AbstractSource')
        self.heading = json.get('Heading', '')


class Answer(object):
    def __init__(self, json):
        self.text = json.get('Answer')
        self.type = json.get('AnswerType', '')


class Definition(object):
    def __init__(self, json):
        self.text = json.get('Definition', '')
        self.url = json.get('DefinitionURL')
        self.source = json.get('DefinitionSource')


class Redirect(object):
    def __init__(self, json):
        self.url = json.get('Redirect', '')
