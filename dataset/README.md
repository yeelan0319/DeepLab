# Dataset


## scripts

Script in the dataset folder is used for creating custom segementation data.

### Dependencies
- Inkscape command line tool

### Alternatives
The scripts was created to use Inkscape is mainly because rsvg package on OSX is
outdated and cannot be used. If you are using linux or running the script using
python3, consider using cairo + rsvg. See details
[here](https://stackoverflow.com/questions/6589358/convert-svg-to-png-in-python)

### How to use
1. To creat custom segmentation data, first label images via MIT online tool -
[LabelMe](http://labelme2.csail.mit.edu/) and download the xml data.

2. Open `createAnnotatedData.sh` and change `SOURCE_PATH` as well as other paths.
After that, run `./createAnnotatedData.sh` and it will create png ready for
segementation training in `DIST_PATH` folder.


## wire
Give some elaboration about:
- What the dataset is about
- Where to download the dataset
