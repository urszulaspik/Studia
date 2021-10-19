import math


class Fraction:
    """
    Class of fractions
    """

    mixed = False

    def __init__(self, nom, denom):
        """
        :param nom: nominator
        :param denom: denominator
        """
        if denom == 0:
            raise ZeroDivisionError(
                "Franction cannot have zero in denominator.")
        elif type(nom) != int or type(denom) != int:
            raise TypeError("Nominator and denominator have to be integer.")
        sign = 1 if nom * denom > 0 else -1 if nom * denom < 0 else 0
        self.nom = sign * abs(nom) // math.gcd(nom, denom)
        self.denom = abs(denom) // math.gcd(nom, denom)

    def __str__(self):
        num = math.gcd(self.nom, self.denom)
        if self.denom == 1:
            return str(self.nom)
        elif not self.mixed:
            return f"{self.nom // num}/{self.denom // num}"
        else:
            return f"{self.nom // self.denom} {self.nom % self.denom}/{self.denom}"

    @staticmethod
    def fractionconvert(number):
        """
        Convert number to fraction class
        :param number: number to convert to fraction class
        :return: number as an element in Fraction class
        """
        if isinstance(number, Fraction):
            return number
        elif isinstance(number, int):
            return Fraction(number, 1)
        elif isinstance(number, float):
            num = str(number)
            comma = num.index(".")
            befcomma = num[0:comma]
            aftcomma = num[comma + 1:]
            denom = 10 ** (len(aftcomma))
            nom = int(aftcomma) + int(befcomma) * denom
            return Fraction(nom, denom)

    def __add__(self, other):
        """
        Add two fractions
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom + other.nom * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        """
        Subtract two fractions
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom - other.nom * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        """
        Multiply two fractions
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.nom, self.denom * other.denom)

    def __truediv__(self, other):
        """
        Divide two fractions
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom, self.denom * other.nom)

    def __lt__(self, other):
        """
        Check < for two fraction
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 < num2

    def __le__(self, other):
        """
        Check <= for two fraction
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 <= num2

    def __eq__(self, other):
        """
        Check == for two fraction
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 == num2

    def __ne__(self, other):
        """
        Check != for two fraction
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 != num2

    def __gt__(self, other):
        """
        Check > for two fraction
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 > num2

    def __ge__(self, other):
        """
        Check >= for two fraction
        :param other: other Fraction
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 >= num2

    def getnum(self):
        """
        Return value of nominator
        """
        return self.nom

    def getdem(self):
        """
        Return value of denominator
        """
        return self.denom
