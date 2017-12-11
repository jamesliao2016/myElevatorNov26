import numpy as np

stNum = 8
rewVal = -1
prob = 0.5
epsThr = 1e-6

action = [0,1]
states = list(range(1,stNum))
valVec = np.zeros(stNum+1)

while True:
    valVecTmp = np.zeros(stNum+1)
    for qq in states:
        for ee in action:
            dirct = 1
            if ee == 0:
                dirct = -1
            valVecTmp[qq] += prob * (rewVal + valVec[qq + dirct])
    gg = np.sum(np.abs(valVec -valVecTmp))
    if gg < epsThr:
        print(valVec)
        break
    valVec = valVecTmp