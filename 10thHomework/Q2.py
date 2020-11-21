import matplotlib.pyplot as plt
from math import tan
from tqdm import tqdm

def squareUnit(p1, p2):
    newPoint = []
    if p1[1] == p2[1]:
        dx = p2[0] - p1[0]
        newPoint.append([p1[0] + dx/3, p1[1]])
        newPoint.append([p1[0] + dx/3, p1[1]+dx/3])
        newPoint.append([p1[0] + 2*dx/3, p1[1] + dx/3])
        newPoint.append([p1[0] + 2*dx/3, p1[1]])
    else:
        dy = p2[1] - p1[1]
        newPoint.append([p1[0], p1[1] + dy/3])
        newPoint.append([p1[0]-dy/3, p1[1] + dy/3])
        newPoint.append([p1[0]-dy/3, p1[1] + 2*dy/3])
        newPoint.append([p1[0], p1[1] + 2*dy/3])
    return newPoint


class fractalCurve():
    def __init__(self, level = 10, generator = squareUnit):
        self.level = level
        self.pattern = []
        self.generator = generator
    def generate(self, level):
        print(level)
        if level == 1:
            self.pattern = [[0,1], [0,0]]
        else:
            self.generate(level - 1)
            plt.plot(self.pattern[0], self.pattern[1])
            plt.title("Level = {}".format(level - 1))
            plt.show()
            newPattern = [[],[]]
            for i in tqdm(range(len(self.pattern[0]) - 1)):
                #print([self.pattern[0][i], self.pattern[1][i]], [self.pattern[0][i+1], self.pattern[1][i+1]])
                newPoint = self.generator([self.pattern[0][i], self.pattern[1][i]], [self.pattern[0][i+1], self.pattern[1][i+1]])
                newPattern[0].append(self.pattern[0][i])
                newPattern[1].append(self.pattern[1][i])
                for j in newPoint:
                    newPattern[0].append(j[0])
                    newPattern[1].append(j[1])
            newPattern[0].append(self.pattern[0][-1])
            newPattern[1].append(self.pattern[1][-1])
            self.pattern = newPattern[:]

    def plot(self):
        self.generate(self.level)
        plt.plot(self.pattern[0], self.pattern[1])
        plt.title("Level = {}".format(self.level))
        plt.show()

f = fractalCurve(level = 12)
f.plot()

