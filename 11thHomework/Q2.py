import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('./cmake-build-debug/Q2.data','r') as fp:
        data = fp.readlines()
    H1,H2,H3 = [],[],[]
    for i in data[0].split(',')[:-1]:
        H1.append(float(i))
    for i in data[1].split(',')[:-1]:
        H2.append(float(i))
    B,t = [1,-1],[999,1000]
    print(H1,H2)
    T = range(len(H1))
    plt.plot(T,H1, label = 'periodic')
    plt.plot(t,B, label = 'Magnet field change')
    plt.plot(T,H2,label = 'free')
    plt.legend();
    plt.show()