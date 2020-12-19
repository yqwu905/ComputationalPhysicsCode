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
        self.x = np.linspace(1,self.nx,self.nx)*self.dx
    def update(self):
        self.u[1:-1] += self.alpha*(self.u[2:] + self.u[:-2] - 2*self.u[1:-1])
    def calculate(self, savefig = False):
        img_num = 0
        for i in tqdm(range(self.nt)):
            self.update()
            if savefig and (i%int(self.nt/100)==0):
                plt.clf()
                #plt.ylim(-1.1,1.1)
                plt.title("$\\beta={},t={:.2f}$".format(self.alpha,self.dt*i))
                plt.plot(self.x, self.u)
                plt.savefig("./img/{}.jpg".format(img_num))
                img_num += 1
    def snapshot(self):
        plt.ylim(-1.1,1.1)
        plt.plot(self.x, self.u)
        plt.show()

h = heat(0.5,0.1,0.0101,100,1000,45,55)
h.calculate(True)