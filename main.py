# coding: utf8
import settings
from random import randint
from random import shuffle


def print_greeting():
    print settings.welcome_greeting


def throw_dice():
    return randint(1, 6)


def get_new_player_position(current_cell, thrown_number):
    """
    Initial cell of the first circle is also a final cell of the next circles,
    thus it also should be valued at 44.
    Although it seems to be like a temporary solution,
    for now there could not be any O cell or get_new_player_position function won`t work.

    This test brings the position after the initial throw.
    >>> get_new_player_position(settings.initial_cell, 2)
    2

    This test estimates the position after finishing
    the first circle and hitting the start field.
    >>> get_new_player_position(settings.cells_number, 1)
    1

    This test estimates the position after crossing the start field.
    >>> get_new_player_position(settings.cells_number, 5)
    5

    """
    return (current_cell + thrown_number) % settings.cells_number


print_greeting()


# Issue #7
# fixed the identifier instead of function/ fixed the import
# deleted the additional constant "constant"

def numb_of_players():
    while True:
        m = raw_input("Enter the number of players: ")
        try:
            m = int(m)
        except ValueError:
            print "Value should be the number!"
            continue
        if m <= 1:
            print "Min number of players is 2"
        elif m <= settings.max_players_number:
            print('Ok!')
            return m
        else:
            print('Max number of players - 4, enter the correct number!')


def input_player_name():
    return raw_input('Player name: ')


# builds the profile of a given player
def player_profile():  # builds the list of players
    return [input_player_name(), settings.initial_funds, settings.initial_cell]


def generate_profiles_list():
    while True:
        try:
            numb_of_players = int(raw_input("Enter the number of players: "))
            profiles_list = []         #TODO: make it dictionary not list
            if numb_of_players <= 1:
                print "Min number of players is 2"
            elif numb_of_players <= settings.max_players_number:
                for player in range(numb_of_players):
                    profiles_list.append(player_profile())
                return profiles_list
            else:
                print('Max number of players - 4, enter the correct number!')
        except ValueError:
            print "Value should be the number!"


def shuffle_players_profile():
    shuffled_list = generate_profiles_list()[:]
    shuffle(shuffled_list)
    return shuffled_list