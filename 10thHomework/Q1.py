'''
!!!!!!!!!!!Warning!!!!!!!!!!!
This code was incorrect(this code implement the enumaration method of SAW, but the question request a simulation implementation), please see the Q1N.py.
!!!!!!!!!!!Warning!!!!!!!!!!!
'''
import numpy as np
from tqdm import tqdm
import json
from math import sqrt

class point():
    def __init__(self, x, y):
        self.value = np.array([x,y],dtype=np.int8)
    def __add__(self, other):
        return point(self.value[0] + other.value[0], self.value[1] + other.value[1])

class SAW():
    def __init__(self, steps = 10):
        with open('data.txt', 'w') as fp:
            fp.write('#################################\n')
        self.path = [[(0,0)]]
        self.steps = steps
        self.pn = []
        self.R = []
    def iter(self):
        newPath = []
        for i in tqdm(self.path):
            for j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newPosition = (i[-1][0] + j[0], i[-1][1] + j[1])
                #print(i,newPosition, newPosition in i)
                if newPosition in i:
                    continue
                else:
                    tmp = i[:]
                    tmp.append(newPosition)
                    newPath.append(tmp)
        self.path = newPath

    def calcDist(self):
        self.R = []
        for i in self.path:
            self.R.append(i[-1][0]**2 + i[-1][1]**2)
        r = np.array(self.R)
        return np.mean(r)

    def calc(self):
        for step in range(self.steps):
            r = self.calcDist()
            self.pn.append(len(self.path))
            with open('data.txt','a') as fp:
                fp.write("Iter {}\tr^2 {}\ttotalNum {}\n ".format(step, r, len(self.path)))
            print("Iteration {} start.".format(step))
            self.iter()
            print("Iteration {} finished.".format(step))

s = SAW(13)
s.calc()