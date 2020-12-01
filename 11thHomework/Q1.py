import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    T,M = [],[]
    Tn, Mn, Nn = [],[],[]
    Tc = 2.27
    with open("Q1.txt","r") as fp:
        datas = fp.readlines()
    for data in datas:
        T.append(float(data.split(",")[0]))
        M.append(float(data.split(",")[1]))
    for i in range(len(T)):
        if T[i] in Tn:
            idx = Tn.index(T[i])
            Mn[idx] += abs(M[i])
            Nn[idx] += 1
        else:
            Tn.append(T[i])
            Mn.append(abs(M[i]))
            Nn.append(1)
    for i in range(len(Tn)):
        Mn[i] = Mn[i]/Nn[i]
    Tn = np.array(Tn)
    Mn = np.array(Mn)
    idx = Tc - Tn > 0
    Tn = Tn[idx]
    Mn = Mn[idx]
    LogT = np.log(Tc-Tn)
    LogM = np.log(Mn)
    popt = np.polyfit(LogT, LogM, deg = 1)
    print(popt)
    x = np.linspace(np.min(LogT), np.max(LogT), 50)
    plt.subplot(1,2,1)
    plt.title("T-M")
    plt.scatter(T, M)
    plt.scatter(Tn, Mn)
    plt.subplot(1,2,2)
    plt.title("Log(T)-Log(M)")
    plt.scatter(LogT,LogM)
    plt.plot(x, popt[0]*x + popt[1])
    plt.show()