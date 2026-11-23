import sys
sys.path.insert(0, '/Users/norahattrem/Desktop/Programmering/Visual_Studio_Code/INF201/Deliverable4/Deliverable_4/src/')

import pytest
from fraction import Fractions


def test_init() -> None:
    fraction = Fractions(2, 3)

    assert fraction.numerator == 2
    assert fraction.denominator == 3


def test_init_invalid_denominator() -> None:
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


@pytest.mark.parametrize("fraction1, fraction2",
                        [[Fractions(1, 2), Fractions(2, 4)]
                        ])
def test_equal(fraction1: Fractions, fraction2: Fractions) -> None:
    assert fraction1 == fraction2


@pytest.mark.parametrize("fraction1, fraction2",
                        [[Fractions(1, 2), Fractions(2, 3)]
                        ])
def test_not_equal(fraction1: Fractions, fraction2: Fractions) -> None:
    assert fraction1 != fraction2


@pytest.mark.parametrize("fraction1, fraction2",
                        [[Fractions(1, 2), Fractions(3, 4)]
                        ])
def test_less_than(fraction1: Fractions, fraction2: Fractions) -> None:
    assert fraction1 < fraction2


@pytest.mark.parametrize("fraction1, fraction2",
                        [[Fractions(3, 6), Fractions(2, 4)],
                         [Fractions(2, 5), Fractions(2, 3)]
                        ])
def test_less_than_or_equal(fraction1: Fractions, fraction2: Fractions) -> None:
    assert fraction1 <= fraction2


@pytest.mark.parametrize("fraction1, fraction2",
                        [[Fractions(6, 5), Fractions(3, 7)]
                        ])
def test_greater_than(fraction1: Fractions, fraction2: Fractions) -> None:
    assert fraction1 > fraction2


@pytest.mark.parametrize("fraction1, fraction2",
                        [[Fractions(3, 4), Fractions(6, 8)],
                         [Fractions(2, 2), Fractions(1, 3)]
                        ])
def test_greater_than_or_equal(fraction1: Fractions, fraction2: Fractions) -> None:
    assert fraction1 >= fraction2


@pytest.mark.parametrize("adding, expected",
                        [[Fractions(2, 3) + Fractions(1, 2), Fractions(7, 6)]
                        ])
def test_add(adding: Fractions, expected: Fractions) -> None:
    assert adding == expected


@pytest.mark.parametrize("subtracting, expected",
                        [[Fractions(2, 3) - Fractions(1, 2), Fractions(1, 6)]
                        ])
def test_subtract(subtracting: Fractions, expected: Fractions) -> None:
    assert subtracting == expected


@pytest.mark.parametrize("multiplying, expected",
                        [[Fractions(2, 3) * Fractions(1, 2), Fractions(2, 6)]
                        ])
def test_multiply(multiplying: Fractions, expected: Fractions) -> None:
    assert multiplying == expected


@pytest.mark.parametrize("dividing, expected",
                        [[Fractions(1, 2) / Fractions(3, 4), Fractions(4, 6)]
                        ])
def test_divide(dividing: Fractions, expected: Fractions) -> None:
    assert dividing == expected
