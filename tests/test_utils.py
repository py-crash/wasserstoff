import pytest

from wasserstoff.utils import pull, stylize
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
    ],
)
def test_stylize(var, stylized):
    result = stylize(var)

    assert result is not None
    assert result == stylized
