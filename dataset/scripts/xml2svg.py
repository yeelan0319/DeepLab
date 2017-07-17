import argparse
import glob
import os

import xml.etree.ElementTree as ET

from string import Template

SVG_TEMPLATE = Template("""
  <svg width="$width" height="$height">
    <rect x="0" y="0" width="$width" height="$height" style="fill:black" />
    $polygons
  </svg>""")
POLYGON_TEMPLATE = Template("""<polygon points="$points" style="fill:red;stroke:white;stroke-width:1;" />""")
TARGET_OBJECTS = ['wire', 'socketboard']

def get_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("--input-dir", type=str,
                        help="input directory where xmls are stored.")
  parser.add_argument("--output-dir", type=str,
                        help="output directory where svg will be saved.")
  return parser.parse_args()

def LoadXML(path):
  return ET.parse(path)

def GenerateSVG(xml_tree):
  root = xml_tree.getroot()
  width_str = root.find('imagesize').find('ncols').text
  height_str = root.find('imagesize').find('nrows').text

  polygons = []
  for obj in root.findall('object'):
    if obj.find('name').text not in TARGET_OBJECTS or obj.find('polygon') is None:
      continue
    polygon = obj.find('polygon')
    points = []
    for pt in polygon.findall('pt'):
      points.append('{},{}'.format(pt.find('x').text, pt.find('y').text))
    polygons.append(POLYGON_TEMPLATE.substitute(points=' '.join(points)))
  polygons_str = ''.join(polygons)

  return SVG_TEMPLATE.substitute(
    width=width_str, height=height_str, polygons=polygons_str)

def main():
  args = get_arguments()

  xml_list = glob.glob(os.path.join(args.input_dir, '*.xml'))
  for xml_path in xml_list:
    print("Converting {}...".format(xml_path))
    svg = GenerateSVG(LoadXML(xml_path))
    output_file = os.path.join(args.output_dir,
      '{}.svg'.format(os.path.splitext(os.path.basename(xml_path))[0]))
    with open(output_file, 'w') as file_object:
      file_object.write(svg)


if __name__ == '__main__':
    main()