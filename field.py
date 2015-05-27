# coding: utf8
import settings
# import test


def generating_empty_field():
    empty_field = [[] for _ in range(settings.cells_number)]
    return empty_field


def generating_bonuses_and_taxes_fields(playing_field, bonus_taxes_cell_data):
    for name, value in bonus_taxes_cell_data.iteritems():
        playing_field[bonus_taxes_cell_data[name][0] - 1] = [  # fixed so that we have no 0 field
                                                               name,
                                                               bonus_taxes_cell_data[name][1]
                                                               ]
    return playing_field


def generating_property_fields(playing_field, property_cell_data):
    for name, value in property_cell_data.iteritems():
        playing_field[property_cell_data[name][0] - 1] = [
            name,
            0,
            property_cell_data[name][1],
            property_cell_data[name][2]
        ]
    return playing_field


def generating_ultimate_field():
    empty_field = generating_empty_field()
    generating_property_fields(empty_field, settings.property_fields)
    generating_bonuses_and_taxes_fields(empty_field, settings.bonuses_and_taxes)
    return empty_field


    # example of how field generation is proceeded