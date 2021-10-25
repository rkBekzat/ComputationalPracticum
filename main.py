import math

import numpy as np
import matplotlib.pyplot as plt
import cmath

from errors import Error
from methods.eulers import Euler
from methods.improved_euler import ImprovedEuler
from methods.runge_kutta import RungeKutta

def y(x):
    return 2*(2*math.sqrt(x)+x+2)



x0=int(input("enter the initial x0:"))
y0=int(input("enter the initial y0:"))
X=int(input("enter the finish point X:"))
N=int(input("enter the number of points N:"))
x=np.linspace(x0, X, N)
h=(X-x0+1)/N
exact=list()
methods = [Euler(x0, y0, X, h, y), ImprovedEuler(x0, y0, X, h, y), RungeKutta(x0, y0, X, h, y)]
for i in x:
    exact.append(y(i))
fig, axs=plt.subplots(3)
l1=list()
l2=list()
l3=list()
for i in range(3):
    er = Error(exact, methods[i].Solve(), methods[i].name)
    l1.append(axs[0].plot(x, methods[i].Solve(), methods[i].color))
    l2.append(axs[1].plot(x, er.LTE(x0, X, h), methods[i].color))
    l3.append(axs[2].plot(x, er.GTE(), methods[i].color))
    axs[i].grid(True)

axs[0].legend((l1[0], l1[1], l1[2]), (methods[0].name, methods[1].name, methods[2].name), loc='upper right', shadow=True)
axs[1].legend((l2[0], l2[1], l2[2]), (methods[0].name, methods[1].name, methods[2].name), loc='upper right', shadow=True)
axs[1].legend((l3[0], l3[1], l3[2]), (methods[0].name, methods[1].name, methods[2].name), loc='upper right', shadow=True)
axs[0].set_title("Exact")
axs[1].set_title("Local Errors")
axs[2].set_title("Global Errors")
plt.show()

#y=2x+4\sqrt{x}+4