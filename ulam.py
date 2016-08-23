#!/usr/bin/env python

import argparse
import ca
import numpy as np
import yaml

from matplotlib.colors import colorConverter
from skimage import img_as_ubyte
from skimage.io import imsave

def ulam(radius=1,
         colors=['#FFFFFF','#000000'],
         width=512,
         height=512,
         code=35 ):
    # Create a lookup table of colors.
    colors = [ list(colorConverter.to_rgb(color)) for color in colors ]
    lut = np.array(colors)
    k = len(colors)
    row = np.random.randint(0, k, width)
    rule = ca.carule(code, k, radius)
    result = np.empty((height, width, 3), dtype=lut.dtype)
    for y in range(height):
        result[y,:,:] = lut[row]
        row = rule(row)
    return result

def parse_args():
    ap = argparse.ArgumentParser(
        description='''Ulam is a toy generative design tool for running cellular automata and creating pretty outputs.''')
    ap.add_argument('outfile',
                    metavar='outfile',
                    type=argparse.FileType('w'),
                    help='A writeable image filename. PNG files work best.'
    )

    ap.add_argument('-r', '--radius',
                    metavar='size',
                    type=int,
                    default=1,
                    help='''The size of the automaton's neighborhood; defaults to 1.'''
    )

    ap.add_argument('-c', '--colors',
                    metavar='color',
                    type=str,
                    default=['#FFFFFF', '#000000'],
                    nargs='+',
                    help='''A list of colors to use in the output. You can use any string color representation recognized by Matplotlib; six digit hex strings are probably the most useful, so be aware that they must be quoted on the command line.'''
    )

    ap.add_argument('-s', '--size',
                    metavar='pixels',
                    type=int,
                    default=[512, 512],
                    nargs=2,
                    help='''The width and height of the output. Defaults to 512 by 512 in no value is specified.'''
    )

    ap.add_argument('-C', '--code',
                    metavar='code',
                    type=int,
                    help='Optionally specify a code in decimal notation, otherwise a random code is generated.')

    return ap.parse_args()    

def main():
    args = parse_args()

    colors = args.colors
    radius = args.radius
    width, height = args.size
    if args.code:
        code = args.code
    else:
        code = ca.getrandcode(len(colors), radius)

    result = ulam(radius, colors, width, height, code)

    result = img_as_ubyte(result)

    imsave(args.outfile.name, result)
    with open('{}.yaml'.format(args.outfile.name), 'w') as out:
        out.write(yaml.dump({
            'colors' : list(colors),
            'radius' : radius,
            'size' : [width, height],
            'code' : code
            }))
    

if __name__ == '__main__':
    main()
