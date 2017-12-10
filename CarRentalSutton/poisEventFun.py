# poisson probability
import numpy as np
from math import *
# Poisson probability density
def poisProbDen(lambdax,nx):
    probRlt = pow(lambdax,nx)*exp(-lambdax)/factorial(nx)
    return probRlt

# Poisson accumulate probability
def poisProbAcc(lambdax,nx):
    probAccRlt = 0.0
    for qq in range(nx+1):
        probAccRlt+=poisProbDen(lambdax,qq)
    return probAccRlt

def eventOccur(lambdax,nx):
    jj = np.random.uniform()
    dd = poisProbAcc(3, 3)
    rlt = 0
    if jj < dd:
        rlt = 1
    return rlt

if __name__ == '__main__':
    for cc in range(20):
        jj = np.random.uniform()
        dd1 = poisProbAcc(5,5)
        dd2 = poisProbAcc(5, 3)
        if jj < dd1 and jj > dd2:
            print('got it %f %f'%(dd1,dd2))
        else:
            print('NO %f %f %f'%(dd1,dd2,jj))

    # print(poisEvent(2,2))