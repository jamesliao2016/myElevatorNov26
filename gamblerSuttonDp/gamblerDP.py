import numpy as np

# Random policy
# Assume there is a linear grid, the chance of choosing each direction is same
# The objective is to reach the two ends

stNum = 100
rewVal = -1
prob = 0.5
epsThr = 1e-6
probH = 0.4

action = [0,1]
states = list(range(1,stNum))
valVec = np.zeros(stNum+1)

stAct = [[(1.0 / (jj+1)) for ii in range(jj+1)] for jj in range(1,stNum)]
stActRaw = [[(1.0 / (jj+1)) for ii in range(jj+1)] for jj in range(1,stNum)]

states = list(range(1,stNum))
valVec = np.zeros(stNum+1)
valVec[stNum]=1.0
# Function for value evaluation
def funEval(states,valVec,stAct,epsThr,stNum):
    while True:
        valVecTmp = np.zeros(stNum+1)
        valVecTmp[stNum] = 1.0
        for qq in states:
            yy = 1
            for ee in stAct[qq-1]:
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

# Function for value improvement
def funImpr(states,valVec,stAct,epsThr,stNum):
    for qq in states:
        yy = 0
        optVal = -999999999999
        tmpProduct = 1.0
        stActNu = stActRaw
        if np.random.uniform() > 0.05:
            stActNu = stAct
        for ee in stActNu[qq-1]:
            dirct = yy
            # valVecTmp[qq] += ee * (rewVal + valVec[qq + dirct])
            tmpVal = probH * (valVec[min(stNum,qq + dirct)] - valVec[qq])\
                     + (1 - probH) * (valVec[max(0,qq - dirct)] - valVec[qq])
            if tmpVal > optVal:
                optVal = tmpVal
                optSol = yy
            yy +=1
            tmpProduct = min(ee,tmpProduct)
        if tmpProduct >= 0.00001:
            uu = 0.0
            for yy in range(len(stAct[qq - 1])):
                # dltTmp = stAct[qq - 1][yy] - max(stAct[qq - 1][yy] - 0.01,0)
                dltTmp = stAct[qq - 1][yy]
                # stAct[qq - 1][yy] = max(stAct[qq - 1][yy] - 0.01,0)
                stAct[qq - 1][yy] = 0
                uu += dltTmp
                stAct[qq - 1][yy] = round(stAct[qq - 1][yy])

            stAct[qq-1][optSol] = stAct[qq-1][optSol] + uu
            stAct[qq - 1][optSol] = round(stAct[qq - 1][optSol])

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
plt.scatter(states,stActFinal)
plt.show()