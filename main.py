# coding: utf8
import settings
import field
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

def check_number_of_players(number_of_players):
    """
    >>> check_number_of_players(float)
    Max number of players - 4, enter the correct number!
    >>> check_number_of_players(5)
    Max number of players - 4, enter the correct number!
    >>> check_number_of_players(1)
    Min number of players is 2
    >>> check_number_of_players(4)
    Ok!
    1
    """

    try:
        number_of_players = int(number_of_players)
        if number_of_players <= 1:
            raise ValueError("Min number of players is 2")
        elif number_of_players > 4:
            raise ValueError('Max number of players - 4, enter the correct number!')
        print('Ok!')
        return 1
    except ValueError as error:
        print error

def get_number_of_players():

    while True:
        number_of_players = raw_input("Enter the number of players: ")
        if check_number_of_players(number_of_players) == 1:
            return int(number_of_players)

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
        settings.initial_cell,
        settings.skip_turn
    ]


def generate_all_players_profiles(names):
    return [create_profile(name) for name in names]


def get_statistics(player, player_throw):
    return ' %s %s %s %s' % (
        player[0],
        player_throw,
        player[2],
        player[1]
    )


def print_statistics(player_throw, player):
    raw_input(get_statistics(player, player_throw))


def update_funds(player, old_player_position):

    if player[2] < old_player_position:
        player[1] += settings.round_bonus

    return player[1]


def hitting_bonuses_and_taxes_fields(player, generated_field):
    if type(generated_field[player[2]]) == int:
        print "Your budget changed by ", generated_field[player[2]]
        player[1] += generated_field[player[2]]
    return player


def passing_fields(player, generated_field, shuffled_profiles):
    if type(generated_field[player[2]]) == str:
        print player[0], " skip next turn"
        player[3] = True
    else:
        hitting_bonuses_and_taxes_fields(player, generated_field)
        buying_property(player, generated_field, shuffled_profiles)
    return player


def buying_choice(key, value, player):
    print key, value[1]
    choice = raw_input("Would you like to buy? Y/N")
    while True:
        if choice in ['Y', 'y']:
            if player[1] >= value[1]:
                value[2] = player[0]
                player[1] -= value[1]
                break
            else:
                print "You don't have enough money"
                break
        elif choice not in ['Y', 'y', 'N', 'n']:
            choice = raw_input("Wrong input, please type 'Y' or 'N'")
        else:
            print "Property skipped"
            break
    return player


def buying_property(player, generated_field, shuffled_profiles):
    if type(generated_field[player[2]]) == dict:
        for key, value in generated_field[player[2]].iteritems():
            if value[2] is None:
                buying_choice(key, value, player)
            elif value[2] not in [player[0], None]:
                player[1] -= value[1] / 10
                print "Player", player[0], " balance decreased by ", value[1] / 10
                for profile in shuffled_profiles:
                    if profile[0] == value[2]:
                        profile[1] += value[1] / 10
                        print "Player", profile[0], " balance increased by ", value[1] / 10
    return player


def main():
    print_greetings()
    generated_field = field.generating_ultimate_field()

    number_of_players = get_number_of_players()

    names = generate_all_players_names(number_of_players)

    players_profiles = generate_all_players_profiles(names)

    shuffled_profiles = shuffle_players_profiles(players_profiles)

    while True:

        for player in shuffled_profiles:

            if player[3] is False:

                player_throw = throw_dices()

                old_player_position = player[2]

                while player_throw[0] == player_throw[1] and player[3] == False:

                    get_new_player_position(player[2], sum(player_throw), player)

                    update_funds(player, old_player_position)

                    print_statistics(player_throw, player)

                    player_throw = throw_dices()

                    old_player_position = player[2]
                    passing_fields(player, generated_field, shuffled_profiles)

                else:
                    if player[3] is False:
                        get_new_player_position(player[2], sum(player_throw), player)

                        update_funds(player, old_player_position)

                        passing_fields(player, generated_field, shuffled_profiles)

                        print_statistics(player_throw, player)
                    else:
                        player[3] = False
            else:
                player[3] = False
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print str(e)
        print()

