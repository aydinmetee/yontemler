katsayilar=[[3,2],[-1,2]]

degerler=[[18],[2]]

x2=(katsayilar[0][0]*degerler[1][0]-katsayilar[1][0]*degerler[0][0])/(katsayilar[0][0]*katsayilar[1][1]-katsayilar[1][0]*katsayilar[0][1])

x1=(degerler[0][0]-(katsayilar[0][1]*x2))/katsayilar[0][0]


print(x1,x2)
