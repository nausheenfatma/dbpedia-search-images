"""
This file contains initial code for utilising rdflib for querying DBpedia
"""

import argparse

from rdflib import Graph

parser = argparse.ArgumentParser()
parser.add_argument(
    '-l',
    default='https://databus.dbpedia.org/repo/sparql',
    help='Link to query for creating the graph',
)
# Default link source: http://dev.dbpedia.org/Download_Data
args = parser.parse_args()

g = Graph().parse(args.l)
q = """select ?e ?image where {
?e foaf:depiction ?image .
} OFFSET 0 LIMIT 100
"""

print('Graph created! Parsing the graph...')

counter = 0

for r in g.query(q):
    print(r)
    counter += 1
    print(counter)
