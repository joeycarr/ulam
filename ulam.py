#!/usr/bin/env python

import argparse
import starter as st
import numpy as np
import yaml

from ca import CellularAutomaton, getrandcode
from matplotlib.colors import colorConverter
from skimage import img_as_ubyte
from skimage.io import imsave, imread

def ulam(radius=1,
         colors=['#FFFFFF','#000000'],
         width=512,
         height=512,
         code=30,
         starter=None ):
    # Create a lookup table of colors.
    colors = [ list(colorConverter.to_rgb(color)) for color in colors ]
    lut = np.array(colors)
    k = len(colors)
    if starter is None:
        starter = st.random(k, width)
    else:
        width = len(row)

    img = np.empty((height, width), dtype=np.int)
    img[0] = starter

    automaton = CellularAutomaton(code, k, radius)
    automaton.apply(img)
    result = lut[img]
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
                    help='''The width and height of the output. Defaults to 512 by 512 in no value is specified. If a starter line is provided, then the width of that line will be used and only the height portion of this argument will matter.'''
    )

    ap.add_argument('-C', '--code',
                    metavar='code',
                    type=int,
                    help='Optionally specify a code in decimal notation, otherwise a random code is generated.')

    ap.add_argument('-S', '--starter',
                    metavar='filename',
                    type=argparse.FileType('r'),
                    help='''Optionally specify an image file that contains the line of unsigned integers fed to the cellular automaton. If no starter line is provided, then uniform random integers are used. If a starter file is specified, the width portion of the --size argument will be ignored.''')

    return ap.parse_args()    

def main():
    args = parse_args()

    colors = args.colors
    radius = args.radius
    width, height = args.size
    if args.code:
        code = args.code
    else:
        code = getrandcode(len(colors), radius)

    starter = None
    if args.starter:
        starter = st.load(args.starter.name)
        assert starter.max() < len(colors), 'The starter has more colors than are supplied to the --color argument.'
        width = len(starter)

    result = ulam(radius, colors, width, height, code, starter)

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
