# Enhancing DBpedia with image-based querying

Currently, users can query DBpedia using text. Although text as an input is an efficient approach to query the graph, there are cases where we do not know what we are seeing. How does one search the knowledge graph (KG) in such cases? Imagine being able to query the DBpedia Knowledge Graph (DB-KG) using images!

The idea here is to create a framework that can combine existing computer vision techniques with knowledge graphs. Doing this will enable us to query the existing knowledge graphs using multiple modalities: images and text. Therefore, in this proposal, we examine and explore two aspects of DB-KG:

-  A framework to create an image-based KG out of existing DBpedia entries;
- Using the graph created to perform tasks like image querying, text + image search, and using relevant input images to add more images to existing articles.

## Instructions to download images from DBpedia

Use the following commond to run `create_dataset.py` and download images to the specified directory.

```python
python article-parser/create_dataset.py --save_dir /path/to/directory/to/save/images/
```

`create_dataset.py` accepts multiple arguments
- `endpoint`: Link to the endpoint
- `graph`: Link to the graph
- `format`: Format to get the output in
- `timeout`: Amount of timeout seconds
- `debug`: If `on` debug mode is on
- `query`: Query string
- `save_dir`: Path to the directory to save the images info

## Instructions to generate embeddings for images

### Generate features for images saved in a directory
Use the following command to run `main.py` and generate features for a group of images in a directory.

```python
python img_models/main.py -p /path/to/image/directory -m resnet50
```

`main.py` accepts two arguments
- `p`: Path to the directory of images for which the features are to be generated
- `m`: Name of the model to load for generating the features. Currently the options are: `resnet18`, `resnet50`, `resnet101`, and `resnet152`.


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


### Get a ranked list of images

Run the following command to get a ranked list of images

```python
python kg_query/main.py --d /path/to/directory/containing/embeddings
```

## Instructions to use the API

Save the embeddings of the dataset to `/scratch/sid/dataset/`. Run the following command

```python
python -m website_demo.wsgi
```

This will open a webpage where you an upload an image of your choice to query the dataset.
