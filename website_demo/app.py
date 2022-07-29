
import os
import argparse
from flask import Flask, render_template, request

from kg_query.main import RankedList
from kg_query.query_embds import QueryEmbds


parser = argparse.ArgumentParser()
parser.add_argument(
    '-d',
    default=('/scratch/sid/dataset/'),
    help='Path to the directory containing positive and negative pairs'
)
args = parser.parse_args()

app = Flask(__name__, static_folder=args.d)

ranked_list = RankedList()

@app.route('/', methods=['POST', 'GET'])
def home():
    images_path = ranked_list.generate_results(5000)[:10]
    images_path = ["/".join(item.split('/')[-2:]) for item in images_path]
    return render_template(
        'index.html',
        image_list=images_path,
        iteration = len(images_path)
    )


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    stackoverflow.com/questions/13768007/browser-caching-issues-in-flask
    Working in Chrome, not in safari.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == '__main__':
    app.run(debug=True)
