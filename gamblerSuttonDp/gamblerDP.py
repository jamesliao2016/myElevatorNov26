import numpy as np

# Random policy
# Assume there is a linear grid, the chance of choosing each direction is same
# The objective is to reach the two ends

stNum = 8
rewVal = -1
prob = 0.5
epsThr = 1e-6
probH = 0.6

action = [0,1]
states = list(range(1,stNum))
valVec = np.zeros(stNum+1)

stAct = [[(1.0 / (jj+1)) for ii in range(jj+1)] for jj in range(1,stNum)]

states = list(range(1,stNum))
valVec = np.zeros(stNum+1)

# Function for value evaluation
def funEval(states,valVec,stAct,epsThr,stNum):
    while True:
        valVecTmp = np.zeros(stNum+1)
        for qq in states:
            yy = 1
            for ee in stAct[qq-1]:
                rewVal = yy - 1
                futVal = probH * (rewVal + valVec[min(qq + rewVal,stNum)]) \
                         + (1 - probH) * (-rewVal + valVec[max(0,qq - rewVal)])
                valVecTmp[qq] += ee * futVal
                yy +=1
            valVecTmp[qq] = round(valVecTmp[qq], 2)
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
        tmpProduct = 1
        for ee in stAct[qq-1]:
            dirct = yy
            # valVecTmp[qq] += ee * (rewVal + valVec[qq + dirct])
            tmpVal = probH * (valVec[min(stNum,qq + dirct)] - valVec[qq])\
                     + (1 - probH) * (valVec[max(0,qq - dirct)] - valVec[qq])
            if tmpVal > optVal:
                optVal = tmpVal
                optSol = yy
            yy +=1
            tmpProduct = tmpProduct * ee
        if tmpProduct >0.00000000001:
            uu = 0.0
            for yy in range(len(stAct[qq - 1])):
                stAct[qq - 1][yy] -= 0.01
                stAct[qq - 1][yy] = round(stAct[qq - 1][yy], 5)
                uu += 0.01
            stAct[qq-1][optSol] += uu
            stAct[qq - 1][optSol] = round(stAct[qq - 1][optSol], 5)

    return stAct

# print(funImpr(states,valVec,stAct,epsThr,stNum))

valVec = funEval(states, valVec, stAct, epsThr, stNum)
while True:
    stAct = funImpr(states, valVec, stAct, epsThr, stNum)
    valVecTmp = funEval(states, valVec, stAct, epsThr, stNum)
    gg = np.sum(np.abs(valVec -valVecTmp))
    if gg < epsThr:
        print('steady value')
        print(valVec)
        print('optimal policy')
        print(stAct)
        break
    valVec = valVecTmp

'''
# initial policy evaluation
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
        # print(valVec)
        break
    valVec = valVecTmp

'''
