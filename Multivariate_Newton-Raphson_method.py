from numpy import *
from numpy.linalg import *
import matplotlib.pyplot as pl
d=1e-6
x=[0,25,50,75,100,125,150,175,200]
y=[10.6,16.0,45.0,83.5,52.8,19.9,10.8,8.25,4.7]
s=[9.34,17.9,41.5,85.5,51.5,21.5,10.8,6.29,4.14]

def f1(a1,a2,a3):
    f1=0
    for i in range(9):
        f1+=(1/(s[i])**2)*((y[i]*((x[i]-a2)**2 + a3)-a1)/
        (((x[i]-a2)**2 + a3)**2))
    return f1
def f2(a1,a2,a3):
    f2=0
    for i in range(9):
        f2+=(1/(s[i])**2)*(((y[i]*((x[i]-a2)**2 + a3)-a1)*(x[i]-a2))/
        (((x[i]-a2)**2 + a3)**3))
    return f2
def f3(a1,a2,a3):
    f3=0
    for i in range(9):
        f3+=(1/(s[i])**2)*((y[i]*((x[i]-a2)**2 +a3)-a1)/
        (((x[i]-a2)**2 + a3)**3))
    return f3
def jacobiana(a1,a2,a3):
    jacob=zeros((3,3))
    jacob[0][0]=(f1(a1+d/2,a2,a3)-f1(a1-d/2,a2,a3))/d
    jacob[0][1]=(f1(a1,a2+d/2,a3)-f1(a1,a2-d/2,a3))/d
    jacob[0][2]=(f1(a1,a2,a3+d/2)-f1(a1,a2,a3-d/2))/d
    jacob[1][0]=(f2(a1+d/2,a2,a3)-f2(a1-d/2,a2,a3))/d
    jacob[1][1]=(f2(a1,a2+d/2,a3)-f2(a1,a2-d/2,a3))/d
    jacob[1][2]=(f2(a1,a2,a3+d/2)-f2(a1,a2,a3-d/2))/d
    jacob[2][0]=(f3(a1+d/2,a2,a3)-f3(a1-d/2,a2,a3))/d
    jacob[2][1]=(f3(a1,a2+d/2,a3)-f3(a1,a2-d/2,a3))/d
    jacob[2][2]=(f3(a1,a2,a3+d/2)-f3(a1,a2,a3-d/2))/d
    return jacob
def vectorf(a1,a2,a3):
    vecf=zeros(3)
    vecf[0]=f1(a1,a2,a3)
    vecf[1]=f2(a1,a2,a3)
    vecf[2]=f3(a1,a2,a3)
    return vecf


def paso(a1,a2,a3):
    vector=zeros(3)
    for i in range(3):
        vector[i]=(-1*dot(inv(jacobiana(a1,a2,a3)),vectorf(a1,a2,a3)))[i]

    return vector

def newton(x):
    solucion=zeros(3)

    err=1.e-6
    nmax=1000
    #semilla


    y=80# Vaores aproximados conocidos 
    z=80# Valores aproximados conocidos
    f=vectorf(x,y,z)
    
    if f[0]==0 and f[1]==0 and f[2]==0:
        print("The solution was found on the first try")
    
    for i in range(nmax):
        dpaso=paso(x,y,z)
        f=vectorf(x,y,z)
        #print(f)
        if abs(f[0])<err and abs(f[1])<err and abs(f[2])<err:
            #print(f"se encontro")
            break
        else:
            x+=dpaso[0]
            y+=dpaso[1]
            z+=dpaso[2]

        if i==nmax-1:   
            print("The required error was not encountered")
        
    
    solucion[0]=x;solucion[1]=y;solucion[2]=z
    return solucion


#esta funcion barre varios valores positivos de x
def verif():
    for i in range(0,100000,500):
        print(newton(i))
verif()#puede mandar a llamarla de manera opcional

sol=newton(90)
print(f"Las soluciones son\n")
print(f"a1={sol[0]} \na2={sol[1]}\na3={sol[2]}")
print(f"\nLas soluciones en el problema son:\n")
print(f"fr={sol[0]} \nEr={sol[1]}\nΓ={sqrt(4*sol[2])}")


def grafica():
    dx=[0,25,50,75,100,125,150,175,200]
    dy=[10.6,16.0,45.0,83.5,52.8,19.9,10.8,8.25,4.7]
    def fun(x,f,e,g):
        return (f)/((x-e)**2 + g)
    
    x=arange(0,202,2)
    y=fun(x,sol[0],sol[1],sol[2])

    hx=linspace(50.1358,106.301,30)
    hy=ones(len(hx))*43.7072
    vy=linspace(0,87.4145,5)
    vx=ones(len(vy))*78.2183




    fig, ax = pl.subplots()
    ax.plot(x,y,'k',linewidth=0.9,label='f(E)')
    ax.plot(hx,hy,'b',linestyle='dotted')
    ax.plot(vx,vy,'r',linestyle='dashdot',label='\nResonance energy \nEr=78.2183 Mev\n')
    ax.plot(dx,dy,'ro',label='Experimental data')
    ax.plot(50.1358,43.7072,'bo',label='Er-Γ/2')
    ax.plot(106.301,43.7072,'co',label='Er+Γ/2')
    legend = ax.legend(loc='upper right', shadow=True, fontsize='small')
    pl.title("Graph with the coefficients found by Newton-Raphson")
    pl.grid(True)
    pl.show()
grafica()
