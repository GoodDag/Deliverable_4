import math as m


class Fractions:
    def __init__(self, numerator: int, denominator: int):

        if not isinstance(numerator, int):
            raise TypeError("Must be integer")

        if not isinstance(denominator, int):
            raise TypeError("Must be integer")

        if denominator <= 0:
            raise ValueError("Denominator has to be positive ")

        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other: Fractions) -> bool:
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other: Fractions) -> bool:
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other: Fractions) -> bool:
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: Fractions) -> bool:
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other: Fractions) -> bool:
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: Fractions) -> bool:
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __add__(self, other: Fractions) -> Fractions:
        add_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        add_denominator = self.denominator * other.denominator
        return Fractions(add_numerator, add_denominator)

    def __sub__(self, other: Fractions) -> Fractions:
        sub_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        sub_denominator = self.denominator * other.denominator
        return Fractions(sub_numerator, sub_denominator)

    def __mul__(self, other: Fractions) -> Fractions:
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        return Fractions(mul_numerator, mul_denominator)

    def __truediv__(self, other: Fractions) -> Fractions:
        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        return Fractions(div_numerator, div_denominator)

    def __str__(self) -> str:
        """String representation of Temperatures object"""
        return f"{self.numerator:.2f} / {self.denominator}"

    def __repr__(self) -> str:
        """Representation of Temperatures object"""
        return f"Fraction({self.numerator} / {self.denominator})"


test1 = Fractions(2, 3)
test2 = Fractions(1, 2)

print(test1 + test2)
