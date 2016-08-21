# Ulam

Ulam is a toy generative design tool for running cellular automata and creating pretty outputs. The goal is to create a small command line tool that will be convenient to work with.

## Parameters:

 - *file* - The output image filename, which should be a PNG. Ulam will also write a similarly YAML document containing the parameters used to generate the output.

## Options:

  - *r* - The size of the CA neighborhood; default 1.
  - *colors* - Specify a color set; implicitly sets the `k` parameter.
  - *height* - The height measurement in pixels. Defaults to 512.
  - *width* - The width measurement in pixels. Defaults to 512
  - *code* - Optionally specify a code in decimal notation, otherwise a random code is generated.

## Futures

  - starter - some way of selecting starter seeds, such as single impulses random fields, or regular patterns. This may be a subcommand that generates starters as PNG or YAML files.
