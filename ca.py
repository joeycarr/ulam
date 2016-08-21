'''Celular Automata.

This package implements one dimensional cellular automata by creating a lookup table of potential output values. The implementation is based on numpy arrays.

'''

import numpy as np
import random

from math import ceil, log

def carule(code, k, r):
    '''Creates a function that runs a cellular automaton on an input list of integers.'''
    table = make_table(code, k, r)
    def rule(l):
        neighborhoods = ( neighborhood(l, n, r) for n in range(len(l)) )
        return [ lookup(table, pack(x, k)) for x in neighborhoods ]
    return rule

def getrandcode(k, r):
    '''Given a depth, k, and radius, r, generate a random code number. These get very big, very quickly, with increasing values of k.'''
    maximum = k ** (k ** (2*r + 1))
    bits = ceil(log(maximum, 2))
    code = maximum + 1
    while code > maximum:
        code = random.getrandbits(bits)
    return code

def neighborhood(array, n, r):
    '''Returns a copy of the array elements that lay on either side of n. The returned list is 2r+1 elements long. The input array is treated as a circular, so the first element is the successor of the last.'''
    index = np.arange(n-r, n+r+1) % len(array)
    return array[index]

def make_table(code, k, r):
    table = unpack(code, k)
    return {'table': table,
            'k': k,
            'r': r,
            'limit' = k ** (2*r + 1)
            }

def lookup(table, n):
    '''Find the resulting value for the given input neighborhood'''
    if n > table['limit']:
        return None
    if n < len(table['table']):
        return table['table'][n]
    else:
        return 0

def pack(seq, radix):
    '''Given a sequence of numbers and a base, radix, pack them into a single integer as the sum of seq[i]*radix**i'''
    i = 0
    result = 0
    for a in seq:
        # a is the same as seq[i]
        result += a * radix**i
        i += 1
    return result

def unpack(n, radix):
    '''Unpack a number into a Numpy array of coefficients of integer powers of the radix. The radix must be specified as an integer, or the results may be unpredictable.'''
    places = ceil(log(n+1, radix))
    result = np.zeros(places, dtype=int)
    if radix < 2:
        return None # prevent an infinite recursion
    i = 0
    while n > 0:
        result[i] = n % radix
        n = n // radix # use floor division for Python 3
        i+=1
    return result
