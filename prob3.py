a=int(input('numaratorul primei fractie:'))
b=int(input('numitorul primei fractie:'))
x=int(input('numaratorul 2 fractie:'))
y=int(input('numitorul 2 fractie:'))
from fractions import Fraction
def sumafract():
    s=Fraction(a,b)+Fraction(x,y)
    return s
def produsfract():
    p=Fraction(a,b) * Fraction(x,y)
    return p
print('suma=', sumafract())
print('produsul=', produsfract())