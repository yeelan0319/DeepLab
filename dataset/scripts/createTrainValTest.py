from __future__ import print_function

import argparse
import glob
import os

def get_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input-dir', type=str,
                      help='input directory where target images are stored.')
  parser.add_argument("--output-file", type=str,
                      help="output directory where svg will be saved.")
  return parser.parse_args()


def main():
  args = get_arguments()

  image_list = [os.path.basename(x) for x in glob.glob(os.path.join(args.input_dir, 'image', '*.jpg'))]
  label_list = [os.path.basename(x) for x in glob.glob(os.path.join(args.input_dir, 'label', '*.png'))]
  with open(args.output_file, 'w') as outfile:
    for image_file in image_list:
        filename = os.path.splitext(image_file)[0]
        label_file = '{}.png'.format(filename)
        if label_file not in label_list:
          print(label_file)
          continue
        else:
          outfile.write('{} {}\n'.format(os.path.join('', '/image', image_file), os.path.join('', '/label', label_file)))


if __name__ == '__main__':
    main()
