"""Custom action classes for argparse."""

from __future__ import print_function

import argparse
import numpy as np

class ListToNparray(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    setattr(namespace, self.dest, np.array(values, dtype=np.float32))
