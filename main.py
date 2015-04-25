# coding: utf8
from literals import welcome_greeting  # importing all literals, however <from literals import *> might be better
from literals import cells_number
from literals import current_cell
from random import randint

print welcome_greeting  # printing greeting

a = raw_input('Player name: ')
def name(a):
    return a
print a


# for issue 2 #
def throw_dice():
    return randint(1, 6)
print throw_dice()

thrown_number = throw_dice()


# for issue 4 #
def moving(current_cell, thrown_number):
    """
    I think we should start counting the cell with 1 rather than with 0, or change the max number of cells to 43.
    This test brings the position after the initial throw.
    >>> moving(0;2)
    2
    This test estimates the position after crossing the start field.
    >>> moving(43;4)
    2
    """
    current_cell += thrown_number  # updates current position
    if current_cell > cells_number:
        current_cell -= cells_number  # if new position is over cells_number updates it to difference
    return current_cell  # between them, and return new position