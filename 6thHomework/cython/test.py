from main_Cython import bifurcationDiagram
from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt

def main():
    wdList = np.linspace(2/3.0,2/3.0+0.02,1)
    pool = Pool(processes=1)
    for i in range(len(wdList)):
        pool.apply_async(bifurcationDiagram, args = (wdList[i], 0.04))
    print('Submit success!')
    pool.close()
    pool.join()


if __name__ == '__main__':
    bifurcationDiagram(0.04)
    