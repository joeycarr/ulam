import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from itertools import permutations as perms
from matplotlib.colors import colorConverter

def colorize(A, colors=['#000000', '#ffffff'], dtype=np.float):
    '''Converts a 2D integer array, A, into a 3 channel RGB ndimage using the colors argument as a lookup table.'''
    colors = [ list(colorConverter.to_rgb(color)) for color in colors ]
    lut = np.array(colors, dtype=dtype)
    return lut[A]

# TODO: add a function to find all the unique colors in an input image.

class ColorTable:

    def __init__(self, path='~/.ulam/colors.csv'):
        self.table = pd.read_csv(path)
        # TODO: initialize the table with some derived attributes, like RGB values, HSV values, etc.

    def schemes(self):
        '''Get a list of all the schemes in the color table.'''
        return self.table['scheme'].unique()

    def permutations(self, scheme, count=2):
        '''A generator that yields all the possible permutations of length `count` for all the colors in a given scheme.'''
        colors = self.table[self.table.scheme == scheme]['hex']
        yield from perms(colors, count)

    def all_permutations(self, count=2):
        '''A generator that yields all the permutations for every color scheme.'''
        for scheme in self.schemes():
            yield from self.permutations(scheme, count)

    # TODO: add a namecolor method that looks up a name for a given color

