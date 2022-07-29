## Query Generated Embeddings

### Load the Embeddings and Query them

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
