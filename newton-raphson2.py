from math import e

def f(x):
	return(x**2-2*x-3)

def fi(x):
	return(2*x-2)

def hata(x1,x2):
	return((x1-x2)/x1)

xi=int(input("Baslangic degeri : " ))

while(True):
	xr=xi-(f(xi)/fi(xi))
	if(f(xr)==0):
		print(xr,xi,hata(xi,xr))
		break
	else:
		xi=xr

