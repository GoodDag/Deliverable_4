import math as m
from functools import total_ordering


@total_ordering
class Temperatures:
    """Class that supports convertion and comparisons between temperatures
    in Celsius (C), Fahrenheit (F) and Kelvin (K)"""

    def __init__(self, value: int | float, unit: str) -> None:
        """
        Initialise the temperature
        Args:
        value (int | float): The number value of the temperature
        unit (str): The unit the temperature is in
        """
        self._value = value
        self._unit = unit.strip().upper()[0]

        if self._unit not in ["C", "F", "K"]:  # Maybe not include full words?
            raise ValueError('Unit must be celsius (C), Fahrenheit (F) or Kelvin (K)')

        if self._value < 0 and self._unit == "K" or self._value < -273.15 and self._unit == "C" or self._value < -459.67 and self._unit == "F":
            raise ValueError('Value cannot be below absolute zero')  # Somehow make shorter?

    @property  # read only attribute not property?
    def value(self) -> int | float:
        """Public read-only property to inspect value"""
        return self._value

    @property  # read only attribute not property?
    def unit(self) -> str:
        """Public read-only property to inspect unit"""
        return self._unit

    def to_celsius(self) -> float:
        """Converts given value to celsius"""
        if self._unit == "K":
            self._value = self._value - 273.15
            self._unit = "C"
            return self._value

        if self._unit == "F":
            self._value = (self._value - 32) * (5 / 9)
            self._unit = "C"
            return self._value

        else:
            return self._value

    def to_fahrenheit(self) -> float:
        """Converts given value to fahrenheit"""
        if self._unit == "C":
            self._value = self._value * (9 / 5) + 32
            self._unit = "F"
            return self._value

        if self._unit == "K":
            self._value = (self._value - 273.15) * (9 / 5) + 32
            self._unit = "F"
            return self._value

        else:
            return self._value

    def to_kelvin(self) -> float:
        """Converts given value to kelvin"""
        if self._unit == "C":
            self._value = self._value + 273.15
            self._unit = "K"
            return self._value

        if self._unit == "F":
            self._value = (self._value - 32) * (5 / 9) + 273.15
            self._unit = "K"
            return self._value

        else:
            return self._value

    def convert_to(self, target_unit: str) -> Temperatures:
        """Converts given value to a given unit"""
        if target_unit.strip().upper()[0] == "C":
            self._value = self.to_celsius()

        if target_unit.strip().upper()[0] == "F":
            self._value = self.to_fahrenheit()

        if target_unit.strip().upper()[0] == "K":
            self._value = self.to_kelvin()

        return Temperatures(value=self._value, unit=target_unit)

    def __repr__(self) -> str:
        """Representation of Temperatures object"""
        return f"Temperature({self._value}, {self._unit})"

    def __str__(self) -> str:
        """String representation of Temperatures object"""
        return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other: object) -> bool:
        """Checks if two given temperature values are equal"""
        tol = 1e-9
        if not isinstance(other, Temperatures):
            return NotImplemented
        if self._unit == other._unit:
            return self._value == other._value
        else:  # Maybe remove upper, cause doesnt matter if same, can convert anyway?
            return m.isclose(self.to_celsius(), other.to_celsius(), rel_tol=tol, abs_tol=tol)

    def __lt__(self, other: Temperatures) -> bool:
        """Checks if a given temperature value is less than another temperature value"""
        if not isinstance(other, Temperatures):
            return NotImplemented
        if self._unit == other._unit:
            return self._value < other._value
        else:
            return self.to_celsius() < other.to_celsius()


temp = Temperatures(value=0, unit='c')
print(temp.value, temp.unit)
print(temp.to_celsius(), temp.unit)
print(temp.to_fahrenheit(), temp.unit)
print(temp.to_kelvin(), temp.unit)
print()
to_c = temp.convert_to(target_unit='c')
print(to_c.value, to_c.unit)
print(temp.__repr__())
print(temp)
print()

t1 = Temperatures(value=32, unit='f')
t2 = Temperatures(value=0, unit='c')
print(f't1 == t2: {t1 == t2}')
print(f't1 != t2: {t1 != t2}')
print(f't1 < t2: {t1 < t2}')
print(f't1 <= t2: {t1 <= t2}')
print(f't1 > t2: {t1 > t2}')
print(f't1 >= t2: {t1 >= t2}')
