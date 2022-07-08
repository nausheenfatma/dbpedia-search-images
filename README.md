# Enhancing DBpedia with image-based querying

Currently, users can query DBpedia using text. Although text as an input is an efficient approach to query the graph, there are cases where we do not know what we are seeing. How does one search the knowledge graph (KG) in such cases? Imagine being able to query the DBpedia Knowledge Graph (DB-KG) using images!

The idea here is to create a framework that can combine existing computer vision techniques with knowledge graphs. Doing this will enable us to query the existing knowledge graphs using multiple modalities: images and text. Therefore, in this proposal, we examine and explore two aspects of DB-KG:

-  A framework to create an image-based KG out of existing DBpedia entries;
- Using the graph created to perform tasks like image querying, text + image search, and using relevant input images to add more images to existing articles.

## Instructions to scrape images from DBpedia and Wikipedia articles

TODO: Details will be added as the project progresses.

## Instructions to generate embeddings for images

### Generate features for an images saved at a location
Use the following command to run `main.py` and generate features for an image.

```python
python img-models/main.py -p /path/to/image.jpg -m resnet50
```

`main.py` accepts two arguments
- `p`: Path to the image for which the features are to be generated
- `m`: Name of the model to load for generating the features. Currently the options are: `resnet18`, `resnet50`, `resnet101`, and `resnet152`.

## Instructions to create the image-based knowledge graph

TODO: Details will be added as the project progresses.

## Instructions to query an image-based knowledge graph

### Load the Image Embeddings and Query them

For querying the images, we first convert them to embeddings. Once we have the embeddings, we create a KDTree out of them for fast querying.
After converting user's query image to an embedding, we use it to query the images' embeddings.

Use the following command to run `query_embds.py` and generate query the saved embeddings of images using a single image's embeddings.

```python
python kg-query/query_embds.py -e /path/to/embeddings.npy -q /path/to/query.npy -l 30 -d euclidean
```

`query_embds.py` accepts four arguments
- `e`: Path to the `npy` file containing images' embeddings that we want to query. These embeddings represent embeddings from the image-based KG created.
- `q`: Path to the `npy` file containing the query's image embedding. This depicts the user's input image's embeddings.
- `l`: Number of points at which to switch to brute-force for the KDTree algorithm.
- `d`: The distance metric to use for querying the KDTree.
