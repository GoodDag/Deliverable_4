import sys
sys.path.insert(0, '/Users/norahattrem/Desktop/Programmering/Visual_Studio_Code/INF201/Deliverable4/Deliverable_4/src/')

import pytest
from temperature import Temperatures

use = Temperatures(value=25, unit='celsius')


def test_default_unit() -> None:
    """Default unit??????????"""
    pass


def test_case_insensitive_units() -> None:
    assert use.unit == 'C'


def test_read_only_behavior() -> None:
    with pytest.raises(AttributeError):
        use.value = 50


def test_invalid_unit_string() -> None:
    with pytest.raises(ValueError):
        Temperatures(value=25, unit='degrees')


@pytest.mark.parametrize("value, unit",
                         [[-300, 'C'],
                          [-500, 'F'],
                          [-10, 'K']
                          ])
def test_below_absolute_zero(value: int | float, unit: str) -> None:
    with pytest.raises(ValueError):
        Temperatures(value=value, unit=unit)


@pytest.mark.parametrize("temp, celsius",
                         [[Temperatures(value=0, unit='K'), -273.15],
                          [Temperatures(value=-40, unit='F'), -40],
                          [Temperatures(value=0, unit='C'), -0],
                          [Temperatures(value=98.6, unit='F'), 37],
                          [Temperatures(value=373.15, unit='K'), 100]
                          ])
def test_conversion_celsius(temp: Temperatures, celsius: int | float) -> None:
    assert pytest.approx(temp.to_celsius()) == celsius


@pytest.mark.parametrize("temp, fahrenheit",
                         [[Temperatures(value=-273.15, unit='C'), -459.67],
                          [Temperatures(value=-40, unit='F'), -40],
                          [Temperatures(value=273.15, unit='K'), 32],
                          [Temperatures(value=37, unit='C'), 98.6],
                          [Temperatures(value=373.15, unit='K'), 212]
                          ])
def test_conversion_fahrenheit(temp: Temperatures, fahrenheit: int | float) -> None:
    assert pytest.approx(temp.to_fahrenheit()) == fahrenheit


@pytest.mark.parametrize("temp, kelvin",
                         [[Temperatures(value=-459.67, unit='F'), 0],
                          [Temperatures(value=-40, unit='C'), 233.15],
                          [Temperatures(value=32, unit='F'), 273.15],
                          [Temperatures(value=310.15, unit='K'), 310.15],
                          [Temperatures(value=100, unit='C'), 373.15]
                          ])
def test_conversion_kelvin(temp: Temperatures, kelvin: int | float) -> None:
    assert pytest.approx(temp.to_kelvin()) == kelvin


def test_round_trip_conversions() -> None:
    assert use.value == use.convert_to('F').convert_to('K').convert_to('C').value


def test_cross_unit_comparisons() -> None:
    pass


def test_formatting() -> None:
    pass