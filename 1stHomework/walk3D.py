import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def randomWalk3D(steps, stepLeng, x0, y0, z0):
    x = np.ones(1) * x0
    y = np.ones(1) * y0
    z = np.ones(1) * z0
    for i in range(steps):
        '''
        a1 = np.random.random()*2*np.pi
        a2 = np.random.random()*np.pi
        '''
        x = np.append(x, x[-1] + np.random.random()*steps)
        y = np.append(z, z[-1] + np.random.random()*steps)
        z = np.append(z, z[-1] + np.random.random()*steps)
        '''
        x = np.append(x, x[-1] + [stepLeng * np.cos(a1) * np.cos(a2)])
        y = np.append(y, y[-1] + [stepLeng * np.cos(a1) * np.sin(a2)])
        z = np.append(z, z[-1] + [stepLeng * np.sin(a1)])
        '''
        return x, y, z

totalNum = 1000
steps = 200
stepLeng = 0.5
x0 = y0 = z0 = 5
fig = plt.figure()
ax = Axes3D(fig)
xr = np.zeros(totalNum)
yr = np.zeros(totalNum)
zr = np.zeros(totalNum)
r = np.zeros(totalNum)

for i in range(totalNum):
    x, y, z = randomWalk3D(steps, stepLeng, x0, y0, z0)
    dist = np.linalg.norm([x0-x[-1], y0-y[-1], z0-z[-1]])
    r[i] = dist
    xr[i] = x[-1]
    yr[i] = y[-1]
    zr[i] = z[-1]
plt.title('N = {}'.format(totalNum))
ax.scatter3D(xr,yr,zr,cmap = 'Blues')
plt.savefig("./{}p.png".format(totalNum))
plt.show()
fig, ax = plt.subplots(1,1)
ax.hist(r,bins = 20)
fig.savefig('./{}h.png'.format(totalNum))

