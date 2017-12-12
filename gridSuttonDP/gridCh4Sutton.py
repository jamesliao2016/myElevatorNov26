import numpy as np

# Random policy
# Assume there is a linear grid, the chance of choosing each direction is same
# The objective is to reach the two ends

stNum = 8
rewVal = -1
prob = 0.5
epsThr = 1e-6

action = [0,1]
states = list(range(1,stNum))
valVec = np.zeros(stNum+1)
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

stAct = [[(0.5) for ii in range(2)] for jj in range(1,stNum)]

states = list(range(1,stNum))
valVec = np.zeros(stNum+1)

def funEval(states,valVec,stAct,epsThr,stNum):
    while True:
        valVecTmp = np.zeros(stNum+1)
        for qq in states:
            yy = 1
            for ee in stAct[qq-1]:
                dirct = 1
                if yy == 0:
                    dirct = -1
                valVecTmp[qq] += ee * (rewVal + valVec[qq + dirct])

                yy -=1
            valVecTmp[qq] = round(valVecTmp[qq], 2)
        gg = np.sum(np.abs(valVec -valVecTmp))
        if gg < epsThr:
            # print(valVec)
            break
        valVec = valVecTmp
    return valVec

valVec = funEval(states,valVec,stAct,epsThr,stNum)

def funImpr(states,valVec,stAct,epsThr,stNum):
    for qq in states:
        yy = 0
        optVal = -999999999999
        for ee in stAct[qq-1]:
            dirct = 1
            if yy == 1:
                dirct = -1
            # valVecTmp[qq] += ee * (rewVal + valVec[qq + dirct])
            tmpVal = valVec[qq + dirct] - valVecTmp[qq]
            if tmpVal > optVal:
                optVal = tmpVal
                optSol = yy
            yy +=1
        if stAct[qq-1][optSol] * stAct[qq-1][1-optSol] >0.001:
            stAct[qq-1][optSol] += 0.01
            stAct[qq - 1][optSol] = round(stAct[qq-1][optSol],2)
            stAct[qq - 1][1 - optSol] -= 0.01
            stAct[qq - 1][1- optSol] = round(stAct[qq - 1][1- optSol], 2)
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
