import math


class Fraction:
    "Class that represent fractions"
    
    mixed=False
    def __init__(self, nom, denom):
        '''
        :param nom: nominator
        :param denom: denominator
        '''
        if denom == 0:
            raise ZeroDivisionError("Franction cannot have zero in denominator.")
        elif type(nom) != int or type(denom) != int:
            raise TypeError("Nominator and denominator have to be integer.")
        sign = 1 if nom*denom > 0 else -1 if nom*denom < 0 else 0
        self.nom = sign*abs(nom)//math.gcd(nom, denom)
        self.denom = abs(denom)//math.gcd(nom, denom)
        self.sign = sign

    def __str__(self):
        num = math.gcd(self.nom, self.denom)
        if self.denom == 1:
            return str(self.nom)
        elif self.mixed == True:
            int_num = (abs(self.nom)//self.denom)*self.sign
            if int_num != 0:
                return f"{int_num} {self.nom%self.denom}/{self.denom}"
        return f"{self.nom//num}/{self.denom//num}"
    
    def fractionconvert(self, number):
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
            nom = int(aftcomma) + int(befcomma)*denom
            return Fraction(nom, denom)

    def __add__(self, other):
        '''
        Add two fractions
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom + other.nom * self.denom, self.denom * other.denom)
    
    def __radd__(self, other):
        '''
        Add two fractions
        :param other: other Fraction
        '''
        return self+other

    def __sub__(self, other):
        '''
        Subtract two fractions
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom - other.nom * self.denom, self.denom * other.denom)
    
    def __rsub__(self, other):
        '''
        Subtract two fractions
        :param other: other Fraction
        '''
        return other+(-1)*self

    def __mul__(self, other):
        '''
        Multiply two fractions
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.nom, self.denom * other.denom)
    
    def __rmul__(self, other):
        other = self.fractionconvert(other)
        return self*other

    def __truediv__(self, other):
        '''
        Divide two fractions
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        return Fraction(self.nom * other.denom, self.denom * other.nom)

    def __rtruediv__(self, other):
        '''
        Divide two fractions
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        return Fraction(self.denom * other.nom, self.nom * other.denom)

    def __lt__(self, other):
        '''
        Check < for two fraction
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 < num2

    def __le__(self, other):
        '''
        Check <= for two fraction
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 <= num2

    def __eq__(self, other):
        '''
        Check == for two fraction
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 == num2

    def __ne__(self, other):
        '''
        Check != for two fraction
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 != num2

    def __gt__(self, other):
        '''
        Check > for two fraction
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 > num2

    def __ge__(self, other):
        '''
        Check >= for two fraction
        :param other: other Fraction
        '''
        other = self.fractionconvert(other)
        num1 = self.nom * other.denom
        num2 = other.nom * self.denom
        return num1 >= num2

    def getnum(self):
        '''
        Return value of nominator
        '''
        return self.nom

    def getdem(self):
        '''
        Return value of denominator
        '''
        return self.denom


y1=-2
y2=Fraction(2, 3)
print(y1/y2)