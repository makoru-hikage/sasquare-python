#!/usr/bin/python
import os, sys, argparse
from functools import partial
from math import log10

from single_array_square import selections
from single_array_square import outputs

print_usage = """
sasquare base [selection_type] [selection_value]

Print a perfect square with a BASE of a chosen integer.
Selects all the cells when options aren't specified.
Some `selection_type`s need `selection_value`s, some don't

selection_types:
    a, ascending-slope INDEX          select all cells in an ascending slope
    A, ascending-opposite INDEX       select a cell and its opposite along an ascending slant
    c, column INDEX                   select all cells within a column by column INDEX
    C, vertical-opposite INDEX        select a cell and its opposite along a column
    d, descending-slope INDEX         select all cells in a descending slope
    D, descending-opposite INDEX      select a cell and its opposite along an descending slant
    j, corner [INDEX]                 select a particular corner, no INDEX selects all
                                            tl for the top-left corner
                                            tr for the top-right corner
                                            bl for the bottom-left corner
                                            br for the bottom-right corner
    m, center                         select the central part of a square
    r, row INDEX                      select all cells within a row by row INDEX
    R, horizontal-opposite INDEX      select a cell and its opposite along a row
    x, cross                          select the longest two slopes
    """

def print_help():
    print(print_usage)

def run_selection(base, selection_type, selection_value = None):
    if selection_type in ('a', 'ascending-slope'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_ascending_slope(base, index)

    elif selection_type in ('A', 'ascending-opposite'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_ascending_opposites(base, index)

    elif selection_type in ('c', 'column'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_column(base, index)

    elif selection_type in ('C', 'vertical-opposite'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_vertical_opposites(base, index)

    elif selection_type in ('d', 'descending-slope'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_descending_slope(base, index)

    elif selection_type in ('D', 'descending-opposite'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_descending_opposites(base, index)

    elif selection_type in ('j', 'corners'):
        if selection_value is None or len(selection_value) < 1:
            outputs.print_all_corners(base)
            sys.exit(0)
        index = selection_value[0]
        outputs.print_one_corner(base, index)

    elif selection_type in ('m', 'center'):
        outputs.print_center(base)

    elif selection_type in ('r', 'row'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_row(base, index)

    elif selection_type in ('R', 'horizontal-opposite'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_horizontal_opposites(base, index)

def main():
    parser = argparse.ArgumentParser(add_help=False, usage=print_usage)

    parser.add_argument("base", type=int)
    parser.add_argument("selection_type", nargs='?')
    parser.add_argument("selection_value", nargs='*')
    args = parser.parse_args()

    #Print a newline
    print()

    if args.selection_type is None:
        ## Print filled square by default
        outputs.print_square_to_stdout(base, range(1, base**2 + 1))
    else:
        run_selection(
            args.base,
            args.selection_type,
            args.selection_value
        )


if __name__ == "__main__":
    main()