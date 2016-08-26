'''This is an imlementation of cellular automata using numpy arrays rather than lists. Since it sounds like the numba jit compiler can't optimize higher order functions, this is written in an imperative style rather than a functional style.'''

import numpy as np

from itertools import product
from math import log, ceil

class CellularAutomaton:
    def __init__(self, code, k, r):
        '''Create a cellular automaton that implements the ruleset defined by the code for the given radix (k) and radius (r).'''
        self.r = r
        self.lookup = make_lookup_table(code, k, r)

    def apply(self, img):
        '''Apply the cellular automaton rules to the img parameter, which must be a 2d numpy integer array. This modifies the img array in place.'''
        region_index = make_region_index(img.shape[1], self.r)
        for row in range(img.shape[0]-1):
            regions = img[row,region_index]
            col = 0
            for region in regions:
                # Creating a lot of garbage tuples is probably slow
                img[row+1, col] = self.lookup[tuple(region)]
                col += 1
        return img

def make_region_index(width, r):
    '''This is a 2d table of indexes for extracting the region of interest for each input cell. Indexing the input row with this table creates a 2d array of values which can in turn be fed into the lookup table for the code.'''
    table = np.empty((width, 2*r+1), dtype=np.int)
    for n in range(width):
        # note that -2 % 10 == 8
        table[n] = np.arange(n-r, n+r+1) % width
    return table

def make_lookup_table(code, k, r):
    '''The lookup table encodes the rules for the cellular automaton. The input line in the region of the current element is used as an index into the lookup table to find the result value. This is an integer array of 2*r+1 dimensions, each k elements long.'''
    assert code < k**k**(2*r+1), "Code invalid for given k and r."
    table = np.zeros((k,)*(2*r+1), dtype=np.int)
    outcomes = unpack(code, k)
    n = 0
    # This counts from zero in base k for 2*r+1 digits
    for index in product(range(k), repeat=2*r+1):
        table[index] = outcomes[n]
        n += 1
        # If the code is a small number, it may not have very many
        # digits, so we run off the end of outcomes before filling the
        # table. The rest is implicitly zeros.
        if n >= len(outcomes):
            break
    return table

def unpack(n, radix):
    '''This turns a number into a list of its place values, so the digits of a decimal number (radix 10) or the ones and zeros of a binary number (radix 2). The result is a list of coefficients of whole number powers of the radix counting from zero, i.e. the resulting array is in little endian order.'''
    assert isinstance( radix, int ), "Radix must be an integer."
    assert radix > 1, "Radix must be 2 or larger."
    digits = ceil(log(n, radix)) + 1
    result = np.zeros(digits, dtype=np.int)
    i = 0
    while n > 0:
        result[i] = n % radix
        n = n // radix
        i += 1
    return result
    
