#Interpolacion Via Splines Cubicos
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as pl
import numpy as np

x = np.array([0,25,50,75,100,125,150,175,200])
y = np.array([10.6,16.0,45.0,83.5,52.8,19.9,10.8,8.25,4.7])

cs = CubicSpline(x, y)
xs = np.arange(0,200,0.05)


#linea vertical
ly=np.linspace(0,83.631,5)
lx=np.ones(len(ly))*76.2001

#liena Horizontal
vx=np.linspace(48.19742,106.6057,5)
vy=np.ones(len(vx))*(83.631/2)


fig, ax = pl.subplots()
ax.plot(x, y, 'ro',label='Experimental data \n')
ax.plot(lx,ly,'r',linestyle='dashdot',label='Resonance energy \nEr=76.2001 Mev\n')
ax.plot(xs, cs(xs),'k',linewidth=0.9,label='Interpolation by\ncubic splines\n')
ax.plot(48.19742,83.631/2,'bo',label='Er-Γ/2')
ax.plot(106.6057,83.631/2,'co',label='Er+Γ/2')
ax.plot(vx,vy,'b',linestyle='dotted')



legend = ax.legend(loc='upper right', shadow=True, fontsize='small')
pl.title("Interpolation by cubic splines")
pl.grid(True)
pl.show()


