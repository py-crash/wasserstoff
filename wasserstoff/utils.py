import json


def read_config(filename):
    """Read JSON file and return content of file.

    :param filename: Name of configuration file.
    :return: Content of configuration file.
    :rtype: dict
    """
    with open(filename + '.json', 'r') as file:
        data = json.load(file)
    return data
