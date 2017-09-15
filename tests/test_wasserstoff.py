from wasserstoff import Environment


def test_env(env):
    assert isinstance(env, Environment)
    assert env.configs == []


def test_env_patch(env, dev, test):
    env.patch(dev, test)

    assert env.configs
    assert len(env.configs) == 2


def test_env_committed(env, dev, test):
    env.patch(dev, test)
    env.commit()

    assert env.dev.SSL
    assert not env.test.SSL


def test_config(dev, test):
    dev.create()
    test.create()

    assert dev.SSL
    assert not test.SSL
