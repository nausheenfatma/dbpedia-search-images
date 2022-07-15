
import os
import argparse
from tqdm import tqdm

from utils import save_image
from rdflib import sparqlEndpoint


def save_batch(output, dir_path):
    count = 0
    for input_dict in tqdm(output):
        count += 1
        image_path = os.path.join(dir_path, f'{count}.jpg')
        try:
            save_image(input_dict, image_path)
        except:
            print(f'Issue saving image number {count}')
            os.system(f'rm {image_path}')
    return None


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
    parser.add_argument(
        '--save_dir',
        '-sd',
        default='''/Users/siddhantbansal/Desktop/IIIT-H/GSoC_2022/Code/image-search-gsoc-2022/dataset/test_run''',
        help='Path to the directory to save the images into',
    )
    args=parser.parse_args()
    print("Generating image's links...")

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
    print("Saving images...")
    save_batch(output, args.save_dir)
