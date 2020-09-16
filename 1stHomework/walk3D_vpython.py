from vpython import *
import random

random.seed(None)
jmax = 1000
x0 = y0 = z0 = 0.0

scene = canvas(x=0, y=0, width=600, height=600, title='Walk3D', forward=vector(-0.6,-0.5,-1))
pts   = curve(x=list(range(0, 100)), radius=10.0,color=color.yellow)    
xax   = curve(x=list(range(0,1500)), color=color.red, pos=[vector(0,0,0),vector(1500,0,0)], radius=10.)
yax   = curve(x=list(range(0,1500)), color=color.red, pos=[vector(0,0,0),vector(0,1500,0)], radius=10.)
zax   = curve(x=list(range(0,1500)), color=color.red, pos=[vector(0,0,0),vector(0,0,1500)], radius=10.)
xname = label( text = "X", pos = vector(1000, 150,0), box=0)
yname = label( text = "Y", pos = vector(-100,1000,0), box=0)
zname = label( text = "Z", pos = vector(100, 0,1000), box=0)

pts.append(vector(0,0,0))           # Starting point
for i in range(1, 100):
    x0 += (random.random() - 0.5)*2.           # -1 =< x =< 1  
    y0 += (random.random() - 0.5)*2.           # -1 =< y =< 1
    z0 += (random.random() - 0.5)*2.           # -1 =< z =< 1
    pts.append(vector(200*x0 - 100,200*y0 - 100,200*z0 - 100))
    rate(100)
print("This walk's distance R =", sqrt(x0*x0 + y0*y0+z0*z0))
