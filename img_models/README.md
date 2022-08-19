## Generate features for a Dataset

### Generate features for an images saved at a location
Use the following command to run `main.py` and generate features for a group of images in a directory.

```python
python img-models/main.py -p /path/to/image/directory -m resnet50
```

`main.py` accepts two arguments
- `p`: Path to the directory of images for which the features are to be generated
- `m`: Name of the model to load for generating the features. Currently the options are: `resnet18`, `resnet50`, `resnet101`, and `resnet152`.
