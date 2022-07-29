
import argparse
from flask import Flask, render_template, request

from kg_query.main import RankedList


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
    if 'submit' in request.form.keys():
        query_number = int(request.form['query'])
        images_ranked_list, uris_ranked_list = ranked_list.generate_results(
            query_number
        )
    else:
        images_ranked_list, uris_ranked_list = ranked_list.generate_results(
            10000
        )
    images_path = ["/".join(item.split('/')[-2:]) for item in images_ranked_list]
    return render_template(
        'index.html',
        image_list=images_path,
        uris_list=uris_ranked_list,
        iteration = len(images_path),
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
