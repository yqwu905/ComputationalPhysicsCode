import numpy as np
import matplotlib.pyplot as plt

def sin(x):
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

testUnit = np.float32(0.005)
x,y1,y0,err = [],[],[],[]
maxAllowError = 0.01
firstErrorPoint = None
for i in range(1,8000):
	c = sin(i*testUnit)
	r = np.sin(i*testUnit)
	x.append(i*testUnit)
	y0.append(r)
	y1.append(c)
	if firstErrorPoint == None:
		if (np.abs(c-r)/r) > maxAllowError:
			firstErrorPoint = (i * testUnit, c)
	err.append(np.abs(c-r))
	#print('{}\t{}\t{}'.format())
plt.subplot(2,1,1)
plt.plot(x, y0, label = 'Numpy', linewidth = 3)
plt.plot(x, y1, label = 'Test', linewidth = 1)
plt.annotate('Error exceed 1% here({:.2f})'.format(firstErrorPoint[0]), firstErrorPoint, xytext = (firstErrorPoint[0], firstErrorPoint[1]+3), arrowprops = dict(arrowstyle = '->'))
plt.legend()
plt.subplot(2,1,2)
plt.plot(x, err, label = 'Error')
plt.annotate('Error exceed 1% here({:.2f})'.format(firstErrorPoint[0]), firstErrorPoint, xytext = (firstErrorPoint[0], firstErrorPoint[1]+3), arrowprops = dict(arrowstyle = '->'))
plt.legend()
plt.show()
