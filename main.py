# coding: utf8
import settings
from random import randint


hdef print_greeting():
    print settings.welcome_greeting


def input_player_name():
    return raw_input('Player name: ')


def throw_dice():
    return randint(1, 6)


def get_new_player_position(current_cell, thrown_number):
    """
    I think we should start counting the cell with 1 rather than with 0, or change the max number of cells to 43.
    This test brings the position after the initial throw.
    >>> get_new_player_position(0, 2)
    2
    This test estimates the position after crossing the start field.
    >>> get_new_player_position(44, 1)
    1

    """
    return (current_cell + thrown_number) % settings.cells_number


print_greeting()


