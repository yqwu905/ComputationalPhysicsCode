import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


G = 15
Ms = 1.9891*10**30
Mj = 1.90*10**27
Me = 5.95*10**24
Lsj = 7.7833*10**11
Lse = 1.496*10**11


class multiBodiesSolver():
    def __init__(self, dt, mass, coords, velocs, name):
        self.__n = len(mass)
        self.__mass = np.array(mass)
        self.__x0 = []
        self.__y0 = []
        self.__idx = np.array(range(self.__n))
        for i in coords:
            self.__x0.append(i[0])
            self.__y0.append(i[1])
        self.__vx0 = []
        self.__vy0 = []
        for i in velocs:
            self.__vx0.append(i[0])
            self.__vy0.append(i[1])
        self.__dt = dt
        self.__name = name
    def setTotalPToZero(self, idx):
        totPx = np.sum(self.__mass * self.__vx0)
        totPy = np.sum(self.__mass * self.__vy0)
        self.__vx0[idx] -= totPx / self.__mass[idx]
        self.__vy0[idx] -= totPy / self.__mass[idx]
    def __Solver(self, idx):
        x,y = self.x[idx - 1], self.y[idx - 1]
        for i in range(self.__n):
            oIdx = (self.__idx != i)
            r3 = np.power(np.sqrt(np.power(x[oIdx] - x[i],2) + np.power(y[oIdx] - y[i],2)),3)
            self.vx[idx][i] = self.vx[idx - 1][i] + np.sum(G * self.__dt * self.__mass[oIdx]*(x[oIdx] - x[i])/r3)
            self.vy[idx][i] = self.vy[idx - 1][i] + np.sum(G * self.__dt * self.__mass[oIdx]*(y[oIdx] - y[i])/r3)
        self.x[idx] = self.x[idx - 1] + self.vx[idx] * self.__dt
        self.y[idx] = self.y[idx - 1] + self.vy[idx] * self.__dt
        self.t.append(self.t[-1] + self.__dt)
    def showSystemInfo(self, idx):
        x,y = self.x[idx], self.y[idx]
        totV = 0
        totK = np.sum(0.5*self.__mass * (np.power(self.__vx0, 2) + np.power(self.__vy0, 2)))
        totPx = np.sum(self.__mass * self.__vx0)
        totPy = np.sum(self.__mass * self.__vy0)
        for i in range(self.__n):
            oIdx = (self.__idx != i)
            r = np.sqrt(np.power(x[oIdx] - x[i],2) + np.power(y[oIdx] - y[i],2))
            totV += -0.5 * G * np.sum(self.__mass[i] * self.__mass[oIdx] / r)
        print("总动能:%e\t总势能%e\t总能量:%e\tx方向动量:%e\ty方向动量:%e\t总动量:%e"%(totK, totV, totV + totK, totPx, totPy, np.sqrt(totPx**2 + totPy**2)))
    def calculate(self, t0 = 50000):
        n = int(t0/self.__dt) + 1
        self.t = [0]
        self.x = np.zeros((n,self.__n))
        self.y = np.zeros((n,self.__n))
        self.vx = np.zeros((n,self.__n))
        self.vy = np.zeros((n,self.__n))
        self.x[0], self.y[0], self.vx[0], self.vy[0] = self.__x0, self.__y0, self.__vx0, self.__vy0
        for i in tqdm(range(1, n)):
            self.__Solver(i)
        self.showSystemInfo(0)
        self.showSystemInfo(n - 1)
    def showResult(self, typec = 0):
        totM = np.sum(self.__mass)
        cx = np.mean(self.__mass*self.x, axis = 1)/totM
        cy = np.mean(self.__mass*self.y, axis = 1)/totM
        plt.scatter(cx,cy,label = 'Mass Center', s = 1)
        for i in range(self.__n):
            plt.scatter(self.x[:,i], self.y[:,i], label = self.__name[i], s = 1)
        plt.legend()
        plt.show()
            
if __name__ == '__main__':
    s = multiBodiesSolver(600,[Ms,Me,Mj],[(0,0),(Lse,0),(Lsj,0)],[(0,0),(0,30000),(0,13070)],['Sun','Earth','Jupiter'])
    #s.setTotalPToZero(0)
    s.calculate(100*365*24*3600)
    #s.showResult()
    