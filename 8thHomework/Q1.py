import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


class CapcitorSolver():
    def __init__(self, geometry = [(-1,-1),(1,1)], meshLeng = 0.05, relaxError = 0.01):
        self.geo = geometry
        self.size = (int((self.geo[1][0] - self.geo[0][0])/meshLeng), int((self.geo[1][1] - self.geo[0][1])/meshLeng))
        self.dl = meshLeng
        self.v = np.zeros(self.size)
        self.r = relaxError
    def __boundaryCondition(self):
        self.v[0,:] = 0
        self.v[-1,:] = 0
        self.v[:,0] = 0
        self.v[:,-1] = 0
        self.v[int(self.size[0]/3), int(self.size[1]/4):int(self.size[1]*3/4)] = 1
        self.v[int(self.size[0]*2/3), int(self.size[1]/4):int(self.size[1]*3/4)] = -1
    def __update(self):
        new = (self.v[0:-2, 1:-1] + self.v[2:, 1:-1] + self.v[1:-1,2:] + self.v[1:-1,0:-2])/4
        deltaV = np.sum(np.abs(new - self.v[1:-1,1:-1]))
        print(deltaV)
        self.v[1:-1,1:-1] = new
        if deltaV > self.r:
            return False
        else:
            return True
    def calc(self):
        flag = False
        while not flag:
            self.__boundaryCondition()
            flag = self.__update()
    def show(self):
        X = np.arange(self.geo[0][0], self.geo[1][0], self.dl)
        Y = np.arange(self.geo[0][1], self.geo[1][1], self.dl)
        X, Y = np.meshgrid(X, Y)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X, Y, self.v,cmap=cm.coolwarm,linewidth=0, antialiased=False)
        fig.colorbar(surf)
        plt.show()   

if __name__ == '__main__':
    c = CapcitorSolver()
    c.calc()
    c.show()
