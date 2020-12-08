import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def M():
    x,y = [],[]
    N = 20
    Size = 4
    with open("Q1.txt",'r') as fp:
        datas = fp.readlines()
    for i in range(N):
        x.append([])
        y.append([])
    n = 0
    for data in datas:
        if ':' in data:
            n+=1
            i = 0
        else:
            if n%1 == 0:
                xy = data.split(',')
                #print(xy)
                if xy[0] != '-nan(ind)' and xy[1] != '-nan(ind)':
                    x[i].append(float(xy[0]))
                    y[i].append(float(xy[1]))
                    i += 1
    plt.subplot(121)
    plt.title("Particle trajectory")
    plt.xlim(0,Size)
    plt.ylim(0,Size)
    for i in range(len(x)):
        size = int(len(x[i])/1.5)
        plt.scatter(x[i],y[i],s=5)
    v = []
    with open("Q1-V.txt",'r') as fp:
        datas = fp.readlines()
    for data in datas:
        v.append(float(data))
    plt.subplot(122)
    plt.title("$v_x$ distribution")
    plt.hist(v, bins = 50,range = (-3,3))
    plt.show()

    #for j in range(len(x[0])):
    #    if (j%3 == 0):
    #        plt.clf()
    #        plt.xlim(-1,21)
    #        plt.ylim(-1,21)
    #        for i in range(N):
    #            if j > 10:
    #                #plt.plot(x[i][j-5:j],y[i][j-5:j])
    #                plt.scatter(x[i][j-5:j],y[i][j-5:j],s = 8)
    #        plt.savefig('./__tmp/{}.png'.format(j))

M()