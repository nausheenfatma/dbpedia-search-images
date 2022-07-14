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
