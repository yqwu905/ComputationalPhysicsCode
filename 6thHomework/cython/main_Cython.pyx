from libc.math cimport sin
import json
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

cdef calculate(double l=9.8, double Fd = 1.44,double omegad = 2/3.0, double dt = 0.001, double q = 0.5, double theta0 = 0.2, double t0 = 50):
    cdef theta = []
    cdef omega = []
    cdef t = []
    cdef double k,w,a,t_,pi,g
    g = 9.8
    pi = 3.141592653
    t = []
    k = g/l
    w = 0
    a = theta0
    t_ = 0
    while t_ <= t0:
        omega.append(w)
        theta.append(a)
        t.append(t_)
        w += (-k*sin(a)-q*w+Fd*sin(omegad*t_)) * dt
        a += w * dt
        if a > pi:
            a -= 2*pi
        elif a < -pi:
            a += 2*pi
        t_ += dt
    return theta, omega, t

def bifurcationDiagram(double dt):
    cdef double pi, flag, fd, omegad
    cdef int i, index
    omegad = 2/3.0
    pi = 3.141592653
    x = []
    y = []
    for theta0 in tqdm(np.linspace(0.19,0.21,200)):
        a,w,t = calculate(9.8, 1.4, 2/3.0, dt, 0.5, theta0, 1000*pi/omegad + 2)
        index = int((600*pi/omegad)/dt)
        flag = 602*pi
        for i in range(index, len(t)):
            if (omegad * t[i] - flag) > 0:
                x.append(theta0)
                y.append(a[i])
                flag += 2*pi
    print(len(x))
    plt.scatter(x,y,s = 2,color = 'blue', marker = '.')
    plt.savefig("./res.png")