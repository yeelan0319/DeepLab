from __future__ import print_function

import argparse
import glob
import os

import numpy as np

from PIL import Image


def get_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input-dir', type=str,
                      help='input directory where target images are stored.')
  return parser.parse_args()


def main():
  args = get_arguments()

  image_list = glob.glob(os.path.join(args.input_dir, '*.jpg'))
  average_matrix = None
  for image_file in image_list:
    with Image.open(image_file) as im:
      img_avg = np.array(im).mean(axis=(0, 1))
      average_matrix = (
        np.vstack([average_matrix, img_avg]) if average_matrix is not None
        else np.array(img_avg))

  print(np.mean(average_matrix, axis=0))


if __name__ == '__main__':
    main()
