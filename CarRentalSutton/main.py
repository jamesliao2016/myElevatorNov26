import poisEventFun as pef
import pandas as pd
from math import *
import reallotFun as rllt

# Parameters
locNum = 2
conArr = [3,4]
repArr = [3,2]
upCarNum = 20

# Policy
w, h = upCarNum, upCarNum;
carPol = [[int((y - x)/2) for x in range(w+1)] for y in range(h+1)]

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
while epsDlt > epsDltBase:

    tmpArr = []
    tmpRep = []
    for ee in range(len(conArr)):
        lstIx = ee - 1
        arrNum = pef.retPoiNum(conArr[lstIx])
        repNum = pef.retPoiNum(repArr[lstIx])
        tmpArr.append(arrNum)
        tmpRep.append(repNum)

        numDlt = repNum - arrNum
        # iniCars[lstIx] += numDlt
    iniCars,mvNumAbs = rllt.moveCar(iniCars,carPol)
    iniCars,lostSale,rentVec = rllt.reallot(iniCars,tmpArr,tmpRep,lostSale,upCarNum)
    vt = rllt.calVal(vt, rentVec,mvNumAbs)
    vtHist.append(vt)
    epsDlt = abs(float(vtHist[ww]) /(ww+1) - float(vtHist[ww-1]) /(ww))/ (float(vtHist[ww-1]) /(ww))
    ww += 1

print(iniCars)
# print(lostSale)
print(vt)
print(ww)
print('average reward: %f'%(float(vtHist[ww-1]) /(ww)))

