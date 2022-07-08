
import os
import argparse

from generate_features import ImgFeatures

parser = argparse.ArgumentParser()
parser.add_argument(
    '-p',
    required=True,
    help='Path to the image to load',
)
parser.add_argument(
    '-m',
    default='resnet50',
    help='Name of the model to load for extracting the features',
)
args = parser.parse_args()

img_feats = ImgFeatures(img_path=args.p, model_name=args.m)
feats = img_feats.get_features()
print(f'Features of shape {feats.shape} generated for {os.path.basename(args.p)}!')
