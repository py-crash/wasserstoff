from os.path import (
    abspath,
    dirname,
    join,
)

import pytest

from wasserstoff import Config, Environment

PATH = abspath(join(dirname(__file__), 'data'))


@pytest.fixture
def env():
    return Environment()


@pytest.fixture
def dev():
    return Config(
        filename=PATH + '/dev',
        scope='dev',
    )


@pytest.fixture
def test():
    return Config(
        filename=PATH + '/test',
        scope='test',
    )


@pytest.fixture
def default():
    return Config(filename=PATH + '/default')


@pytest.fixture
def text():
    return Config(
        filename=PATH + '/text',
        scope='test',
        fmt='text',
    )
