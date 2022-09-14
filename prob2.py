from math import factorial
n=int(input('n= '))
m=int(input('m= '))
def f(x):
    s=0
    d=1
    for i in range(1, x+1):
        d*=1
    return d
nr=factorial(m) * (factorial(n-m))
c=factorial(n)/nr
print('n/m(n-m) =',c)