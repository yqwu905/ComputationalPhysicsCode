import numpy as np
import matplotlib.pyplot as plt

def taylorCos(x):
    eps = np.float32(10**-8)
    sum = np.float32(1)
    term = np.float32(1)
    n = 0
    while True:
        n += 1
        term = -x*x*term/(2*n*(2*n-1))
        sum += term
        if abs(term/sum) < eps:
            break
    return sum

def taylorSin(x):
    if x<0:
        return -1 * taylorSin(abs(x))
    elif x > 2*np.pi:
        return taylorSin(x % (2*np.pi))
    elif x > np.pi:
        return -1 * taylorSin(2*np.pi - x)
    elif x > np.pi/2:
        return taylorSin(np.pi - x)
    elif x > np.pi/4:
        return taylorCos(abs(x - np.pi/2))
    else:
        eps = np.float32(10**-8)
        term = np.float32(x)
        sum = np.float32(x)
        n = 1
        while(True):
            n += 1
            term = -x*x*term/((2*n-1)*(2*n-2))
            sum += term
            if np.abs(term/sum) < eps:
                break
        return sum

if __name__ == '__main__':
    x = np.linspace(0.001, 100, 10000)
    y = []
    for i in x:
        y.append(taylorSin(i))
        #print(i)
    y = np.array(y)
    yn = np.sin(x)
    plt.title('Sin Function')
    plt.plot(x,y,label = 'Taylor Expand Sin',linewidth=3)
    plt.plot(x, yn, label = 'Numpy Sin')
    plt.plot(x, np.abs(yn - y), label = 'Error')
    plt.legend()
    plt.show()
