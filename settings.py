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

field_data = {
    'property': [{'Cafe': [1, 10000, None]},
                 {'Warehouse': [9, 20000, None]},
                 {'Marine': [17, 30000, None]},
                 {'Factory': [25, 40000, None]},
                 {'Cafe2': [11, 10000, None]},
                 {'Warehouse2': [19, 20000, None]},
                 {'Marine2': [27, 30000, None]},
                 {'Factory2': [35, 40000, None]}],
    'bonuses_and_taxes': [(3, 15000),
                          (12, 15000),
                          (24, -15000),
                          (42, -15000)
                          ],
    'pass_throw': (5, 16, 23, 34, 41)}

