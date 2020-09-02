from Fraction import Fraction

fraction1 = Fraction(1,-4)
print(f'User inputed {fraction1}') # prints -1/4

fraction2 = Fraction(1,'j') # exception raised for nonint
fraction3 = Fraction(1,0) # exception raised for division by 0

fraction4 = Fraction(1,2)
fraction5 = Fraction(1,2)
fraction6 = Fraction(1,3)
fraction6 = Fraction(1,3)

# Overloading equals
print('Is {} equal to {}? Answer: {}'.format(fraction4, fraction6, fraction4 == fraction6))
print('Is {} equal to {}? Answer: {}'.format(fraction4, fraction5, fraction4 == fraction5))

# Overloading greater than
print('Is {} greater than {}? Answer: {}'.format(fraction4, fraction6,fraction4 > fraction6))
print('Is {} greater than {}? Answer: {}'.format(fraction6, fraction4,fraction6 > fraction4))

