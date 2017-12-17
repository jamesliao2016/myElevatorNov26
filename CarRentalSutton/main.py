import poisEventFun as pef
import numpy as np
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
simPeriod = 10
iniCars = [10,10]
lostSale = [(i-i) for i in range(len(iniCars))]
vt = 0
mvNumAbs = 0
epsDltBase = 0.01
epsDlt = 100
ww = 1
vtHist = [2]
# Simulation START here
while True:
# for ss in range(3000):
    iniCars[0] = np.random.randint(upCarNum)
    iniCars[1] = np.random.randint(upCarNum)
    epsDlt = 0.0

    iniRaw = iniCars
    oldVal = valVec[iniCars[0]][iniCars[1]]
    diffNum = abs(iniCars[0] - iniCars[1])
    tmpVal = valVec[iniCars[0]][iniCars[1]]
    optSol = 0

    actL = -min(iniCars)
    actU = max(iniCars)
    for action in range(actL,actU):
        nuVal = 0
        for uu in range(simPeriod):
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
            iniCarsUp, mvNumAbs = rllt.moveCar(iniCars, action, upCarNum)
            iniCarsUp,lostSale,rentVec = rllt.reallot(iniCarsUp,tmpArr,tmpRep,lostSale,upCarNum)
            vt = rllt.calVal(rentVec,mvNumAbs)
            valBellTmp = vt + rhoVal * valVec[iniCars[0]][iniCars[1]]
            nuVal += float(valBellTmp / simPeriod)
        if nuVal > (tmpVal + epsDltBase):
            tmpVal = nuVal
            valVec[iniRaw[0]][iniRaw[1]] = nuVal
            carPol[iniRaw[0]][iniRaw[1]] = action
            optSol = action
            break
    diffVal = abs(valVec[iniRaw[0]][iniRaw[1]] - oldVal)
    epsDlt = max(epsDlt,diffVal)
    if (epsDlt < epsDltBase) and (epsDlt>0):
        break

print(iniCars)
print(valVec)
# print(vt)
# print(ww)
# print('average reward: %f'%(float(vtHist[ww-1]) /(ww)))
