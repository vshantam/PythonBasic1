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
welcome_greeting = 'Hello! Welcome to Monopoly!'

# initial cell number
"""
 Initial cell of the first circle is also a final cell of the next circles, thus it also should be valued at
 Although it seems to be like a temporary solution, ...
 for now there couldn`t be any O cell or Denis`s get_new_player_position function won`t work"
"""
initial_cell = 44
