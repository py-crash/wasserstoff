from wasserstoff.utils import read_config


class Config(object):
    """Main class"""

    def __init__(self, filename=None):
        if filename:
            self._config = read_config(filename)

    @staticmethod
    def const_style(var):
        var = str(var).replace(' ', '_').replace('-', '_')
        return var.upper()

    def add(self, scope, file):
        return self

    def setup(self):
        """Create consts in scope of current object.
        """
        pass
