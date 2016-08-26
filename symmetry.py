'''Implement some operations that impose symmetry onto a given numpy array or image.'''

import numpy as np
import skimage

def tile(img, rows=2, cols=2):
    '''Numpy's built-in tile pads extra dimensions on the left, so it fails to treat RGB and grayscale images uniformly. This version of tile assumes only two dimensions and leaves any higher dimensions as they are.'''
    tmp = np.concatenate((img,)*rows, axis=0)
    return np.concatenate((tmp,)*cols, axis=1)

def tilefill(img, width=512, height=512):
    '''Tile the given image and trim it to the given dimensions.'''
    rows = height // img.shape[0] + 1
    cols = width // img.shape[1] + 1
    tmp = tile(img, rows, cols)
    return tmp[:height,:width]

def pinwheel(img):
    '''Impose pinwheel-like symmetry by duplicating and rotating the image by quarter turns. Only works for square input images.'''
    assert img.shape[0] == img.shape[1], 'pinwheel() only works on square images.'
    return np.vstack([np.hstack([img,              np.rot90(img, 1)]),
                      np.hstack([np.rot90(img, 3), np.rot90(img, 2)])])

def twofoldh(img):
    '''Mirror across the y axis.'''
    return np.concatenate((img, np.fliplr(img)), axis=1)

def twofoldv(img):
    '''Mirror across the x axis.'''
    return np.concatenate((img, np.flipud(img)), axis=0)

def fourfold(img):
    '''Mirror across both the x and y axes.'''
    return twofoldv(twofoldh(img))

def proph(img):
    '''Mirror across the y axis and flip the mirrored image vertically.'''
    return np.concatenate((img, np.flipud(img)), axis=1)

def propv(img):
    '''Mirror across the x axis and flip the mirrored image horizontally.'''
    return np.concatenate((img, np.fliplr(img)), axis=0)

def glideh(A, B):
    '''Impose horizontal glide symmetry by concatenating the images vertical while rolling the second input by 50% its height. The output will tile smoothly. Inputs must be the same size and shape.'''
    roll = B.shape[0] // 2
    tmp = np.roll(np.flipud(B), roll, axis=1)
    return np.concatenate((A, tmp), axis=0)


def glidev(A, B):
    '''Impose vertical glide symmetry by concatenating the images horizontally while flipping and rolling the second input by 50% its width. The output will tile smoothly. Inputs must be the same size and shape.'''
    roll = B.shape[1] // 2
    tmp = np.roll(np.fliplr(B), roll, axis=0)
    return np.concatenate((A, tmp), axis=1)
