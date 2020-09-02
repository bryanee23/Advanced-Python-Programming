'''
Create a class named Fraction on a separate file Fraction.py.
Each Fraction object will represent a numerical fraction (i.e. 3/5, 2/3, etc)

Objects of this class should have two attributes, which the client sets through the constructor:
numerator
denominator

Overload the greater than, equals, and string methods for this class. The string method should print a string representation of the object. For example, if numerator is 5 and denominator is 3 for a Fraction object, it should print "5/3"

In a second file Main.py, demonstrate the use of this class. Create at least two Fraction objects and demonstrate the three different overloaded operators working on these objects.


When you are finished, you may either attach your .py files to this page or copy and paste your code as a text submission
'''

class Fraction:
    def __init__(self, top = int, bottom = int):
        self.numerator = top
        self.denominator = bottom
        self.check_fraction()
        self.evaluated_value = self.evaluate_fraction()

    def evaluate_fraction(self):
      return self.numerator / self.denominator

    def _check_numerator(self, num):
      if isinstance(num, int):
        return num
      else:
        raise ValueError(f'{num} is not an integer, please input an integer')

    def _check_denominator(self, num):
      if isinstance(num, int) == False:
        raise ValueError(f'{num} is not an integer, please input an integer')

      if num == 0:
          raise ValueError("The universe was destroyed because it cannot divide zero \nPlease a number other than 0")
      return num

    def check_fraction(self):
        self.numerator = self._check_numerator(self.numerator)
        self.denominator = self._check_denominator(self.denominator)

        if self.denominator < 0:
          self.numerator = -self.numerator
          self.denominator = abs(self.denominator)

    def __str__(self):
      return f'{self.numerator}/{self.denominator}'

    def __eq__(self, other):
      if self.evaluated_value == other.evaluated_value:
        return True
      else:
        return False

    def __gt__(self, other):
      if self.evaluated_value > other.evaluated_value:
        return True
      else:
        return False