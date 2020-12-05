import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm

class MD():
    def __init__(self, L, N, T, dt, sigma, epsilon, v0, rCutOff):
        self.L, self.N, self.T, self.dt, self.sigma, self.epsilon, self.v0, self.rCutOff = L, N, T, dt, sigma, epsilon, v0, rCutOff
        NP = int(math.sqrt(L))
        if NP != int(NP):
            NP += 1
        scale = L/(NP+1)
        self.v = []
        self.x, self.y = [],[]
        v = np.random.normal(loc = v0, scale = 1.0, size = N)
        for i in range(N):
            self.x.append([])
            self.y.append([])
            self.x[i].append(scale * (i%NP + 1))
            self.y[i].append(scale * (int(i/NP) + 1))
            theta = np.random.random(1)[0]*2*np.pi
            self.x[i].append(self.x[i] + np.cos(theta)*v[i]*dt)
            self.y[i].append(self.y[i] + np.sin(theta)*v[i]*dt)
    def dist(self,x1,x2,y1,y2):
        v1 = np.array([x2,y2])
        vList = [np.array([x1,y1]),np.array([self.L - x1, y1]),np.array([x1, self.L - y1]),np.array([self.L - x1, self.L - y1])]
        rMin, theta = float("inf"), 0
        for i in vList:
            print(i)
            v = v1 - i
            r = np.linalg.norm(v)
            if r < rMin:
                rMin = r
                theta = np.arccos(v[0]/r)
        return rMin, theta
    def update(self):
        totFx,totFy = [],[]
        self.v.append(0)
        for i in range(self.N):
            totFx.append(0)
            totFy.append(0)
            for j in range(self.N):
                if i==j:
                    continue
                r,theta = self.dist(self.x[i][-1], self.y[i][-1], self.x[j][-1], self.y[j][-1])
                if r > self.rCutOff:
                    continue
                f = 24*(2/r**13 - 1/r**7)
                totFx[i] += f*np.cos(theta)
                totFy[i] += f*np.sin(theta)
        for i in range(self.N):
            self.x[i].append(2*self.x[i][-1]-self.x[i][-2] + totFx[i]*self.dt**2)
            self.y[i].append(2*self.y[i][-1]-self.y[i][-2] + totFy[i]*self.dt**2)
            self.v.append(np.linalg.norm)
            if self.x[i][-1] < 0:
                self.x[i][-1] = int(self.x[i][-1]/self.L)*self.L - self.x[i][-1]
            if self.x[i][-1] > self.L:
                self.x[i][-1] = self.x[i][-1] - int(self.x[i][-1]/self.L)*self.L - self.L
            if self.y[i][-1] < 0:
                self.y[i][-1] = int(self.y[i][-1]/self.L)*self.L - self.y[i][-1]
            if self.y[i][-1] > self.L:
                self.y[i][-1] = self.y[i][-1] - int(self.y[i][-1]/self.L)*self.L - self.L
    def calculate(self):
        NUM = int(self.T/self.dt)
        for i in tqdm(range(NUM)):
            self.update()
    def show(self):
        plt.xlim(0,self.L)
        plt.ylim(0,self.L)
        for i in range(self.N):
            plt.plot(self.x[i], self.y[i])
            plt.scatter(self.x[i], self.y[i], s = 5)
        plt.show()


if __name__ == '__main__':
    m = MD(10,20,1,0.01,1,1,1,3)
    m.calculate()
    m.show()