import math

class Komplex:
    def __init__(self, x, y, typec=1):
        assert (typec in [0,1]), "typec could only be 1 or 0, not {}".format(typec)
        self.typec = typec
        if typec == 1:
            self.re = x
            self.im = y
        elif typec == 0:
            self.re = x*math.cos(y)
            self.im = x/math.sin(y)
    
    def __add__(self, another):
        if self.typec == another.typec:
            return Komplex(self.re + another.re, self.im + another.im, self.typec)
        else:
            print("Warning:two complex with different type were given, set type to cartesian")
            return Komplex(self.re + another.re, self.im + another.im)

    def __sub__(self, another):
        if self.typec == another.typec:
            return Komplex(self.re - another.re, self.im - another.im, self.typec)
        else:
            print("Warning:two complex with different type were given, set type to cartesian")
            return Komplex(self.re - another.re, self.im - another.im)

    def __mul__(self, another):
        if self.typec == another.typec:
            return Komplex(self.re * another.re - self.im * another.im, self.im * another.re + another.im * self.re, self.typec)
        else:
            print("Warning:two complex with different type were given, set type to cartesian")
            return Komplex(self.re * another.re - self.im * another.im, self.im * another.re + another.im * self.re)

    def __truediv__(self, another):
        factor = (another.re**2 + another.im**2)
        if self.typec == another.typec:
            return Komplex((self.re * another.re + self.im * another.im)/factor, (self.im * another.re - self.re * another.im)/factor, self.typec)
        else:
            print("Warning:two complex with different type were given, set type to cartesian")
            return Komplex((self.re * another.re + self.im * another.im)/factor, (self.im * another.re - self.re * another.im)/factor)

    def __repr__(self):
        if self.typec == 1:
            return "{}+{}i".format(self.re, self.im)
        else:
            return "{}*e^({}i)".format(math.sqrt(self.re**2+self.im**2), math.atan(self.im/self.re))

    def setType(self, typec):
        assert (typec in [0,1]), "typec could only be 1 or 0, not {}".format(typec)
        self.typec = typec

    def conj(self):
        return(Komplex(self.re, -self.im, self.typec))

    def getRe(self):
        return self.re

    def getIm(self):
        return self.im
