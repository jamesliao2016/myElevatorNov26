# poisson probability
import numpy as np
from math import *
def poisEvent(lambdax,nx):
    probRlt = 0
    if nx>0:
        probRlt = pow(lambdax,nx)*exp(-lambdax)/factorial(nx)
    return probRlt

if __name__ == '__main__':
    for cc in range(10):
        jj = np.random.uniform()
        dd = poisEvent(3,3)
        if jj < dd:
            print('got it %f'%dd)
        else:
            print('NO %f %f'%(dd,jj))

    # print(poisEvent(2,2))