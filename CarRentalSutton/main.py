import poisEventFun as pef
import numpy as np
import reallotFun as rllt

# Parameters
locNum = 2
conArr = [3,4]
repArr = [3,2]
upCarNum = 20
rhoVal = 0.9
epsEval = 0.1

# Policy
w, h = upCarNum, upCarNum;
carPol = [[int((y - x)/2) for x in range(w+1)] for y in range(h+1)]
valVec = [[(0.0) for x in range(w+1)] for y in range(h+1)]

# Simulation parameters
simPeriod = 2
iniCars = [10,10]
lostSale = [(i-i) for i in range(len(iniCars))]
vt = 0
mvNumAbs = 0
epsDltBase = 1
epsDlt = 100
ww = 1
vtHist = [2]
# Simulation START here
while True:
    gg=[]
    for numCar1 in range(upCarNum):
        for numCar2 in range(upCarNum):
        # for ss in range(3000):
            iniCars[0] = numCar1
            iniCars[1] = numCar2
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
                diffTmp = 0
                oo = 1
                # Policy evaluation
                while oo<=30:
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
                    valBellTmp = vt + rhoVal * valVec[iniCarsUp[0]][iniCarsUp[1]]
                    nuVal = nuVal *(oo)/(oo+1) + float(valBellTmp / (oo+1))
                    oo += 1
                    if abs(nuVal - diffTmp) < epsEval:
                        break
                    diffTmp = nuVal
                    # Policy improvement
                if nuVal > (tmpVal + epsDltBase):
                    tmpVal = nuVal
                    valVec[iniRaw[0]][iniRaw[1]] = nuVal
                    carPol[iniRaw[0]][iniRaw[1]] = action
                    optSol = action
                    break
            diffVal = abs(valVec[iniRaw[0]][iniRaw[1]] - oldVal)
            epsDlt = max(epsDlt,diffVal)
            gg.append(diffVal)
    if (max(gg) < epsDltBase) and (max(gg)>=0):
        break

# print(valVec)
print(carPol)
# print('average reward: %f'%(float(vtHist[ww-1]) /(ww)))
