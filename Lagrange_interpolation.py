from math import*
import numpy as np
import matplotlib.pyplot as pl
datosx=[0,25,50,75,100,125,150,175,200]
datosy=[10.6,16.0,45.0,83.5,52.8,19.9,10.8,8.25,4.7]

def Lagrange(lx,ly):
    n=len(lx)
    gdex=[]

    for i in range(n):  
        a=1
        for j in range(n):
            k=lx[i]-lx[j]
            if j==i:
                pass
            else :
                a*=np.poly1d([1,-lx[j]])/k
    
        gdex.append(a)


    for i in range(n):
        gdex[i]*=ly[i]
    polinomio=0
    for i in range(n):
        polinomio+=gdex[i]

    return polinomio

def grafica1(lx,ly):
    polinomio=Lagrange(datosx,datosy)
    ejex=np.arange(0,201,1) 
    ejey=polinomio(ejex)# fill an array with the values evaluated in the Lagrange polynomial


    #eje horizontal
    gam=np.linspace(48.71,106.39,30)
    gam1=np.ones(len(gam))*41.7080
    
    #eje vertical 
    vy=np.linspace(0,83.4161,5)
    vx=np.ones(len(vy))*74.58

    fig, ax = pl.subplots()
    ax.plot(lx,ly,'ro',label='Experimental data.\n')
    ax.plot(ejex,ejey,'k',linewidth=0.9,label='\Lagrange interpolating polynomial.\n')
    ax.plot(48.71,41.708,'bo',label='Er-Γ/2')
    ax.plot(106.39,41.708,'co',label='Er+Γ/2')
    ax.plot(gam,gam1,'b',linestyle='dotted')
    ax.plot(vx,vy,'r',linestyle='dashdot',label='\nResonance energy \nEr=74.58 Mev.\n')
    legend = ax.legend(loc='upper right', shadow=True, fontsize='small')
    pl.title("Lagrange interpolation.")
    pl.grid(True)
    pl.show()


#incido d) del problema 3
listpolinomios=[]
for i in range(0,8,2):
    listax=[]
    listay=[]
    for j in range(i,i+3):
        listax.append(datosx[j])
        listay.append(datosy[j])
    listpolinomios.append(Lagrange(listax,listay))
#display data in 5 Mev steps

print("Data for Lagrange interpolation\with 5 MeV steps.")
for i in range(0,205,5):
    if i<=50:
        print(f'f({i})={listpolinomios[0](i)}')
    if 50<i<=100:
        print(f'f({i})={listpolinomios[1](i)}')
    if 100<i<=150:
        print(f'f({i})={listpolinomios[2](i)}')
    if 150<i<=200:
        print(f'f({i})={listpolinomios[3](i)}')
   


def grafica2():
        #eje horizontal
    gam=np.linspace(48.0521,105.598,30)
    gam1=np.ones(len(gam))*41.8049
    
    #eje vertical 
    vy=np.linspace(0,83.6098,5)
    vx=np.ones(len(vy))*76.4089
    
    
    x1=np.linspace(0,50,50)
    y1=listpolinomios[0](x1)
    x2=np.linspace(50,100,50)
    y2=listpolinomios[1](x2)
    x3=np.linspace(100,150,50)
    y3=listpolinomios[2](x3)
    x4=np.linspace(150,200,50)
    y4=listpolinomios[3](x4)


    fig, ax = pl.subplots()
    ax.plot(x1,y1,'r',linewidth=0.9)
    ax.plot(x2,y2,'k',linewidth=0.9)
    ax.plot(x3,y3,'g',linewidth=0.9)
    ax.plot(x4,y4,'b',linewidth=0.9)
    
    ax.plot(datosx,datosy,'ro',label='Experimental data.\n')
    ax.plot(48.0521,41.8089,'bo',label='Er-Γ/2')
    ax.plot(105.598,41.8089,'co',label='Er+Γ/2')
    ax.plot(gam,gam1,'b',linestyle='dotted')
    ax.plot(vx,vy,'r',linestyle='dashdot',label='Resonance energy. \nEr=76.4089 Mev\n')
    legend = ax.legend(loc='upper right', shadow=True, fontsize='small')
    pl.title("Lagrange interpolation every 3 points.")
    pl.grid(True)
    pl.show()


grafica1(datosx,datosy)
grafica2()

