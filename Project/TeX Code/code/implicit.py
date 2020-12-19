import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class heat():
    def __init__(self, k, dx, dt, nx, totT, x1, x2):
        self.dx = dx
        self.dt = dt
        self.nx = nx
        self.nt = int(totT/dt)
        self.u = np.zeros(nx)
        self.u[x1:x2] = 1
        self.alpha = k*dt/(dx**2)
        print(self.alpha)
        self.x = np.linspace(1,self.nx,self.nx)*self.dx
        self.M = np.eye(nx)*-2
        for i in range(nx):
            if i != 0:
                self.M[i][i-1] = 1
            if i != (nx-1):
                self.M[i][i+1] = 1
        self.M = np.linalg.inv(np.eye(self.nx)-self.alpha*self.M)
    def update(self):
        self.u = np.dot(self.M, self.u)
        #print(self.u)
    def calculate(self, savefig = False):
        img_num = 0
        for i in tqdm(range(self.nt)):
            self.update()
            if savefig and (i%int(self.nt/100)==0):
                plt.clf()
                plt.ylim(-1.1,1.1)
                plt.title("$\\beta={},t={:.2f}$".format(self.alpha,self.dt*i))
                plt.plot(self.x, self.u)
                plt.savefig("./img/{}.jpg".format(img_num))
                img_num += 1
    def snapshot(self):
        plt.ylim(-1.1,1.1)
        plt.plot(self.x, self.u)
        plt.show()


h = heat(0.5,0.1,1,1000,1000,450,550)
h.calculate(True)