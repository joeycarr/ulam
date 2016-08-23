'''Make patterns appropriate for starting cellular automata. A command line interface doesn't make as much sense for this tool and it will probably need to be called from python scripts.'''

import numpy as np

def save(data, filename):
    '''Saves the numpy array in the data argument into the given filename. The npy extension will be added if it isn't already present.'''
    data.save(filename, allow_pickle=False)

def load(filename):
    '''Load and return a numpy array for the starting pattern from the given file.'''
    return np.load(filename, allow_pickle=False)

# --------------------
#  Creation Functions
# --------------------

def random(k=2, width=512):
    '''Generate an array of uniform random noise for the given number of colors, k.'''
    return np.random.randint(0, k, width)

def impulse(width=512):
    '''Generate a 1 in the center of a field of zeros.'''
    result = np.zeros(width, dtype=np.int)
    result[width//2] = 1
    return result

def repeat(pattern, n):
    '''Convert the pattern to an array and repeat each element n times.'''
    result = np.asarray(pattern, dtype=np.int)
    result = np.repeat(result, n)
    return result

def cycle(pattern, n):
    '''Convert the pattern to an array and repeat the pattern n times.'''
    result = np.asarray(pattern, dtype=np.int)
    result = np.concatenate((result,)*n)
    return result

# ------------------------
#  Manipulation Functions
# ------------------------

def mirror(A):
    '''Create a double length version of the array by repeating it forwards then backwards.'''
    return np.append(A, A[-1::-1])

def shuffle(A):
    '''A copy of the elements of the array in a new order.'''
    result = np.copy(A)
    np.random.shuffle(result)
    return result
