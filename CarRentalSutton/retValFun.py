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

def returnVal(valVec,carPol,iniCars,epsDltBase)
    # Simulation START here
    while True:
        gg=[]
        for numCar1 in range(upCarNum):
            for numCar2 in range(upCarNum):
                oldVal = valVec[numCar1][numCar2]
                for reqCar1 in range(iniCarsUp[0]):
                    for reqCar2 in range(iniCarsUp[1]):
                        for turnCar1 in range(iniCarsUp[0]):
                            for turnCar2 in range(iniCarsUp[1]):
                                # for ss in range(3000):
                                iniCars[0] = numCar1
                                iniCars[1] = numCar2
                                arrProb1 = pef.poisProbDen(conArr[0], reqCar1)
                                arrProb2 = pef.poisProbDen(conArr[1], reqCar2)
                                turnProb1 = pef.poisProbDen(repArr[0], turnCar1)
                                turnProb2 = pef.poisProbDen(repArr[1], turnCar2)
                                joinProb = arrProb1 * arrProb2 *turnProb1 * turnProb2

                                epsDlt = 0.0
                                iniRaw = iniCars

                                diffNum = abs(iniCars[0] - iniCars[1])
                                tmpVal = valVec[iniCars[0]][iniCars[1]]
                                optSol = 0

                                tmpArr = [reqCar1,reqCar2]
                                tmpRep = [turnCar1,turnCar2]
                                iniCarsUp, mvNumAbs = rllt.moveCar(iniCars, action, upCarNum)
                                iniCarsUp, lostSale, rentVec = rllt.reallot(iniCarsUp, tmpArr, tmpRep,
                                                                            upCarNum)
                                vt = rllt.calVal(rentVec,mvNumAbs)
                                valBellTmp = joinProb * (vt + rhoVal * valVec[iniCarsUp[0]][iniCarsUp[1]])
                                nuVal = nuVal *(oo)/(oo+1) + float(valBellTmp / (oo+1))

                    # Policy improvement
            diffVal = abs(valVec[iniRaw[0]][iniRaw[1]] - oldVal)
            epsDlt = max(epsDlt,diffVal)
            gg.append(diffVal)
        if (max(gg) < epsDltBase) and (max(gg)>=0):
            break
    return valVec
