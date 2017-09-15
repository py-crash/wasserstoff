from wasserstoff.utils import read_config


class Environment(object):
    """Main class"""

    def patch(self, *args):
        for obj in args:
            setattr(self, obj.NAME, obj)

        return self

    def commit(self):
        pass


class Config(object):
    """Environment
    """

    NAME = ''

    def __init__(self, filename=None, scope=None):
        if filename:
            self.NAME = scope
            self._config = read_config(filename)
