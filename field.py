# coding: utf8
import settings


def generating_empty_field():
    empty_field = [[] for _ in range(settings.cells_number)]
    return empty_field


def generating_bonuses_and_taxes_fields(playing_field, field_data):
    for _ in field_data['bonuses_and_taxes']:
        playing_field[_[0]] = _[1]
    return playing_field


def generating_property_fields(playing_field, field_data):
    for _ in field_data['property']:
        for key, value in _.iteritems():
            playing_field[_[key][0]] = _
    return playing_field


def generating_passing_fields(playing_field, field_data):
    for _ in field_data['pass_throw']:
        playing_field[_] = 'pass_throw'
    return playing_field


def generating_ultimate_field():
    field = generating_empty_field()
    generating_property_fields(field, settings.field_data)
    generating_bonuses_and_taxes_fields(field, settings.field_data)
    generating_passing_fields(field, settings.field_data)
    return field
