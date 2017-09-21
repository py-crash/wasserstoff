import pytest

from wasserstoff import Environment
from wasserstoff.exceptions import ConfigsNotFound


def test_env(env):
    assert isinstance(env, Environment)
    assert env.configs == []


def test_commit_without_configs(env):
    with pytest.raises(ConfigsNotFound):
        env.commit()


def test_env_patch(env, dev, test):
    env.patch(dev, test)

    assert env.configs
    assert len(env.configs) == 2


def test_env_commit(env, dev, test, default):
    env.patch(dev, test, default)
    env.commit()

    assert env.dev.SSL
    assert not env.test.SSL
    assert not env.default.SSL


def test_config(dev, test):
    dev.create()
    test.create()

    assert dev.SSL
    assert not test.SSL
