import sys
sys.path.insert(0, '/Users/norahattrem/Desktop/Programmering/Visual_Studio_Code/INF201/Deliverable4/Deliverable_4/src/')

import pytest
from temperature import Temperatures

default = Temperatures()

@pytest.mark.parametrize("default, expected",
                         [[default.value, 25],
                         [default.unit, 'C']
                         ])
def test_default_unit(default: int | str, expected: int | str) -> None:
    assert default == expected


def test_case_insensitive_units() -> None:
    assert default.unit == 'C'


def test_read_only_behavior() -> None:
    with pytest.raises(AttributeError):
        default.value = 50


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
    assert default.value == default.convert_to('F').convert_to('K').convert_to('C').value


@pytest.mark.parametrize("temp1, temp2",
                         [[Temperatures(value=0, unit='C'), Temperatures(value=0, unit='C')],
                          [Temperatures(value=298.15, unit='K'), Temperatures(value=25, unit='C')],
                          [Temperatures(value=89.6, unit='F'), Temperatures(value=305.15, unit='K')],
                          ])
def test_equality(temp1: Temperatures, temp2: Temperatures) -> None:
    assert temp1 == temp2


@pytest.mark.parametrize("temp1, temp2",
                         [[Temperatures(value=15, unit='K'), Temperatures(value=0, unit='K')],
                          [Temperatures(value=50, unit='F'), Temperatures(value=25, unit='C')],
                          [Temperatures(value=100, unit='C'), Temperatures(value=60, unit='K')],
                          ])
def test_not_equal(temp1: Temperatures, temp2: Temperatures) -> None:
    assert temp1 != temp2


@pytest.mark.parametrize("temp1, temp2",
                         [[Temperatures(value=10, unit='F'), Temperatures(value=30, unit='F')],
                          [Temperatures(value=0, unit='C'), Temperatures(value=60, unit='F')],
                          [Temperatures(value=40, unit='K'), Temperatures(value=0, unit='C')],
                          ])
def test_less_than(temp1: Temperatures, temp2: Temperatures) -> None:
    assert temp1 < temp2


@pytest.mark.parametrize("temp1, temp2",
                         [[Temperatures(value=55, unit='K'), Temperatures(value=55, unit='K')],
                          [Temperatures(value=0, unit='F'), Temperatures(value=20, unit='C')],
                          [Temperatures(value=-30, unit='F'), Temperatures(value=238.71, unit='K')],
                          ])
def test_less_or_equal(temp1: Temperatures, temp2: Temperatures) -> None:
    assert temp1 <= temp2


@pytest.mark.parametrize("temp1, temp2",
                         [[Temperatures(value=16, unit='F'), Temperatures(value=15, unit='F')],
                          [Temperatures(value=-40, unit='F'), Temperatures(value=150, unit='K')],
                          [Temperatures(value=5, unit='C'), Temperatures(value=100, unit='K')],
                          ])
def test_greater_than(temp1: Temperatures, temp2: Temperatures) -> None:
    assert temp1 > temp2


@pytest.mark.parametrize("temp1, temp2",
                         [[Temperatures(value=10, unit='C'), Temperatures(value=10, unit='C')],
                          [Temperatures(value=40, unit='F'), Temperatures(value=20, unit='K')],
                          [Temperatures(value=25, unit='C'), Temperatures(value=77, unit='F')],
                          ])
def test_greater_or_equal(temp1: Temperatures, temp2: Temperatures) -> None:
    assert temp1 >= temp2


@pytest.mark.parametrize("formatting, expected",
                         [[default.__repr__(), 'Temperature(25, C)'],
                          [default.__str__(), '25.00 °C']
                          ])
def test_formatting(formatting: str, expected: str) -> None:
    assert formatting == expected
