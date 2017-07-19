#!/bin/sh

# On Mac
# INKSCAPE_PATH="/Applications/Inkscape.app/Contents/Resources/script"
# On Linux
INKSCAPE_PATH="inkscape"

WD=$(pwd)
SOURCE_PATH="${WD}/wire/xml"
DIST_PATH="${WD}/wire/png"
TMP_PATH="${WD}/wire/tmp"

mkdir "$TMP_PATH"
mkdir "$DIST_PATH"

echo "Generate temporary SVGs..."
echo ""
python scripts/xml2svg.py --input-dir=${SOURCE_PATH} --output-dir=${TMP_PATH}
echo ""
echo "SVG generated!"
echo ""

for svg in ${TMP_PATH}/*.svg; do
  filename=$(basename $svg)
  outputfile=${DIST_PATH}/${filename%.*}.png
  echo "Save ${filename} as png..."
  $INKSCAPE_PATH ${svg} --export-png=${outputfile}
done
echo ""

echo "Removing tmporary svg files..."
rm -r "$TMP_PATH"
echo ""
echo "All done!"
