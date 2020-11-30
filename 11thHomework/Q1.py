import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def meshSearch(t, m):
    min = 1000000000000
    minIJ = [1,1]
    for i in np.linspace(2, 2.27, 50):
        for j in np.linspace(1/8-0.05,1/8+0.05,50):
            T = (i - t) > 0
            #print(np.power(i-t[T], j))
            err = np.sum(np.abs(m[T] - np.power(i-t[T], j)))
            if err < min:
                print(err, i, j)
                min = err
                minIJ = [i,j]
    return min, minIJ


if __name__ == '__main__':
    T,M = [],[]
    with open('data.txt','r',encoding='UTF-8') as fp:
        data = fp.readlines()
    for i in data:
        T.append(float(i.split(',')[0]))
        M.append(float(i.split(',')[1]))
    T = np.array(T)
    M = np.array(M)
    print(meshSearch(T,M))
    plt.title("T-M relation")
    plt.plot(T,M,label='Magnetization')

    plt.xlabel('T')
    plt.ylabel('M')
    plt.legend()
    plt.show()