# poisson probability
import numpy as np
from math import *
def poisEvent(lambdax,nx):
    probRlt = 0
    if nx>0:
        probRlt = pow(lambdax,nx)*exp(-lambdax)/factorial(nx)
    return probRlt

def eventOccur(lambdax,nx):
    jj = np.random.uniform()
    dd = poisEvent(3, 3)
    rlt = 0
    if jj < dd:
        rlt = 1
    return rlt

if __name__ == '__main__':
    for cc in range(10):
        jj = np.random.uniform()
        dd = poisEvent(3,3)
        if jj < dd:
            print('got it %f'%dd)
        else:
            print('NO %f %f'%(dd,jj))

    # print(poisEvent(2,2))