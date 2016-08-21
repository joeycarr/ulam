#!/usr/bin/env python

import ca
import math
import numpy as np
import os
import random

from skimage.io import imsave

WIDTH=512
# The porcelain palette
# COLORS=[[230,232,233], [134, 149, 185], [93,113,175], [49,67,99]]

# A subset of the tropical palette
COLORS=[[253,254,206], [193,216,33], [21,27,22], [70,165,164]]

def color_lookup(n):
    return COLORS[n]

k = len(COLORS)
r = 1

starter = ca.unpack( random.getrandbits(int(math.log(k**WIDTH,2))), k )
while len(starter) < WIDTH:
    starter.append(0)

for i in range(101):

    data = []
    row = list(starter)
    code = ca.getrandcode(k, r)
    carule = ca.carule(code, k, r)

    for n in range(WIDTH):
        row = carule(row)
        stretched = map( color_lookup, row )
        data.append( list(stretched) )

    img = np.array(data, dtype=np.uint8)

    imsave('color_ca_2/{:03d}.png'.format(i), img)

    with open('color_ca_2/{:03d}.txt'.format(i), 'w') as out:
        out.write("k: {:d}\n".format(k))
        out.write("r: {:d}\n".format(r))
        out.write("code: {:d}\n".format(code))
