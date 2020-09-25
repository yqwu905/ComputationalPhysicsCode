import numpy as np
import matplotlib.pyplot as plt
from sympy import Rational

def UpSum(n):
	term = np.float32(0)
	s = np.float32(0)
	for i in range(1, n + 1):
		term = np.float32(1/i)
		s += term
	return s

def DownSum(n):
	term = np.float32(0)
	s = np.float32(0)
	for i in range(n, 0, -1):
		term = np.float32(1/i)
		s += term
	return s

def KahanSum(n):
	s = np.float32(0)
	err = np.float32(0)
	term = np.float32(0)
	for i in range(n, 0, -1):
		term = np.float32(1/i)
		y = np.float32(term - err)
		t = np.float32(s + y)
		err = (t - s) - y
		s = t
	return s

def TrueSum(n):
	s = Rational(1/1)
	for i in range(2, n + 1):
		s = s + Rational(1/i)
	return s.evalf()

def calcAll(n):
	err = np.zeros(n, dtype = np.float32)
	u = np.zeros(n, dtype = np.float32)
	d = np.zeros(n, dtype = np.float32)
	k = np.zeros(n, dtype = np.float32)
	t = np.zeros(n, dtype = np.float32)
	for i in range(1, n + 1):
		u[i - 1] = UpSum(i)
		d[i - 1] = DownSum(i)
		k[i - 1] = KahanSum(i)
		t[i - 1] = TrueSum(i)
		#err[i - 1] = (u[i - 1] - d[i - 1])/(np.abs(u[i - 1]) + np.abs(d[i - 1]))
		if i%int(n/10) == 0:
			print("{}/{}".format(i, n))
	return u, d, k, t

if __name__ == '__main__':
	totalNum = 200
	u, d, k, t = calcAll(totalNum)
	err1 = (u - d) / (np.abs(u) + np.abs(d))
	err2 = np.abs(t - u)/t
	err3 = np.abs(t - d)/t
	err4 = np.abs(t - k)/t
	n = np.linspace(1, totalNum, totalNum)
	plt.figure(figsize = (19.2, 9.68))
	plt.subplot(2,2,1)
	plt.title('$S^{(Up)}$ and $S^{(Down)}$')
	plt.plot(n, u, label = 'Up Sum', linewidth = 3)
	plt.plot(n, d, label = 'Down Sum', linewidth = 1)
	plt.legend()
	plt.subplot(2,2,2)
	plt.title('$\\frac{S^{Up}-S^{Down}}{|S^{Up}|+|S^{Down}|}$ versus N')
	plt.xscale('symlog')
	plt.yscale('symlog')
	plt.plot(n, err1)
	plt.legend()
	plt.subplot(2,2,3)
	plt.title('Kahan Summation')
	plt.plot(n, k)
	plt.subplot(2,2,4)
	plt.title('Error Comparsion')
	plt.plot(n, err2, label = '$S^{Up}$ Error')
	plt.plot(n, err3, label = '$S^{Down}$ Error')
	plt.plot(n, err4, label = 'Kahan summation Error')
	plt.legend()
	#plt.show(dpi = 100)
	plt.savefig('./Sum_{}.png'.format(totalNum),dpi = 100)
	print('Up sum mean error:{}\nDown sum mean error:{}\nKahan sum error:{}'.format(np.mean(err2), np.mean(err3), np.mean(err4)))
