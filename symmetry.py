'''Implement some operations that impose symmetry onto a given numpy array or image.'''

import numpy as np
import skimage

def pinwheel(img):
    # probably only works with RGB images because of the weird axis
    # handling in the tile function. Should probably use concatenate
    # or stack instead of trying to tile it initially.
    out = np.tile(img, (2,2,1))
    assert img.shape[0] == img.shape[1], "pinwheel() only works on square images"
    rows = cols = img.shape[0]
    out[0:rows,cols:] = np.rot90(img, 1)
    out[rows:,cols:]  = np.rot90(img, 2)
    out[rows:,0:cols] = np.rot90(img, 3)
    return out

def twofoldh(img):
    return np.concatenate((img, np.fliplr(img)), 1)

def twofoldv(img):
    return np.concatenate((img, np.flipud(img)), 0)

def fourfold(img):
    return twofoldv(twofoldh(img))

