"""
This file contians code for quering embeddings and finding the nearest neighbors
"""

import argparse
import numpy as np
from sklearn.neighbors import KDTree


class QueryEmbds():
    def __init__(
        self,
        embeddings,
        leaf_size=30,
        metric='euclidean',
    ):
        self.embeddings = embeddings
        self.metric = metric
        self.leaf_size = leaf_size
        self.kdt = KDTree(
            self.embeddings,
            leaf_size=self.leaf_size,
            metric=self.metric,
        )

    def query(self, query_embd):
        dist, ind = self.kdt.query(
            query_embd.reshape(1, -1),
            k=self.embeddings.shape[0],
            dualtree=True
            )
        return dist, ind


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-e',
        default=None,
        help='Path to the npy file containing image embeddings',
    )
    parser.add_argument(
        '-q',
        default=None,
        help=("Path to the npy file containing the query's image embedding. "
        "This depicts the user's input's image embedding"),
    )
    parser.add_argument(
        '-l',
        default=30,
        help=('Number of points at which to switch to brute-force for the '
        'KDTree algorithm'),
    )
    parser.add_argument(
        '-d',
        default='euclidean',
        help='The distance metric to use for querying the KDTree',
    )
    args = parser.parse_args()

    if args.e is not None:
        embeddings = np.load(args.e)
    else:
        embeddings = np.random.randn(100, 1248)

    if args.q is not None:
        query_embed = np.load(args.q)
    else:
        query_embed = np.random.randn(1, 1248)

    query_cls = QueryEmbds(
        embeddings,
        leaf_size=args.l,
        metric=args.d
    )
    dist, ind = query_cls.query(query_embed)

    print(f'Embedding at location {ind[0][0]} is the'
    f' closest with distance of {np.round(dist[0][0], 2)}')
