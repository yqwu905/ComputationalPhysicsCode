import numpy as np
from Q1 import CapcitorSolver
from scipy.sparse import lil_matrix
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

class sparseMatrixCapcitorSolver(CapcitorSolver):
    def __init__(self, geometry = [(-1,-1),(1,1)], meshLeng = 0.05, relaxError = 0.002):
        super().__init__(geometry, meshLeng, relaxError)
        print("Common matrix occupied {} bytes of memory.".format(self.v.__sizeof__()))
        self.v[0,:] = 0
        self.v[-1,:] = 0
        self.v[:,0] = 0
        self.v[:,-1] = 0
        self.v[int(self.size[0]/3), int(self.size[1]/4):int(self.size[1]*3/4)] = 1
        self.v[int(self.size[0]*2/3), int(self.size[1]/4):int(self.size[1]*3/4)] = -1
        self.v = lil_matrix(self.v)
        print("Sparse matrix occupied {} bytes of memory.".format(self.v.__sizeof__()))
    def show(self):
        X = np.arange(self.geo[0][0], self.geo[1][0], self.dl)
        Y = np.arange(self.geo[0][1], self.geo[1][1], self.dl)
        X, Y = np.meshgrid(X, Y)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X, Y, self.v.toarray(),cmap=cm.coolwarm,linewidth=0, antialiased=False)
        fig.colorbar(surf)
        plt.show()   

if __name__ == '__main__':
    s = sparseMatrixCapcitorSolver(meshLeng=0.0001)

