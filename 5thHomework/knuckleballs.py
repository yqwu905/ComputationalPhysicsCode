from vpython import *

g = 9.8

class simpleBall():
    def __init__(self, x0 = 0, y0 = 0, z0 = 1.5, vx0 = 10, vy0 = 0, vz0 = 5, dt = 0.01):
        assert z0 > 0, "Error: Positive z0 was expected, not {}.".format(z0)
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
            self.vy.append(self.vy[-1])
            self.vz.append(self.vy[-1] - g * self.dt)
            self.x.append(self.x[-1] + self.dt * self.vx[-1])
            self.y.append(self.y[-1] + self.dt * self.vy[-1])
            self.z.append(self.z[-1] + self.dt * self.vz[-1])
            if self.z[-1] <= 0:
                break
    def show(self):
        scene = canvas(x=0, y=0, width=600, height=600, title='Walk3D')
        c = curve()
        for i in range(1, len(self.t)):
            c.append(vector(self.x[i-1], self.y[i-1],self.z[i-1]),vector(self.x[i], self.y[i],self.z[i]))
            rate(100)

s = simpleBall()
s.calc()
s.show()