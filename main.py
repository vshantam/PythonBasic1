# coding: utf8
import settings
from random import randint
from random import shuffle


def print_greeting():  # fixed the function
    print settings.welcome_greeting
    print settings.version


def throw_dice():  # added one more dice
    x = randint(1, 6)
    y = randint(1, 6)
    return [x, y] # returning list, because we need to check if player should do second throw.


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


# Issue #7
# fixed the identifier instead of function/ fixed the import
# deleted the additional constant "constant"

def numb_of_players():
    """
    >>>numb_of_players(float)
    ValueError: Number must be exact integer
    >>>numb_of_players(m>4)
    ValueError: Max players - 4
    >>>numb_of_players(m<2)
    ValueError: Min players - 2


    """
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


#Modified issue 9
def input_player_name():
    return raw_input('Player_' + str(player) + ' name: ')


# builds the profile of a given player
def player_profile():  # builds the list of players
    return [input_player_name(), settings.initial_funds, settings.initial_cell]


def player_number():
    while True:
        try:
            number_of_players = int(raw_input("Enter the number of players: "))
            if number_of_players <= 1:
                print "Min number of players is 2"
            elif number_of_players <= settings.max_players_number:
                return number_of_players
            else:
                print('Max number of players - 4, enter the correct number!')
        except ValueError:
            print "Value should be the number!"


def generate_profiles_list():
    profiles_list = []  # TODO: make it dictionary not list
    global player
    for player in range(1, player_number() + 1):
        while True:
            current_profile = player_profile()
            if current_profile not in profiles_list:
                profiles_list.append(current_profile)
                break
            else:
                print "This name is already held, please try another name"
    return profiles_list


def shuffle_players_profile():
    shuffled_list = generate_profiles_list()[:]
    shuffle(shuffled_list)
    return shuffled_list


def main():
    print_greeting()
    shuffled_list = shuffle_players_profile()
    while True:
        for player in shuffled_list:
            raw_input(player[0] + '>>>')


main()
