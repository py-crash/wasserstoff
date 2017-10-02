from configparser import ConfigParser


def upper_keys(dictionary):
    if isinstance(dictionary, list):
        return [upper_keys(v) for v in dictionary]
    elif isinstance(dictionary, dict):
        return dict((k.upper(), upper_keys(v))
                    for k, v in dictionary.items())
    else:
        return dictionary


def parse_text(data):
    """
    Read keys and values (as strings) from a text file
    Each line should have the format: KEY=VALUE.

    :param data: open file object with the text file.
    :return: Dictionary of keys:values seen in the file.
    :rtype: dict.
    """
    config = {}
    for line in data.readlines():
        if not line.startswith('#'):
            try:
                k, v = line.strip().split('=', 1)
                config[k] = v
            except ValueError:
                continue

    return upper_keys(config)


def parse_ini(filename=None):
    """
    Parse .ini file and convert it to dict.

    :param filename: File name.
    :return:
    """
    if filename:
        parser = ConfigParser()
        parser.read(filename)
        configs = upper_keys({
            s: dict(parser.items(s)) for s in parser.sections()
        })

        return configs
