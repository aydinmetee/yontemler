def f(a):
	return((a**2)-(a*2)-3)

x1=int(input("Birinci sayiyi girin :"))
x2=int(input("İkinci sayiyi girin :"))

if(f(x1)*f(x2)==0):
	print("Girdiginiz sayilardan biri denklemin köküdür.")
elif(f(x1)*f(x2)>0):
	print("Bu aralikta denklemin bir kökü yoktur.")
else:
	for i in range(100):
		xu=(x1+x2)/2
		if(f(xu)==0):
			print("kök = ",xu)
			print("i = ",i)
			break
		elif(f(x2)*f(xu)<0):
			x1=xu
		else:
			x2=xu

