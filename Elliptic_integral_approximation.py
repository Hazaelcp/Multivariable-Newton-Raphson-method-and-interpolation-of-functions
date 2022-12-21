from scipy.integrate import quad
from numpy import *
from math import*

def K(t):
    return 1/(sqrt(1-(sin(t)/2)**2))


def E(t):
    return (sqrt(1-(sin(t)/2)**2))

#Trapecio
def trapezoide(f,ini,fin,n):
    h=(fin-ini)/(n-1)   
    suma=(f(ini)+f(fin))/2     
    for i in range(1,n-1):
        suma+=f(ini+i*h)
    suma=h*suma
    print("Using the trapezoid rule\n")
    print(f'\t integral(1/2)={suma}')
    
    i=quad(f,0,pi/2)
    print(f'\t Scipy integral value(1/2)={i[0]}')
    error=abs((suma-i[0])/i[0])*100
    print(f'\t The error is {error}%')
    
    
#simpson
def simpson(f,ini,fin,n):
    h=(fin-ini)/(n-1)
    suma=f(ini)+f(fin)
    for i in range(1,n-1):
        if i%2==0:
            suma+=2*f(ini+h*i)
        else:
            suma+=4*f(ini+h*i)
    
    suma=(h/3)*suma
    print("Using Simpson's rule \n")
    print(f'\t integral(1/2)={suma}')
    i=quad(f,0,pi/2)
    print(f'\t Scipy integral value(1/2)={i[0]}')
    error=abs((suma-i[0])*100/i[0])
    print(f'\t El error es: {error}%')


print('VALUE OF THE ELLIPTIC INTEGRAL K(1/2)')
trapezoide(K,0,pi/2,1000)
simpson(K,0,pi/2,1001)

print('\n\n\n\n\n\VALUE OF THE ELLIPTIC INTEGRAL E(1/2)')
trapezoide(E,0,pi/2,1000)
simpson(E,0,pi/2,1001)

