import math


class Fraction:
    """
    Class that represent fractions

    proper: inform if Fraction should
    be in proper or in inproper form
    """

    proper = False

    def __init__(self, nom: int, denom: int):
        """
        Create a fraction with both 
        the denominator and numerator specified as integers

        Args:
            nom (int): nominator of the fraction
            denom (int): denominator of the fraction

        Raises:
            ZeroDivisionError: Franction cannot have zero in denominator
            TypeError: Nominator and denominator have to be integer
        """
        if denom == 0:
            raise ZeroDivisionError(
                "Franction cannot have zero in denominator.")
        elif type(nom) != int or type(denom) != int:
            raise TypeError("Nominator and denominator have to be integer.")
        sign = 1 if nom*denom > 0 else -1 if nom*denom < 0 else 0
        self.nom = sign*abs(nom)//math.gcd(nom, denom)
        self.denom = abs(denom)//math.gcd(nom, denom)
        self.sign = sign

    def __str__(self):
        """
        Create the text representation of Fraction.
        If denominator is equal to 1, representation 
        is only nominator. If proper is True, Fraction 
        is represented in property form, and if not 
        in inproperty form.

        Returns:
            (str): text representation of Fraction
        """
        if self.denom == 1:
            return str(self.nom)
        elif self.proper == True:
            int_num = (abs(self.nom)//self.denom)*self.sign
            if int_num != 0:
                return f"{int_num} {abs(self.nom)%self.denom}/{self.denom}"
        return f"{self.nom}/{self.denom}"

    def fractionconvert(self, number):
        """
        Check if number is Fraction class
        and if it isn't convert to Fraction class element

        Args:
            number (Fraction, int, float): number to check

        Returns:
            (Fraction): number in fraction form
        """
        if isinstance(number, Fraction):
            return number
        elif isinstance(number, int):
            return Fraction(number, 1)
        elif isinstance(number, float):
            num = str(number)
            comma = num.index(".")
            befcomma = num[0:comma]
            aftcomma = num[comma+1:]
            denom = 10**(len(aftcomma))
            sign = 1 if number > 0 else -1 if number < 0 else 0
            nom = sign*(int(aftcomma) + abs(int(befcomma))*denom)
            return Fraction(nom, denom)

    def __add__(self, other):
        """
        Add Fraction and other number, left addition operator

        Args:
            other (Fraction, int, float): other number to add to the Fraction

        Returns:
            (Fraction): Sum of Fraction and other number
        """
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom + other.nom * self.denom, self.denom * other.denom)

    def __radd__(self, other):
        """
        Add Fraction and other number, right addition operator

        Args:
            other (Fraction, int, float): other number to add to the Fraction

        Returns:
            (Fraction): Sum of Fraction and other number
        """
        return self + other

    def __sub__(self, other):
        """
        Subtract other number from the Fraction, left subtraction operator

        Args:
            other (Fraction, int, float): other number to subtract to the Fraction

        Returns:
            (Fraction): Difference of Fraction and other number
        """
        other = self.fractionconvert(other)
        return self + (-1)*other

    def __rsub__(self, other):
        """
        Subtract other number from the Fraction, right subtraction operator

        Args:
            other (Fraction, int, float): other number from which a Fraction is subtracted

        Returns:
            (Fraction): Difference of other number and Fraction
        """
        return other + (-1)*self

    def __mul__(self, other):
        """
        Multiply Fraction and other number, left multiplication operator

        Args:
            other (Fraction, int, float): other number with which the fraction is being multiplied

        Returns:
            (Fraction): Product of other number and Fraction
        """
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.nom, self.denom * other.denom)

    def __rmul__(self, other):
        """
        Multiply Fraction and other number, right multiplication operator

        Args:
            other (Fraction, int, float): other number with which the fraction is being multiplied

        Returns:
            (Fraction): Product of other number and Fraction
        """
        other = self.fractionconvert(other)
        return self * other

    def __truediv__(self, other):
        """
        Divide two fractions
        :param other: other Fraction
        """
        """
        Divide Fraction by other number, left multiplication operator

        Args:
            other (Fraction, int, float): other number by which the fraction will be divided

        Returns:
            (Fraction): Quotient of Fraction and other number
        """
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom, self.denom * other.nom)

    def __rtruediv__(self, other):
        """
        Divide other number by fraction, right multiplication operator

        Args:
            other (Fraction, int, float): other number that is divided by the fraction

        Returns:
            (Fraction): Quotient of other number and Fraction
        """
        other = self.fractionconvert(other)
        return Fraction(self.denom * other.nom, self.nom * other.denom)

    def __lt__(self, other):
        """
        Check < relation between Fraction and other number

        Args:
            other (Fraction, int, float): other number in relation

        Returns:
            (bool): True - relation takes place, False - no
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 < num2

    def __le__(self, other):
        """
        Check <= relation between Fraction and other number

        Args:
            other (Fraction, int, float): other number in relation

        Returns:
            (bool): True - relation takes place, False - no
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 <= num2

    def __eq__(self, other):
        """
        Check == relation between Fraction and other number

        Args:
            other (Fraction, int, float): other number in relation

        Returns:
            (bool): True - relation takes place, False - no
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 == num2

    def __ne__(self, other):
        """
        Check != relation between Fraction and other number

        Args:
            other (Fraction, int, float): other number in relation

        Returns:
            (bool): True - relation takes place, False - no
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 != num2

    def __gt__(self, other):
        """
        Check > relation between Fraction and other number

        Args:
            other (Fraction, int, float): other number in relation

        Returns:
            (bool): True - relation takes place, False - no
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 > num2

    def __ge__(self, other):
        """
        Check >= relation between Fraction and other number

        Args:
            other (Fraction, int, float): other number in relation

        Returns:
            (bool): True - relation takes place, False - no
        """
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 >= num2

    def getNum(self):
        """
        Show value of Fraction's nominator

        Returns:
            (int): value of nominator
        """
        return self.nom

    def getDem(self):
        """
        Show value of Fraction's denominator

        Returns:
            (int): value of denominator
        """
        return self.denom
