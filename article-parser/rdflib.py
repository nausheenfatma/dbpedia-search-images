"""
This file contains initial code for utilising rdflib for querying DBpedia
"""

import sys
import json
import logging
import argparse
import http.client
from pprint import pprint
import urllib.request, urllib.parse, urllib.error


def query_dbpedia(
    query,
    endpoint="http://dbpedia.org/sparql",
    graph="http://dbpedia.org",
    format="JSON",
    cxml_subjs="121",
    cxml_hrefs="",
    timeout="600",
    debug="on",
):
    param = dict()
    param["default-graph-uri"] = graph
    param["query"] = query
    param["format"] = format
    param["CXML_redir_for_subjs"] = cxml_subjs
    param["CXML_redir_for_hrefs"] = cxml_hrefs
    param["timeout"] = timeout
    param["debug"] = debug
    try:
        resp = urllib.request.urlopen(
            endpoint + "?" + urllib.parse.urlencode(param)
        )
        j = resp.read()
        resp.close()
    except (urllib.error.HTTPError, http.client.BadStatusLine):
        logging.debug("*** Query error. Empty result set. ***")
        j = '{ "results": { "bindings": [] } }'
    sys.stdout.flush()
    return json.loads(j)

def sparqlEndpoint(
    query,
    endpoint,
    graph,
    format,
    cxml_subjs,
    cxml_hrefs,
    timeout,
    debug,
):
      j=query_dbpedia(
          query,
          endpoint=endpoint,
          graph=graph,
          format=format,
          cxml_subjs=cxml_subjs,
          cxml_hrefs=cxml_hrefs,
          timeout=timeout,
          debug=debug,
      )
      return j.get('results').get('bindings')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--endpoint',
        '-e',
        default="http://dbpedia.org/sparql",
        help='Link to the endpoint',
    )
    parser.add_argument(
        '--graph',
        '-g',
        default="http://dbpedia.org",
        help='Link to the graph',
    )
    parser.add_argument(
        '--format',
        '-f',
        default='JSON',
        help='Format to get the output in',
    )
    parser.add_argument(
        '--subjs_cxml',
        '-s',
        default='121',
        help='TODO',
    )
    parser.add_argument(
        '--hrefs_cxml',
        '-c',
        default='',
        help="TODO",
    )
    parser.add_argument(
        '--timeout',
        '-t',
        default='600',
        help='Amount of timeout seconds',
    )
    parser.add_argument(
        '--debug',
        '-d',
        default='on',
        help='Debug?',
    )
    parser.add_argument(
        '--query',
        '-q',
        default='''select ?e ?image where { ?e dbo:thumbnail ?image . } LIMIT 100''',
        help='query string',
    )
    args=parser.parse_args()

    output = sparqlEndpoint(
        query=args.query,
        endpoint=args.endpoint,
        graph=args.graph,
        format=args.format,
        cxml_subjs=args.subjs_cxml,
        cxml_hrefs=args.hrefs_cxml,
        timeout=args.timeout,
        debug=args.debug,
    )
    pprint(output)
