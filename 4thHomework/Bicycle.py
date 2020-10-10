import matplotlib.pyplot as plt

class bicycle():
    def __init__(self, power = 10, mass = 1, timeStep = 0.1, totalTime = 20, v0 = 1):
        self.v = [v0]
        self.t = [0]
        self.m = mass
        self.p = power
        self.dt = timeStep
        self.time = totalTime
    def run(self):
        _time = 0
        while(_time < self.time):
            self.v.append(self.v[-1] + self.dt * self.p / (self.m * self.v[-1]))
            self.t.append(_time)
            _time += self.dt
    def showResult(self):
        plt.plot(self.t, self.v, label = 'velocity with time')
        plt.xlabel('time($s$)')
        plt.ylabel('velovity')
        plt.title('Bicycling velocity with time')
        plt.legend()
        plt.show()

class bicycleWithResistance(bicycle):
    def __init__(self, C = 1, rho = 1, A = 1):
        super().__init__()
        self.C = C
        self.rho = rho
        self.A = A
    def run(self):
        _time = 0
        while(_time < self.time):
            self.v.append(self.v[-1] + self.dt * self.p / (self.m * self.v[-1]) - (self.C * self.rho * self.A * self.v[-1]**2)/(2*self.m)*self.dt)
            self.t.append(_time)
            _time += self.dt


class bicycleWeNeed(bicycleWithResistance):
    def __init__(self, vStar = 7):
        super().__init__()
        self.v0 = 0
        self.vStar = vStar
    def run(self):
        _time = 0
        f0 = self.p / self.vStar
        while _time < self.time:
            if self.v[-1] < self.vStar:
                self.v.append(self.v[-1] + f0/self.m - (self.C * self.rho * self.A * self.v[-1]**2)/(2*self.m)*self.dt)
            else:
                self.v.append(self.v[-1] + self.dt * self.p / (self.m * self.v[-1]) - (self.C * self.rho * self.A * self.v[-1]**2)/(2*self.m)*self.dt)
            self.t.append(_time)
            _time += self.dt

a = bicycle()
b = bicycleWithResistance()
c = bicycleWeNeed()
a.run()
b.run()
c.run()
plt.plot(a.t, a.v, label = 'Simple bicycle model')
plt.plot(b.t, b.v, label = 'Bicycle with resistance model')
plt.plot(c.t, c.v, label = 'Bicycel with resistance and $v_0=0$ model')
plt.xlabel('time($s$)')
plt.ylabel('velovity')
plt.title('Different bicycle model')
plt.legend()
plt.show()
