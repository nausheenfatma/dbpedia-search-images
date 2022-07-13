
import argparse
import urllib.request
from pprint import pprint
from rdflib import sparqlEndpoint


def save_image(input_dict, filename):
    """
    Method to save an image given the image link
    """
    image_link = input_dict['image']['value']
    file = open(filename, 'wb')
    file.write(urllib.request.urlopen(image_link).read())
    file.close()
    return None
