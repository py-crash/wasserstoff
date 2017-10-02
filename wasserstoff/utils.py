from collections import Mapping
import json

from wasserstoff.parsers import parse_text


def pull(filename, fmt='json'):
    """
    Read file and return contents of file.

    :param filename: Name of configuration file.
    :param fmt: format to parse, defaults to json
    :return: Content of configuration file.
    :rtype: dict
    """
    data = None

    if fmt == 'json':
        with open(filename + '.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

    if fmt == 'text':
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
