import numpy as np

# Random policy
# Assume there is a linear grid, the chance of choosing each direction is same
# The objective is to reach the two ends

stNum = 100
epsThr = 0.00000001
probH = 0.4

states = list(range(0,stNum))
valVec = np.zeros(stNum+1)
valVec[stNum]=1.0

stAct = [[(1.0 / (min((jj+1),(101 - jj)))) for ii in range(0,min((jj+1),(101 - jj)))]\
         for jj in range(0,stNum)]

# Function for value evaluation
def funEval(states,valVec,stAct,epsThr,stNum):
    while True:
        valVecTmp = np.zeros(stNum+1)
        valVecTmp[stNum] = 1.0
        for qq in states:
            yy = 1
            for ee in stAct[qq]:
                rewVal = yy - 1
                futVal = probH * (valVec[min(qq + rewVal,stNum)]) \
                         + (1 - probH) * (valVec[max(0,qq - rewVal)])
                valVecTmp[qq] += ee * futVal
                yy +=1
            valVecTmp[qq] = round(valVecTmp[qq], 5)
        gg = np.sum(np.abs(valVec -valVecTmp))
        if gg < epsThr:
            # print(valVec)
            break
        valVec = valVecTmp
    return valVec

valVec = funEval(states,valVec,stAct,epsThr,stNum)

# stActRaw = [[(0) for ii in range(jj+1)] for jj in range(0,stNum)]

# Function for value improvement
def funImpr(states,valVec,stAct,epsThr,stNum):
    for qq in states:
        yy = 0
        optVal = -999999999999
        tmpProduct = 1.0
        # stActNu = stAct
        for ee in stAct[qq]:
            dirct = yy
            # valVecTmp[qq] += ee * (rewVal + valVec[qq + dirct])
            tmpVal = probH * (valVec[min(stNum,qq + dirct)] )\
                     + (1 - probH) * (valVec[max(0,qq - dirct)] )
            if tmpVal > optVal:
                optVal = tmpVal
                optSol = yy
            yy += 1
            tmpProduct = min(ee,tmpProduct)
        if tmpProduct >= 0.00001:
            uu = 0.0
            for yy in range(len(stAct[qq])):
                # dltTmp = stAct[qq - 1][yy] - max(stAct[qq - 1][yy] - 0.01,0)
                dltTmp = stAct[qq][yy]
                # stAct[qq - 1][yy] = max(stAct[qq - 1][yy] - 0.01,0)
                stAct[qq][yy] = 0
                uu += dltTmp
                stAct[qq][yy] = round(stAct[qq][yy])
            stAct[qq][optSol] = stAct[qq][optSol] + uu
            stAct[qq][optSol] = round(stAct[qq][optSol])

    return stAct

# print(funImpr(states,valVec,stAct,epsThr,stNum))

valVec = funEval(states, valVec, stAct, epsThr, stNum)
while True:
    stActTmp = funImpr(states, valVec, stAct, epsThr, stNum)
    valVecTmp = funEval(states, valVec, stActTmp, epsThr, stNum)
    gg = np.sum(np.abs(valVec -valVecTmp))
    hh = np.abs(np.sum(np.sum(stAct)) - np.sum(np.sum(stActTmp)))
    if gg < epsThr:
        print('steady value')
        print(valVec)
        print('optimal policy')
        print(stAct)
        break
    valVec = valVecTmp
    stAct = stActTmp
stActFinal = []

for pp in stAct:
    aa = 0
    for ss in (pp):
        if ss > 0.5:
            stActFinal.append(aa)
        aa+=1
import matplotlib.pyplot as plt
print(len(states))
print(len(stActFinal))
plt.scatter(states,stActFinal)
plt.show()