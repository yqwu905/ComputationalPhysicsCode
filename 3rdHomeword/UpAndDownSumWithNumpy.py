import numpy as np
import time
import matplotlib.pyplot as plt

def numpyUpSum(n):
    s = np.arange(1, n + 1, dtype = np.float32)
    up = 1/s
    return up.sum()

def upSum(n):
    sum = np.float32(0)
    for i in range(1, n + 1):
        sum += np.float32(1/i)
    return sum

def timeTest(func, n):
    st = time.time()
    func(n)
    ed = time.time()
    return ed-st

if __name__ == '__main__':
    numpyTime = []
    normalTime = []
    n = np.array(range(1, 100)) * 1000
    for i in n:
        numpyTime.append(timeTest(numpyUpSum, i))
        normalTime.append(timeTest(upSum, i))
        print(i)
    plt.plot(n, numpyTime, label = 'Numpy')
    plt.plot(n, normalTime, label = 'Simplt method')
    plt.legend()
    plt.show()

