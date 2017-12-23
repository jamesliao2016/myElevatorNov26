import poisEventFun as pef
import numpy as np
import reallotFun as rllt

def returnVal(valVec,carPol,iniCars,epsDltBase,conArr,repArr,upCarNum,rhoVal)
    # Simulation START here
    while True:
        gg=[]
        for numCar1 in range(upCarNum):
            for numCar2 in range(upCarNum):
                oldVal = valVec[numCar1][numCar2]
                for reqCar1 in range(iniCars[0]):
                    for reqCar2 in range(iniCars[1]):
                        for turnCar1 in range(iniCars[0]):
                            for turnCar2 in range(iniCars[1]):
                                arrProb1 = pef.poisProbDen(conArr[0], reqCar1,upCarNum)
                                arrProb2 = pef.poisProbDen(conArr[1], reqCar2,upCarNum)
                                turnProb1 = pef.poisProbDen(repArr[0], turnCar1,upCarNum)
                                turnProb2 = pef.poisProbDen(repArr[1], turnCar2,upCarNum)
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
                gg.append(diffVal)
        if (max(gg) < epsDltBase) and (max(gg)>=0):
            break
    return valVec
