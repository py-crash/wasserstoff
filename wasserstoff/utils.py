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
