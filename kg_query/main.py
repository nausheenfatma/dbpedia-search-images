"""
Code to lead the embeddings saved, get the query image, and query on the dataset
"""

import os
import argparse
import numpy as np

from .query_embds import QueryEmbds


parser = argparse.ArgumentParser()
parser.add_argument(
    '-d',
    default='/scratch/sid/dataset_embeddings',
    help='Path to the directory containing the embeddings',
)
args = parser.parse_args()


class RankedList():
    def __init__(self):
        pass

    def load_dict(self, dict_):
        output = list()
        img_path = list()
        for key, value in dict_.items():
            output.append(np.expand_dims(value.cpu().detach().numpy(), axis=0))
            img_path.append(key)
        return output, img_path

    def load_embeddings(self, embed_path='/scratch/sid/dataset_embeddings'):
        print('Loading the embeddings...')
        birds = np.load(
            os.path.join(embed_path, 'birds_embeddings.npy'),
            allow_pickle=True,
        ).item()
        weapons = np.load(
            os.path.join(embed_path, 'weapons_embeddings.npy'),
            allow_pickle=True,
        ).item()
        historic_places = np.load(
            os.path.join(embed_path, 'historic_places_embeddings.npy'),
            allow_pickle=True,
        ).item()
        politician = np.load(
            os.path.join(embed_path, 'politician_embeddings.npy'),
            allow_pickle=True,
        ).item()
        reptile = np.load(
            os.path.join(embed_path, 'reptile_embeddings.npy'),
            allow_pickle=True,
        ).item()

        print('Concatenating the embeddings...')
        embds = list()
        embds.extend(self.load_dict(birds)[0])
        embds.extend(self.load_dict(weapons)[0])
        embds.extend(self.load_dict(historic_places)[0])
        embds.extend(self.load_dict(politician)[0])
        embds.extend(self.load_dict(reptile)[0])

        img_paths = list()
        img_paths.extend(self.load_dict(birds)[1])
        img_paths.extend(self.load_dict(weapons)[1])
        img_paths.extend(self.load_dict(historic_places)[1])
        img_paths.extend(self.load_dict(politician)[1])
        img_paths.extend(self.load_dict(reptile)[1])

        embeddings = np.concatenate(embds, axis=0)
        return embeddings, img_paths

    def generate_results(self, query_index):
        embeddings, img_paths = self.load_embeddings()
        print('Querying the embeddings...')
        queryembd = QueryEmbds(embeddings)
        _, ind = queryembd.query(embeddings[query_index])
        print('Generating the ranked list...')
        ranked_list = list()
        for pred in ind[0]:
            ranked_list.append(img_paths[pred])
        return ranked_list


if __name__ == '__main__':
    ranked_list = RankedList()
    results = ranked_list.generate_results(0)
    print(results[:10])
