import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import random
from sympy import symbols, diff, N

def fun(X, Y):
    return 2*(np.exp(-X**2 - Y**2))# - np.exp(-(X - 1)**2 - (Y - 1)**2))

def symfun(X, Y):
    return 2*(np.exp(1)**(-X**2 - Y**2))# - np.exp(1)**(-(X - 1)**2 - (Y - 1)**2))

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = fun(X, Y)
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Simplest default with labels')

o=[(random.random()-0.5)*4, (random.random()-0.5)*4]
x, y = symbols('x y', real=True)
dx=diff(symfun(x, y), x)
dy=diff(symfun(x,y), y)
d=[dx.subs({x:o[0], y:o[1]}), dy.subs({x:o[0], y:o[1]})]
alpha=0.7
i=0
while bool((d[0]**2+d[1]**2)>=1e-4) and i<1000:
    d=[dx.subs({x:o[0], y:o[1]}), dy.subs({x:o[0], y:o[1]})]
    no=[o[0]+d[0]*alpha, o[1]+d[1]*alpha]
    #plt.plot(np.array([o[0], no[0]]), np.array([o[1], no[1]]), color="#"+hex(i)[2:]+""+hex(i)[2:]+""+hex(i)[2:])
    plt.plot(o[0], o[1], color="#"+hex(i%(256-16)+16)[2:]+""+hex(i%(256-16)+16)[2:]+""+hex(i%(256-16)+16)[2:], marker='o')
    o=no
    i+=1

plt.plot(o[0], o[1], color="#"+hex(i%(256-16)+16)[2:]+""+hex(i%(256-16)+16)[2:]+""+hex(i%(256-16)+16)[2:], marker='o')

plt.show()
