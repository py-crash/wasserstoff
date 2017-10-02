from collections import Mapping
from wasserstoff.parsers import textparse
import json


def pull(filename, fmt='json'):
    """Read file and return contents of file.

    :param filename: Name of configuration file.
    :param format: format to parse, defaults to json
    :return: Content of configuration file.
    :rtype: dict
    """
    if fmt == 'json':
        with open(filename + '.json', 'r') as file:
            data = json.load(file)
    if fmt == 'text':
        with open(filename, 'r') as file:
            data = textparse(file)
    return data


def stylize(var):
    """Change variable style to upper case with underscores"""

    return str(var) \
        .replace(' ', '_') \
        .replace('-', '_') \
        .replace('.', '_') \
        .upper()


def update_scope(initial, new):
    """Recursively update a dictionary.

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
