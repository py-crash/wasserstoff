from wasserstoff import exceptions
from wasserstoff.utils import (
    stylize,
    pull,
)


class Environment(object):
    """Basic environment"""

    configs = []

    def patch(self, *args):
        """Append configurations to environment.
        """

        for arg in args:
            self.configs.append(arg)
        return self

    def commit(self):
        """Set all new config with name env.scope
        """

        if self.configs:
            for cfg in self.configs:
                setattr(self, cfg.scope, cfg)
                cfg.create()
        else:
            raise exceptions.ConfigsNotFound(
                'Environments list is empty',
            )


class Config(object):
    """Environment
    """

    def __init__(self, filename=None, scope=None):
        if scope is not None:
            self.scope = scope
        else:
            self.scope = 'default'

        if filename:
            self.dictionary = pull(filename)

    def create(self):
        """Set key value attributes to the scope of current instance.
        """
        for var, value in self.dictionary.items():
            setattr(self, stylize(var), value)
