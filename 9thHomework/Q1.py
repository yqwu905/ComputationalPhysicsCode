import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy.fft as nf

def sinFunctionGenerate(x):
    return np.sin(10*np.pi*x)

def gaussPack(x):
    x0 = 0.4
    k = 1000
    return np.exp(-k*np.power((x-x0),2))

def squareWaveGenerate(x):
    ampl = 1.0
    wide = 0.1
    x0 = x[0]
    flag = 1
    y = np.zeros(x.__len__())
    for i in range(x.__len__()):
        if x[i] - x0 > wide:
            print('ddd')
            x0 = x[i]
            flag = flag*-1
        y[i] = flag*ampl
    return y


class waveOnString():
    def __init__(self, c = 5, dt = 0.001, dx = 0.005, waveGenerator = sinFunctionGenerate, l = 1, t0 = 5, waveRange = [0,1/4]):
        self.x = np.arange(0,l,dx)
        self.y = np.zeros(int(l/dx))
        self.newy = self.y.copy()
        self.y[int(waveRange[0]/dx):int(waveRange[1]/dx)] = waveGenerator(self.x[int(waveRange[0]/dx):int(waveRange[1]/dx)])
        self.lasty = self.y.copy()
        self.r = c*dt/dx
        self.t0 = t0
        self.l = l
        self.dt = dt
        self.dx = dx
        self.t = 0
    def __update(self):
        self.y[0] = self.y[1]
        self.y[-1] = 0
        self.newy[1:-1] = 2*(1-self.r**2)*self.y[1:-1] - self.lasty[1:-1] + self.r**2*(self.y[2:]+self.y[:-2])
        self.lasty = self.y.copy()
        self.y = self.newy.copy()
        self.t += self.dt
    def __animaInit(self):
        self.ln.set_data(self.x,self.y)
        return self.ln,
    def __animeUpdate(self,frame):
        print(np.mean(self.y))
        self.ln.set_data(self.x,self.y)
        self.__update()
        return self.ln,
    def animate(self):
        fig,ax = plt.subplots()
        self.ln, = plt.plot(self.x, self.y)
        anim = animation.FuncAnimation(fig,self.__animeUpdate, frames=np.linspace(0,self.t0,int(self.t0/self.dt)), interval = 100, init_func = self.__animaInit, blit = True)
        plt.show()
    def freqSpec(self, x = None):
        if x == None:
            x = np.mean(self.x)
        index = int(x/self.dx)
        t = [0]
        a = [self.y[index]]
        for i in np.arange(0,self.t0,self.dt):
            self.__update()
            t.append(t[-1] + self.dt)
            a.append(self.y[index])
        t, a = np.array(t), np.array(a)
        plt.subplot(121)
        plt.plot(t,a)
        plt.title("Signal at $x = {}$".format(x))
        plt.subplot(122)
        comp_arr = nf.fft(a)
        freqs = nf.fftfreq(a.size, t[1] - t[0])
        pows = np.abs(comp_arr)
        plt.grid()
        plt.plot(freqs[freqs > 0], pows[freqs > 0])
        plt.title("Frequency")
        plt.show()


w = waveOnString(dt = 0.0001, dx = 0.0005, waveGenerator=squareWaveGenerate)
w.freqSpec(x = 0.95)
