# coding: utf8
"""
This module include all settings for
Monopoly project.
Each setting (variable) should be followed
with short and proper commentary
"""

# number of cells on the playing map
cells_number = 44

# welcome greeting, shown at the start of game
welcome_greetings = 'Hello! Welcome to Monopoly!'

version = 'v. 1.1'

# initial cell number
"""
 Initial cell of the first circle is also a final cell of the next circles,
 thus it also should be valued at 44.
 Although it seems to be like a temporary solution,
 for now there couldn`t be any O cell or get_new_player_position function won`t work.
"""
initial_cell = 0

# initial amount of money
initial_funds = 200000
# bonus for completing one circle
round_bonus = 50000

max_players_number = 4

property_fields = {
    'Cafe': [1, 100, None],
    'Warehouse': [9, 200, None],
    'Marine': [17, 300, None],
    'Factory': [25, 400, None]
}

bonuses_and_taxes = {'a': [5, 500], 'b': [15, 500], 'c': [25, 500], 'd': [35, 500]}