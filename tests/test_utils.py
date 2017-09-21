import pytest

from wasserstoff.utils import pull, stylize, update_scope
from .conftest import PATH


def test_pull():
    result = pull(PATH + '/dev')
    assert isinstance(result, dict)
    assert result


@pytest.mark.parametrize(
    'var, stylized', [
        ('port', 'PORT'),
        ('my server', 'MY_SERVER'),
        ('N N N', 'N_N_N'),
        ('N.N.N', 'N_N_N'),
    ],
)
def test_stylize(var, stylized):
    result = stylize(var)

    assert result is not None
    assert result == stylized


def test_update_scope():
    first = {'configs': {'dev': ['port']}}
    second = {'configs': {'test': ['server']}}

    result = update_scope(first, second)

    assert 'test' in result['configs']
    assert 'dev' in result['configs']

    third = {
        'configs': {
            'dev': [
                'port 2',
            ],
        },
    }

    result = update_scope(first, third)
    assert 'port' not in result['configs']['dev']
