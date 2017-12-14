import numpy as np

# Random policy
# Assume there is a linear grid, the chance of choosing each direction is same
# The objective is to reach the two ends

stNum = 100
epsThr = 1e-10
probH = 0.4

states = list(range(0,stNum))
valVec = np.zeros(stNum+1)
policy = [0 for ii in range(stNum)]
valVec[stNum]=1.0

stAct = [[(1.0 / (min((jj+1),(101 - jj)))) for ii in range(0,min((jj+1),(101 - jj)))]\
         for jj in range(0,stNum)]

# Function for value evaluation

deltaVal = 1
tmpval = 0
while (deltaVal > epsThr):
    deltaVal = 0
    for qq in (range(1,stNum)):
        oldVal = valVec[qq]
        optValTmp = 0.0
        optSol = policy[qq]
        for ee in range(min(qq+1,stNum+1-qq)):
            futVal = probH * (valVec[qq+ee]) \
                     + (1 - probH) * (valVec[qq-ee])
            if futVal > optValTmp:
                optValTmp = futVal
                optSol = ee
        valVec[qq] = optValTmp
        policy[qq] = optSol
        gg =abs(valVec[qq]-oldVal)
        deltaVal = max(deltaVal,gg)
print(deltaVal)


# stActRaw = [[(0) for ii in range(jj+1)] for jj in range(0,stNum)]

# print(funImpr(states,valVec,stAct,epsThr,stNum))

# valVec = funEval(states, valVec, stAct, epsThr, stNum)
# while True:
#    stActTmp = funImpr(states, valVec, stAct, epsThr, stNum)
#     valVecTmp = funEval(states, valVec, stAct, epsThr, stNum)
#     gg = np.sum(np.abs(valVec -valVecTmp))
#    hh = np.abs(np.sum(np.sum(stAct)) - np.sum(np.sum(stActTmp)))
#     if gg < epsThr:
print('steady value')
print(valVec)

        # break
    # valVec = valVecTmp
    # stAct = stActTmp
# stActFinal = []
#
# for pp in stAct:
#     aa = 0
#     for ss in (pp):
#         if ss > 0.5:
#             stActFinal.append(aa)
#         aa+=1

import matplotlib.pyplot as plt
# print(len(states))
print(len(policy))
print('optimal policy')
print(policy)
plt.scatter(states,policy)
plt.show()
# plt.scatter(states,valVec)
# print(len(valVec))
# plt.show()


# Function for value improvement
# def funImpr(states,valVec,stAct,epsThr,stNum,policy):
#     for qq in (range(1,stNum)):
#         yy = 0
#         optVal = valVec[qq]
#         optSol = policy[qq]
#         for ee in stAct[qq]:
#             dirct = yy
#             tmpVal = probH * (valVec[min(stNum,qq + dirct)])\
#                      + (1 - probH) * (valVec[max(0,qq - dirct)])
#             if tmpVal > optVal:
#                 optVal = tmpVal
#                 optSol = yy
#             yy += 1
#         policy[qq] = optSol
#     return policy
