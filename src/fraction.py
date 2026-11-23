import math as m


class Fractions:
    def __init__(self, numerator: int, denominator: int):
        """
        Initialise the fractions
        Args:
        numerator (int): the number over the fractional line
        denominator (int): the number under the fractional line
        """
        if not isinstance(numerator, int):
            raise TypeError("Must be integer")

        if not isinstance(denominator, int):
            raise TypeError("Must be integer")

        if denominator <= 0:
            raise ValueError("Denominator has to be positive ")

        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other: Fractions) -> bool:
        """Checks if two fractions are equal"""
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other: Fractions) -> bool:
        """Checks if two fractions are not equal"""
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other: Fractions) -> bool:
        """Checks if one fraction are less than another"""
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: Fractions) -> bool:
        """Checks if one fraction are less than or equal another"""
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other: Fractions) -> bool:
        """Checks if one fraction are greater than another"""
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: Fractions) -> bool:
        """Checks if one fraction are greater than or equal with another"""
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __add__(self, other: Fractions) -> Fractions:
        """Adding two fractions"""
        add_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        add_denominator = self.denominator * other.denominator
        return Fractions(add_numerator, add_denominator)

    def __sub__(self, other: Fractions) -> Fractions:
        """Substracting two fractions"""
        sub_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        sub_denominator = self.denominator * other.denominator
        return Fractions(sub_numerator, sub_denominator)

    def __mul__(self, other: Fractions) -> Fractions:
        """Multiplying two fractions"""
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        return Fractions(mul_numerator, mul_denominator)

    def __truediv__(self, other: Fractions) -> Fractions:
        """Dividing two fractions"""
        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        return Fractions(div_numerator, div_denominator)
    