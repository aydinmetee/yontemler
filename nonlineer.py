from math import e

def f(a,b):
	return(-4+a**2+b**2)

def g(a,b):
	return(-1+e**a+b)

def fa(a,b):
	return(2*a)
def fb(a,b):
	return(2*b)
def ga(a,b):
	return(e**a)
def gb(a,b):
	return(1)


xi,yi=1.0,2.0

for i in range(10):
	deltay=(-f(xi,yi)*ga(xi,yi)+g(xi,yi)*fa(xi,yi))/(fb(xi,yi)*ga(xi,yi)-gb(xi,yi)*fa(xi,yi))
	deltax=(-f(xi,yi)-fb(xi,yi)*deltay)/fa(xi,yi)
	xi=xi+deltax
	yi=yi+deltay

print(xi,yi)
	
