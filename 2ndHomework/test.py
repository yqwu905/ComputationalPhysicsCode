import numpy as np
import matplotlib.pyplot as plt
import json

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


num = 150
it = 30000
u = []
d = []
for i in range(num):
    u.append(UpSum(i*it))
    d.append(DownSum(i*it))
    print(i)
u = np.array(u)
d = np.array(d)
n = np.linspace(0, num*it, num)
err = (u - d)/(u + d)
with open('./data','w') as fp:
	json.dump(err, fp)
plt.plot(n, err)
plt.show()
    