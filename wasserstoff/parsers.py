

def textparse(data):
    """Read keys and values(as strings) from a text file
    Each line should have the format:
        KEY=VALUE

    :param data: open file object with the text file
    :return: Dictionary of keys:values seen in the file
    :rtype: dict
    """
    config = {}
    for line in data.readlines():
        try:
            k, v = line.strip().split('=', 1)
            config[k] = v
        except ValueError:
            continue
    return config
