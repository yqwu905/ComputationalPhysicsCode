from Q1 import multiBodiesSolver
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

G = 6.67259*10**-11
Ms = 1.9891*10**30
Mj = 1.90*10**27
Me = 5.95*10**24
Lsj = 7.7833*10**11
Lse = 1.496*10**11

c1 = 6.612*10**24
h = 2.3

class multiBodiesSolverWithHeat(multiBodiesSolver):
    def calcTemp(self,sunIdx, earthIdx):
        T = h
        for i in sunIdx:
            r2 = np.power(self.x[:,i] - self.x[:,earthIdx], 2) + np.power(self.y[:,i] - self.y[:,earthIdx], 2)
            T += c1/r2
        plt.plot(self.t,T,label = 'Temperature')
        plt.xlabel('t/s')
        plt.ylabel('T/K')
        plt.title('10x$M_J$T-t')
        plt.show()

a = sqrt(2)/2

s = multiBodiesSolverWithHeat(6000,[Ms,Me,Mj],[(0,0),(Lse,0),(Lsj,0)],[(0,0),(0,30000),(0,13070)],['Sun','Earth','Jupiter'])
#s.setTotalPToZero(0)
s.calculate(365*24*3600)
s.showResult()
s.calcTemp([0,2],1)
