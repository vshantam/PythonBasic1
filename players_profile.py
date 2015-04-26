# coding: utf8
import settings
import main


def input_player_name():
    return raw_input('Player name: ')


# builds the profile of a given player
def player_profile():  # builds the list of players
    return [input_player_name(), settings.initial_funds, settings.initial_cell]


# builds the list of profiles of all players
def all_players_profile():
    l = []
    x = main.numb_of_players()
    n = 0
    while n < x:
        n += 1
        l.append(player_profile())
    return l

