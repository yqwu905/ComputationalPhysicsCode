from vpython import *
import math

g = 9.8
zoomFactor = 100
airDensity = 1.293

class simpleBall():
    def __init__(self, x0 = 0, y0 = 1.5, z0 = 0, vx0 = 10, vy0 = 15, vz0 = 0, dt = 0.001):
        assert y0 > 0, "Error: Positive y0 was expected, not {}.".format(y0)
        self.dt = dt
        self.t = [0]
        self.x = [x0]
        self.y = [y0]
        self.z = [z0]
        self.vx = [vx0]
        self.vy = [vy0]
        self.vz = [vz0]
    def calc(self):
        while True:
            self.t.append(self.t[-1] + self.dt)
            self.vx.append(self.vx[-1])
            self.vy.append(self.vy[-1] - g * self.dt)
            self.vz.append(self.vz[-1])
            self.x.append(self.x[-1] + self.dt * self.vx[-1])
            self.y.append(self.y[-1] + self.dt * self.vy[-1])
            self.z.append(self.z[-1] + self.dt * self.vz[-1])
            if self.y[-1] <= 0:
                break
    def trajectoryShow(self):
        xmax = max([max(self.x)*zoomFactor,1500])
        ymax = max([max(self.y)*zoomFactor,1500])
        zmax = max([max(self.z)*zoomFactor,1500])
        scene = canvas(x=0, y=0, width=600, height=600, title="Ball's trajectory")
        xax   = curve(x=list(range(0,1500)), color=color.red, pos=[vector(0,0,0),vector(xmax,0,0)], radius=10.)
        yax   = curve(x=list(range(0,1500)), color=color.red, pos=[vector(0,0,0),vector(0,ymax,0)], radius=10.)
        zax   = curve(x=list(range(0,1500)), color=color.red, pos=[vector(0,0,0),vector(0,0,zmax)], radius=10.)
        xname = label( text = "X", pos = vector(1000, 150,0), box=0)
        yname = label( text = "Y", pos = vector(-100,1000,0), box=0)
        zname = label( text = "Z", pos = vector(100, 0,1000), box=0)
        xmaxName = label(text = '{}'.format(int(xmax)),pos = vector(xmax,0,0), box = 0)
        ymaxName = label(text = '{}'.format(int(ymax)),pos = vector(0,ymax,0), box = 0)
        zmaxName = label(text = '{}'.format(int(zmax)),pos = vector(0,0,zmax), box = 0)
        c = curve(x=list(range(0, len(self.t))),radius=10.0,color=color.yellow)
        for i in range(len(self.t)):
            c.append(vector(self.x[i]*zoomFactor, self.y[i]*zoomFactor,self.z[i]*zoomFactor))
            rate(int(1/self.dt))
    def realtimeShow(self):
        scene = canvas(x=0, y=0, width=600, height=600, title="Ball's real time show")
        ball = sphere(radius = 2, texture=textures.wood, make_trail = True)
        for i in range(len(self.t)):
            ball.pos = vector(self.x[i],self.y[i],self.z[i])
            rate(int(1/self.dt))
    
class resistanceBall(simpleBall):
    def __init__(self, vwindx = -1, vwindy = 0, vwindz = 0, mass = 0.149,vd = 35,delta = 5):
        super().__init__()
        self.vwx = vwindx
        self.vwy = vwindy
        self.vwz = vwindz
        self.m = mass
        self.vd = vd
        self.delta = delta
    def calc(self):
        while True:
            v = math.sqrt(self.x[-1]**2 + self.y[-1]**2 + self.z[-1]**2)
            dv = math.sqrt((self.x[-1] - self.vwx)**2 + (self.y[-1] - self.vwy)**2 + (self.z[-1] - self.vwz)**2)
            self.t.append(self.t[-1] + self.dt)
            self.vx.append(self.vx[-1] - self.m * (0.0039 + 0.0058/(1 + math.exp(v - self.vd)/self.delta)) * dv * (self.vx[-1] - self.vwx)*self.dt)
            self.vy.append(self.vy[-1] - g * self.dt - self.m * (0.0039 + 0.0058/(1 + math.exp(v - self.vd)/self.delta)) * dv * (self.vy[-1] - self.vwy)*self.dt)
            self.vz.append(self.vz[-1] - self.m * (0.0039 + 0.0058/(1 + math.exp(v - self.vd)/self.delta)) * dv * (self.vz[-1] - self.vwz)*self.dt)
            self.x.append(self.x[-1] + self.dt * self.vx[-1])
            self.y.append(self.y[-1] + self.dt * self.vy[-1])
            self.z.append(self.z[-1] + self.dt * self.vz[-1])
            if self.y[-1] <= 0:
                break

class spinResistanceBall(resistanceBall):
    def __init__(self, omega = 10, s0 = 0.00041):
        super().__init__()
        self.omega = omega
        self.angle = [0]
        self.s0 = self.m * s0
    def calc(self):
        while True:
            v = math.sqrt(self.vx[-1]**2+self.vy[-1]**2+self.vz[-1]**2)
            fm = self.s0 * self.omega * v * math.sqrt(self.vx[-1]**2 + self.vy[-1]**2)/v
            theta = math.atan(self.vz[-1]/self.vx[-1])
            fmx = fm*math.sin(theta)
            fmz = - fm * math.cos(theta)
            alateral = g * (sin(4*self.angle[-1])-0.25*sin(8*self.angle[-1])+0.08*sin(12*self.angle[-1])-0.025*sin(16*self.angle[-1]))
            v = math.sqrt(self.x[-1]**2 + self.y[-1]**2 + self.z[-1]**2)
            dv = math.sqrt((self.x[-1] - self.vwx)**2 + (self.y[-1] - self.vwy)**2 + (self.z[-1] - self.vwz)**2)
            self.t.append(self.t[-1] + self.dt)
            self.vx.append(self.vx[-1] - self.m * (0.0039 + 0.0058/(1 + math.exp(v - self.vd)/self.delta)) * dv * (self.vx[-1] - self.vwx)*self.dt + fmx/self.m * self.dt)
            self.vy.append(self.vy[-1] - g * self.dt - self.m * (0.0039 + 0.0058/(1 + math.exp(v - self.vd)/self.delta)) * dv * (self.vy[-1] - self.vwy)*self.dt)
            self.vz.append(self.vz[-1] - self.m * (0.0039 + 0.0058/(1 + math.exp(v - self.vd)/self.delta)) * dv * (self.vz[-1] - self.vwz)*self.dt + fmz/self.m * self.dt)
            self.x.append(self.x[-1] + self.dt * self.vx[-1])
            self.y.append(self.y[-1] + self.dt * self.vy[-1])
            self.z.append(self.z[-1] + self.dt * self.vz[-1])
            self.angle.append(self.angle[-1] + self.omega * self.dt)
            if self.y[-1] <= 0:
                break
    def realtimeShow(self):
        scene = canvas(x=0, y=0, width=600, height=600, title="Ball's real time show")
        ball = sphere(radius = 2, texture=textures.wood, make_trail = True)
        for i in range(len(self.t)):
            ball.pos = vector(self.x[i],self.y[i],self.z[i])
            if i >= 1:
                ball.rotate(angle = self.angle[i] - self.angle[i-1], axis = vec(0,1,0), origin = ball.pos)
            rate(int(1/self.dt))


r = spinResistanceBall()
r.calc()
r.trajectoryShow()
r.realtimeShow()