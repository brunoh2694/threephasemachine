#6.10Fitzgerald
import numpy as np
import math as mt
import cmath as cm
import matplotlib.pyplot as plt

Vl= 460




vf=Vl/mt.sqrt(3)
Rs=0.103
Xs=1.1j
Rr=0.225
Xr=1.13j
Xm=59.4j
Rf= 962
Nsin=(120*60)/4

for s in range(1,4,1):
#velocidades
    Nmec = (1 - s/100) * Nsin
    wmec = Nmec*mt.pi*2/60
    wsin=Nsin*mt.pi/30

#corrente do estator
    zr=(Rr/(s/100))+Xr
    zm = (Xm*Rf)/(Xm+Rf)
    zeq=(zr*zm)/(zr+zm)
    zs=Rs+Xs
    ztotal= zeq+zs
    Zfinal= cm.polar(ztotal)#passa a impedancia para polar
    Is=vf/ztotal
    Ie=cm.polar(Is)#mostra a corrente na forma polar
    h=np.abs(Ie)#amostra  aparte absoluta do fasor corrente
    I= cm.phase(Is) #mostra o angulo da corrente
    Ireal = Is.real #mostra a parte real da corrente

#Potencias#####TRETERETERRTET
    Pin = mt.sqrt(3)*Vl*(h[0])*mt.cos(I)
    Pgap = Pin-(3*Rs*h[0]**2)
    Pconv=(1-s/100)*Pgap
    Pmec=Pconv-220-265
    rend=(Pmec/Pin)*100

#Torque
    Tmec = Pmec/wmec
    Tin= Pgap/wsin
 #Resultados
    print(f'\nPara o escorregamento S={s/100} tem-se:')
    print(f'A velocidade é {Nmec} m/s e {wmec} rad/s')
    print(f'O torque mecânico é {Tmec} N.m')
    print(f'O torque induzido é {Tin} N.m')
    print(f'o fator de potência é {mt.cos(I)}')
    print(f'A potência de entrada é {Pin/1000} kW')
    print(f'A potência de saida é {Pmec/1000} kW')
    print(f'O rendimento é {rend} %')
    print(f'{Ireal}')
#GRÁFICO
x = Pmec
y= Tin
plt.plot (x,y)
plt.show()
