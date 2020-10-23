import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from math import pi,sin
from multiprocessing import Pool

g = 9.8

class pendulum():
    def __init__(self,l = 9.8,Fd =1.44,omegad = 2/3.0,dt = 0.001, q = 0.5, theta0 = 0.2):
        self.l = l
        self.Fd = Fd
        self.omegad = omegad
        self.dt = dt
        self.q = q
        self.theta0 = theta0
    def calculate(self, t0 = 50):
        self.theta = []
        self.omega = []
        self.t = []
        k = g/self.l
        w = 0
        a = self.theta0
        t_ = 0
        while t_ <= t0:
            self.omega.append(w)
            self.theta.append(a)
            self.t.append(t_)
            w += (-k*sin(a)-self.q*w+self.Fd*sin(self.omegad*t_)) * self.dt
            a += w * self.dt
            if a > pi:
                a -= 2*pi
            elif a < -pi:
                a += 2*pi
            t_ += self.dt
    def showTrajectory(self):
        plt.subplot(1,2,1)
        plt.plot(self.t, self.theta)
        plt.title('$\\theta$-t Figure')
        plt.subplot(1, 2, 2)
        plt.plot(self.t, self.omega)
        plt.title('$\\omega$-t Figure')
        plt.show()
    def __animeInit(self):
        self.ax.set_xlim(min(self.theta), max(self.theta))
        self.ax.set_ylim(min(self.omega), max(self.omega))
        self.text_pt.set_position((min(self.theta), min(self.omega)))
        return self.ln,self.text_pt,
    def __animeUpdate(self, frame):
        self.xdata.append(self.theta[frame])
        self.ydata.append(self.omega[frame])
        self.ln.set_data(self.xdata, self.ydata)
        self.point.set_data(self.theta[frame], self.omega[frame])
        self.text_pt.set_text("t=%.3f"%(self.t[frame]))
        return self.ln,self.point,self.text_pt,
    def showPhaseGraph(self):
        plt.plot(self.theta, self.omega)
        plt.show()
    def animePahseGraph(self):
        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []
        self.ln, = plt.plot([], [])
        self.point, = plt.plot(self.theta[0], self.omega[0],"ro")
        self.text_pt = plt.text(0, 0, '', fontsize=16)
        ani = FuncAnimation(self.fig, self.__animeUpdate, frames=range(len(self.t)),
                    init_func=self.__animeInit, blit=True, interval = 10)
        plt.show()
    def PoincareSection(self, isShow = True, waiting = 0):
        x = []
        y = []
        for i in range(len(self.t)):
            if self.t[i] > 2*pi/self.omegad*waiting:
                if abs(round(self.t[i]/(2*pi/self.omegad)) - (self.t[i]/(2*pi/self.omegad))) < 0.001:
                    x.append(self.theta[i])
                    y.append(self.omega[i])

        self.PoincareSectionX = x
        self.PoincareSectionY = y
        if isShow:
            plt.scatter(x,y,s=5)
            plt.show()
    def bifurcationDiagram(self):
        x,y,cx,cy = [],[],[],[]
        for fd in np.linspace(1.35,1.48,200):
            self.Fd = fd
            self.calculate(800*pi/self.omegad + 2)
            index = int((600*pi/self.omegad)/self.dt)
            flag = 600*pi
            for i in range(index, len(self.t)):
                if (self.omegad * self.t[i] - flag - 2 * pi) > 0:
                    if np.abs(self.omegad * self.t[i - 1] - flag) < np.abs(self.omegad * self.t[i] - flag):
                        x.append(fd)
                        y.append(self.theta[i - 1])
                    else:
                        x.append(fd)
                        y.append(self.theta[i])
                    flag += 2*pi
            y_ = np.array(y)
            x_ = np.array(x)
            index_ = x_ == fd
            ylist = y_[index_]
            li = [{'c':ylist[0],'list':[ylist[0]]}]
            for i in ylist[1:]:
                cflag = False
                for j in range(len(li)):
                    if np.abs(i - li[j]['c']) < 0.1:
                        cflag = True
                        s_ = li[j]['list']
                        s_.append(i)
                        li[j] = {'c':np.mean(s_),'list':s_}
                if not cflag:
                    li.append({'c':i,'list':[i]})
            print(fd, len(li))
            for i in li:
                cx.append(fd)
                cy.append(i['c'])
        plt.scatter(x,y,s = 5)
        plt.scatter(cx,cy,color='red', s = 8)
        plt.title("$\Omega_d$={}, dt={}".format(self.omegad,self.dt))
        #plt.show()
        plt.savefig("./{}-{}.png".format(self.omegad, self.dt))

def main():
    wdList = np.linspace(1/5, 2, 16)
    pList = []
    pool = Pool(processes=8)
    for i in range(len(wdList)):
        pList.append(pendulum(omegad=wdList[i]))
        pool.apply_async(pList[i].bifurcationDiagram)
    print('Submit success!')
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()

'''
p = pendulum(dt = 0.01,omegad = 1/3.0)
p.bifurcationDiagram()
'''
'''
plt.subplot(1,3,1)
plt.xlim(-0,3)
plt.ylim(-3,3)
p1 = pendulum(Fd = 1.4)
p1.calculate(5000)
p1.PoincareSection(False, waiting=300)
plt.scatter(p1.PoincareSectionX, p1.PoincareSectionY)
plt.title('$F_d$ = 1.44')

plt.subplot(1,3,2)
plt.xlim(-0,3)
plt.ylim(-3,3)
p1 = pendulum(Fd = 1.44)
p1.calculate(5000)
p1.PoincareSection(False, waiting=300)
plt.scatter(p1.PoincareSectionX, p1.PoincareSectionY)
plt.title('$F_d$ = 1.44')


plt.subplot(1,3,3)
plt.xlim(-0,3)
plt.ylim(-3,3)
p1 = pendulum(Fd = 1.465)
p1.calculate(5000)
p1.PoincareSection(False, waiting=300)
plt.scatter(p1.PoincareSectionX, p1.PoincareSectionY)
plt.title('$F_d$ = 1.456')

plt.show()
'''




#p.showTrajectory()
#p.showPhaseGraph()
#p.animePahseGraph()
#p.PoincareSection()
#p.bifurcationDiagram()