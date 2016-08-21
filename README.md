# Ulam

The goal of this project is to create a small command line tool that will be convenient to work with.


```
usage: ulam.py [-h] [-r size] [-c color [color ...]] [-s pixels pixels]
               [-C code]
               outfile

Ulam is a toy generative design tool for running cellular automata and
creating pretty outputs.

positional arguments:
  outfile               A writeable image filename. PNG files work best.

optional arguments:
  -h, --help            show this help message and exit
  -r size, --radius size
                        The size of the automaton's neighborhood; defaults to
                        1.
  -c color [color ...], --colors color [color ...]
                        A list of colors to use in the output. You can use any
                        string color representation recognized by Matplotlib;
                        six digit hex strings are probably the most useful, so
                        be aware that they must be quoted on the command line.
  -s pixels pixels, --size pixels pixels
                        The width and height of the output. Defaults to 512 by
                        512 in no value is specified.
  -C code, --code code  Optionally specify a code in decimal notation,
                        otherwise a random code is generated.
```

## Issues

Python's argparse implementation tries to interpret `outfile` as a color if it comes immediately after the `--colors` option. Either specify `outfile` before `--colors` or place another option between `--colors` and `outfile`.

## Future development

Right now the starters are completely random. I'd like to make it easier to create/specify a more structured starter.

