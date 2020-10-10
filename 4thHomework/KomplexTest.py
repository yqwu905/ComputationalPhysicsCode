from Komplex import Komplex
import math

a = Komplex(1.0, 1.0)
b = Komplex(1.0, 2.0)
e = b

print("Cartesian: a = {}".format(a))
print("Cartesian: b = {}".format(b))
print("Cartesian: a + b = {}".format(a+b))
print("Cartesian: a - b = {}".format(a-b))
print("Cartesian: a * b = {}".format(a*b))
print("Cartesian: a / b = {}".format(a/b))
print("Cartesian: e = b = {}".format(e))

a = Komplex(math.sqrt(2.0), math.pi/4.0)
b = Komplex(1.0, 2.0)
b.setType(0)

print("Polar: a = {}".format(a))
print("Polar: b = {}".format(b))
print("Polar: a + b = {}".format(a+b))
a.setType(1)
print("Different type sum: a + b = {}".format(a + b))
b.setType(1)
print("Polar: a = {}".format(a))
print("Polar: b = {}".format(b))
print("Polar: a + b = {}".format(a+b))
