'''Celular Automata.

The main entry to this module is the carule function. The rest of the functions are for internal use. The signature of the function produced by carule is [int] -> [int], i.e. it takes an input array of integers and produces an array of integers of equal length. The values of the input cells may range from zero to k-1.

'''

from math import ceil, log
import random

def carule(code, k, r):
    '''Creates a function that runs a cellular automaton on an input list of integers.'''
    looker = lookup(code, k, r)
    def rule(l):
        neighborhoods = ( neighborhood(l, n, r) for n in range(len(l)) )
        return [ looker(pack(x, k)) for x in neighborhoods ]
    return rule

def getrandcode(k, r):
    '''Given a depth, k, and radius, r, generate a random code number. These get very big, very quickly, with increasing values of k.'''
    maximum = k ** (k ** (2*r + 1))
    bits = int(ceil(log(maximum, 2)))
    code = maximum + 1
    while code > maximum:
        code = random.getrandbits(bits)
    return code

def neighborhood(l, n, r):
    '''Returns a list of elements from the list l in the neighborhood of n. The returned list is 2r+1 elements long. The input list, l, is treated as a circular list, so the first element is the successor of the last.'''
    ll = len(l)
    for i in range( n-r, n+r+1 ):
        yield l[ i%ll ]

def lookup(code, k, r):
    '''Produces a lookup function based on the given code number for an automaton of depth k and radius r.'''
    lookup = unpack(code, k)
    limit = k ** (2*r + 1)
    def looker(i):
        if i > limit:
            return None
        if i < len(lookup):
            return lookup[i]
        else:
            return 0
    return looker


def pack(l, k):
    '''Given a list of numbers and a base, k, pack them into a single integer as the sum of l[n]*k**n'''
    n = 0
    s = 0
    for a in l:
        # a is the same as l[n]
        s += a * k**n
        n += 1
    return s

def unpack(n, radix):
    '''Unpack a number into a list of coefficients of integer powers of the radix. The radix must be specified as an integer, or the results may be unpredictable.'''
    result = []
    if radix < 2:
        return None # prevent an infinite recursion
    while n > 0:
        result.append(n % radix)
        n = n // radix # use floor division for Python 3
    return result
