import pytest

from wasserstoff.parsers import (
    upper_keys,
    parse_text,
    parse_ini,
)


@pytest.mark.parametrize(
    'lower, upper', [
        (
            {'lower': 'key'}, {'LOWER': 'key'},
        ),
    ],
)
def test_upper_keys(lower, upper):
    result = upper_keys(lower)

    assert result == upper


def test_parse_text():
    with open('data/text', 'r', encoding='utf-8') as f:
        txt = parse_text(f)

    assert isinstance(txt, dict)


def test_parse_ini():
    ini = parse_ini(filename='data/env_test.ini')
    assert isinstance(ini, dict)
