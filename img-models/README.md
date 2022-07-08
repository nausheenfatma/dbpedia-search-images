## Generate features for an Image

### Generate features for an images saved at a location
Use the following command to run `main.py` and generate features for an image.

```python
python img-models/main.py -p /path/to/image.jpg -m resnet50
```

`main.py` accepts two arguments
- `p`: Path to the image for which the features are to be generated
- `m`: Name of the model to load for generating the features. Currently the options are: `resnet18`, `resnet50`, `resnet101`, and `resnet152`.
