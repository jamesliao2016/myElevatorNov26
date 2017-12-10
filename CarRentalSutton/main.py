import poisEventFun as pef
import pandas as pd
from math import *
import reallotFun as rllt

# Parameters
locNum = 2
conArr = [3,4]
repArr = [3,2]

# Simulation part
simPeriod = 100
iniCars = [100,100]
lostSale = [0,0]
for ww in range(simPeriod):
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
    iniCars,lostSale = rllt.reallot(iniCars,tmpArr,tmpRep,lostSale)
print(iniCars)
print(lostSale)
