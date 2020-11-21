import numpy as np
from random import random
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(x,mu,gamma):
    return (mu/3)*(1+(gamma-1)/x)

class SAW():
    def __init__(self, steps = 50, n = 10**6):
        self.n = n
        self.steps = steps
    def simulate(self):
        nSurvive = 0
        for i in tqdm(range(self.n)):
            if self.oneWay():
                nSurvive += 1
        return (nSurvive/self.n)
    def oneWay(self):
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        path = [[0,0]]
        lastDir = None
        for step in range(self.steps):
            dir = int(random()*4)
            if lastDir == None:
                path.append([path[-1][0] + direction[dir][0], path[-1][1] + direction[dir][1]])
                lastDir = dir
            else:
                while lastDir+dir == 1 or lastDir+dir == 5:
                    dir = int(random()*4)
                path.append([path[-1][0] + direction[dir][0], path[-1][1] + direction[dir][1]])
                lastDir = dir
            for i in path[:-1]:
                if i == path[-1]:
                    return False
        return True

n = 10**3
pn = []
for i in range(1,51):
    s = SAW(steps = i, n = int(n * 1.2**i))
    pn.append(s.simulate())
    print(pn[-1])
with open('data.txt','w') as fp:
    json.dump(pn, fp)


with open('data.txt', 'r') as fp:
    data = np.array(json.load(fp))
tot = 4
for i in data:
    print(tot * i)
    tot = tot * 3

x = np.array(range(1,50))
y = data[1:]/data[0:-1]
popt, pcov = curve_fit(f, x, y)
print("mu = {}, gamma = {}".format(popt[0], popt[1]))
plt.scatter(x,y,label = '$\\frac{P(n+1)}{P(n)}$', color = 'r')
plt.plot(x, f(range(1,50), popt[0], popt[1]), label = "$\\frac{P(n+1)}{P(n)}\\sim\\frac{%.2f}{3}(1+\\frac{%.2f - 1}{n})$"%(popt[0], popt[1]))
plt.legend()
plt.show()

