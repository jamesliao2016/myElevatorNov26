import poisEventFun as pef
import pandas as pd
from math import *
import reallotFun as rllt

# Parameters
locNum = 2
conArr = [3,4]
repArr = [3,2]
upCarNum = 20
rhoVal = 0.9

# Policy
w, h = upCarNum, upCarNum;
carPol = [[int((y - x)/2) for x in range(w+1)] for y in range(h+1)]
valVec = [[(0.0) for x in range(w+1)] for y in range(h+1)]

# Simulation parameters
simPeriod = 100
iniCars = [10,10]
lostSale = [(i-i) for i in range(len(iniCars))]
vt = 0
mvNumAbs = 0
epsDltBase = 0.0001
epsDlt = 100
ww = 1
vtHist = [2]
# Simulation START here
# while True:
while ww < 3000:
    epsDlt = 0.0
    tmpArr = []
    tmpRep = []
    iniRaw = iniCars
    oldVal = valVec[iniCars[0]][iniCars[1]]
    diffNum = abs(iniCars[0] - iniCars[1])
    tmpVal = valVec[iniCars[0]][iniCars[1]]
    for action in range(diffNum):
        iniCars, mvNumAbs = rllt.moveCar(iniCars, action)
        for ee in range(len(conArr)):
            lstIx = ee - 1
            arrNum = pef.retPoiNum(conArr[lstIx])
            repNum = pef.retPoiNum(repArr[lstIx])
            tmpArr.append(arrNum)
            tmpRep.append(repNum)
            numDlt = repNum - arrNum
            # iniCars[lstIx] += numDlt
        iniCarsUp,lostSale,rentVec = rllt.reallot(iniRaw,tmpArr,tmpRep,lostSale,upCarNum)
        vt = rllt.calVal(vt, rentVec,mvNumAbs)
        valVec[iniRaw[0]][iniRaw[1]] = vt + rhoVal * valVec[iniCars[0]][iniCars[1]]
        nuVal = valVec[iniRaw[0]][iniRaw[1]]
        if nuVal > (tmpVal + epsDltBase):
            tmpVal = nuVal
            valVec[iniRaw[0]][iniRaw[1]] = nuVal
            carPol[iniRaw[0]][iniRaw[1]] = action
    # vtHist.append(vt)
    # epsDlt = abs(float(vtHist[ww]) /(ww+1) - float(vtHist[ww-1]) /(ww))/ (float(vtHist[ww-1]) /(ww))
    diffVal = abs(valVec[iniRaw[0]][iniRaw[1]] - oldVal)
    epsDlt = max(epsDlt,diffVal)
    if (epsDlt < epsDltBase) and (epsDlt>0):
        break
    ww += 1

print(iniCars)
print(valVec)
# print(vt)
# print(ww)
# print('average reward: %f'%(float(vtHist[ww-1]) /(ww)))
