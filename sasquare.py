#!/usr/bin/python
import os, sys, argparse
from functools import partial
from math import log10

from single_array_square import selections
from single_array_square import parts
from single_array_square import outputs
from single_array_square import helpers

print_usage = """
sasquare base [-h] [selection_type] [selection_value]

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
    elif selection_type in ('c', 'column'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_column(base, index)
    elif selection_type in ('d', 'descending-slope'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_descending_slope(base, index)
    elif selection_type in ('j', 'corners'):
        if selection_value is None or len(selection_value) < 1:
            outputs.print_all_corners(base)
            sys.exit(0)
        index = selection_value[0]
        corners = {
            "tr": selections.select_topright_corner(base),
            "tl": selections.select_topleft_corner(base),
            "br": selections.select_bottomright_corner(base),
            "bl": selections.select_bottomleft_corner(base)
        }
        if index not in corners.keys():
            print_help()
            sys.exit()
        outputs.print_square_to_stdout(base, (corners[index],))
    elif selection_type in ('m', 'center'):
        outputs.print_center(base)
    elif selection_type in ('r', 'row'):
        if selection_value is None:
            print_help()
            sys.exit()
        index = int(selection_value[0])
        outputs.print_row(base, index)




def main():
    parser = argparse.ArgumentParser(add_help=False, usage=print_usage)

    parser.add_argument("base", help="the integer multiplied by itself", type=int)
    parser.add_argument("selection_type", nargs='?')
    parser.add_argument("selection_value", nargs='*')
    parser.add_argument("-h", action="store_false")
    args = parser.parse_args()

    base = args.base
    selection_type = args.selection_type
    selection_value = args.selection_value

    #Print a newline
    print()

    if args.h is not None:
        print_help()
        sys.exit(0)

    if selection_type is None:
        outputs.print_square_to_stdout(base, range(1, base**2 + 1))
    else:
        run_selection(base, selection_type, selection_value)


if __name__ == "__main__":
    main()