from collections import Mapping
import json


def pull(filename):
    """Read JSON file and return content of file.

    :param filename: Name of configuration file.
    :return: Content of configuration file.
    :rtype: dict
    """
    with open(filename + '.json', 'r') as file:
        data = json.load(file)
    return data


def stylize(var):
    """Change variable style to upper case with underscores"""
    return str(var) \
        .replace(' ', '_') \
        .replace('-', '_') \
        .upper()


def update_scope(initial, new):
    """Recursively update a dictionary.

    :param initial: Dict to update.
    :param new: Dict to update from.
    :return: Updated dict.
    """
    for k, v in new.items():
        if isinstance(v, Mapping):
            r = update_scope(initial.get(k, {}), v)
            initial[k] = r
        else:
            initial[k] = new[k]
    return initial
