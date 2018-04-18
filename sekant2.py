def f(x):
	return(x**2-2*x-3)

def hata(x1,x2):
	return((x1-x2)/x1)

x1=int(input("Birinci deger:"))

x3=int(input("İkinci deger: "))

while(True):
	x2=x1-((f(x1)*(x3-x1))/(f(x3)-f(x1)))
	if(int(f(x2)==0)):
		print(x2)
		break
	x1,x3=x3,x2
