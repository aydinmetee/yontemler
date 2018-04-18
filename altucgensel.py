dosya=open("katsayilar.txt")
matris= []

for line in dosya.readlines():
	line=line.rstrip('\n').split(' ')
	matris.append(line)
dosya.close()

##Bu kod bir matrisi alt ücgensel matrise cevirir.

boyut=len(matris)

for i in range(boyut):
	kat=int(matris[i][i])
	for j in range(boyut+1):
		matris[i][j]=float(matris[i][j])/kat
	for k in range(1,boyut-i):
		kat=float(matris[k+i][i])
		for z in range(boyut+1):
			matris[k+i][z]=float(matris[k+i][z])-float(matris[i][z])*(kat/float(matris[i][i]))

print(matris)

##Bu kod alt ücgensel matrisi birim matrise  cevirir.

for i in range(boyut-1,0,-1):
	for k in range(0,i):
		kat=float(matris[k][i])
		for j in range(i,boyut+1):
			matris[k][j]=float(matris[k][j])-(float(matris[i][j])*kat)

print(matris)
