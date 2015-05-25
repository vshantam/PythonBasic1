# coding: utf8
import settings
from random import randint, shuffle


def print_greetings():
    print "%s\n%s" % (settings.welcome_greetings, settings.version)


def throw_dice():
    return randint(1, 6)


def throw_dices():
    return [throw_dice() for _ in range(2)]


def get_new_player_position(current_cell, thrown_number, player):
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
    player[2] = (current_cell + thrown_number) % settings.cells_number

    return player[2]


def get_number_of_players():
    """
    >>> get_number_of_players(float)
    ValueError: Number must be exact integer
    >>> get_number_of_players(5)
    ValueError: Max players - 4
    >>> get_number_of_players(1)
    ValueError: Min players - 2
    """
    while True:
        number_of_players = raw_input("Enter the number of players: ")
        try:
            number_of_players = int(number_of_players)
            if number_of_players <= 1:
                raise ValueError("Min number of players is 2")
            elif number_of_players > settings.max_players_number:
                raise ValueError('Max number of players - 4, enter the correct number!')
            print('Ok!')
            return number_of_players
        except ValueError as error:
            print error


def input_player_name(player, names):
    while True:
        name = raw_input('Player_%d name: ' % (player + 1))
        if name not in names:
            return name
        print "Name %s exists" % name


def shuffle_players_profiles(profiles):
    shuffled_list = profiles[:]
    shuffle(shuffled_list)
    return shuffled_list


def generate_all_players_names(number_of_players):
    names_profiles = []
    for player_number in range(number_of_players):
        players_name = input_player_name(
            player_number,
            names_profiles
        )
        names_profiles.append(players_name)
    return names_profiles


def create_profile(name):
    return [
        name,
        settings.initial_funds,
        settings.initial_cell
    ]


def generate_all_players_profiles(names):
    return [create_profile(name) for name in names]


def get_statistics(player, player_throw, old_player_position):
    return ' %s %s %s %s' % (
        player[0],
        player_throw,
        get_new_player_position(player[2], sum(player_throw), player),
        update_funds(player, old_player_position)
    )


def print_statistics(player_throw, player, old_player_position):
    raw_input(get_statistics(player, player_throw, old_player_position))


def update_funds(player, old_player_position):
    if player[2] < old_player_position:
        player[1] += settings.round_bonus
    return player[1]


def generating_empty_field():
    playing_field = [[] for cell in range(settings.cells_number)]
    return playing_field


def generating_bonuses_and_taxes_fields(playing_field, bonus_taxes_cell_data):
    for name, value in bonus_taxes_cell_data.iteritems():
        playing_field[bonus_taxes_cell_data[name][1] - 1] = [  # fixed so that we have no 0 field
                                                               name,
                                                               bonus_taxes_cell_data[name][0]
                                                               ]
    return playing_field


playing_field = generating_empty_field()
bonuses_and_taxes = {'a': [500, 5], 'b': [500, 15], 'c': [500, 25], 'd': [500, 35]}

print generating_bonuses_and_taxes_fields(playing_field, bonuses_and_taxes)
# example of how field generation is proceeded


def generating_property_fields(playing_field, property_cell_data):
    for name, value in property_cell_data.iteritems():
        playing_field[property_cell_data[name][0] - 1] = [
            name,
            property_cell_data[name][1],
            property_cell_data[name][2]
        ]
    return playing_field


property_fields = {
    'Cafe': [1, 100, None],
    'Warehouse': [9, 200, None],
    'Marine': [17, 300, None],
    'Factory': [25, 400, None]
}

print generating_property_fields(playing_field, property_fields)
# example of how field generation is proceeded


def main():
    print_greetings()

    number_of_players = get_number_of_players()

    names = generate_all_players_names(number_of_players)

    players_profiles = generate_all_players_profiles(names)

    shuffled_profiles = shuffle_players_profiles(players_profiles)

    while True:

        for player in shuffled_profiles:

            player_throw = throw_dices()

            old_player_position = player[2]

            while player_throw[0] == player_throw[1]:

                print_statistics(player_throw, player, old_player_position)

                player_throw = throw_dices()

                old_player_position = player[2]
            else:
                print_statistics(player_throw, player, old_player_position)


