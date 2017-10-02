from collections import Mapping
import json

from wasserstoff.parsers import parse_text, parse_ini
from wasserstoff import constants as c


def pull(filename, ext='json'):
    """
    Read file and return contents of file.

    :param filename: Name of configuration file.
    :param ext: format to parse, defaults to json
    :return: Content of configuration file.
    :rtype: dict
    """
    data = None

    if ext == c.JSON:
        with open(filename + '.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

    if ext == c.INI:
        data = parse_ini(filename + '.ini')

    if ext == c.TXT:
        with open(filename, 'r', encoding='utf-8') as file:
            data = parse_text(file)

    return data


def stylize(string):
    """
    Change variable style to upper case with underscores.
    :param string: String.

    :Example:
        UNDERSCORE_VAR
    """

    return str(string) \
        .replace(' ', '_') \
        .replace('-', '_') \
        .replace('.', '_') \
        .upper()


def update_scope(initial, new):
    """
    Recursively update a dictionary.

    :param initial: Dict to update.
    :param new: Dict to update from.
    :return: Updated dict.
    :rtype: dict
    """
    for k, v in new.items():
        if isinstance(v, Mapping):
            r = update_scope(initial.get(k, {}), v)
            initial[k] = r
        else:
            initial[k] = new[k]
    return initial
