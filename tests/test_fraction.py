import sys
sys.path.insert(0, '/Users/norahattrem/Desktop/Programmering/Visual_Studio_Code/INF201/Deliverable4/Deliverable_4/src/')

import pytest
from fraction import Fractions


def test_init():
    fraction = Fractions(2, 3)

    assert fraction.numerator == 2
    assert fraction.denominator == 3


def test_init_invalid_denominator():
    with pytest.raises(ValueError):
        Fractions(2, 0)

    with pytest.raises(ValueError):
        Fractions(2, -3)


@pytest.mark.parametrize("numerator, denominator",
                         [[2, 2.5],
                         [2.5, 2]
                         ])
def test_init_invalid_type(numerator: int | float, denominator: int | float) -> None:
    with pytest.raises(TypeError):
        Fractions(numerator, denominator)


def test_equal():
    fracton1 = Fractions(1, 2)
    fraction2 = Fractions(2, 4)

    assert fracton1 == fraction2


def test_not_equal():
    fracton1 = Fractions(1, 2)
    fraction2 = Fractions(2, 3)

    assert fracton1 != fraction2


def test_less_than():
    fracton1 = Fractions(1, 2)
    fraction2 = Fractions(2, 3)

    assert fracton1 < fraction2


def test_less_than_or_equal():
    fracton1 = Fractions(1, 2)
    fraction2 = Fractions(2, 3)

    assert fracton1 <= fraction2


def test_greater_than():
    fracton1 = Fractions(2, 3)
    fraction2 = Fractions(1, 2)

    assert fracton1 > fraction2


def test_greater_than_or_equal():
    fracton1 = Fractions(2, 3)
    fraction2 = Fractions(1, 2)

    assert fracton1 >= fraction2


@pytest.mark.parametrize("adding, expected",
                         [[Fractions(2, 3) + Fractions(1, 2), Fractions(7, 6)]
                           ])
def test_add(adding, expected):
    assert adding == expected


def test_subtract():
    fracton1 = Fractions(2, 3)
    fraction2 = Fractions(1, 2)

    assert fracton1 - fraction2


def test_multiply():
    fracton1 = Fractions(2, 3)
    fraction2 = Fractions(1, 2)

    assert fracton1 * fraction2


def test_divide():
    fracton1 = Fractions(2, 3)
    fraction2 = Fractions(1, 2)

    assert fracton1 / fraction2

