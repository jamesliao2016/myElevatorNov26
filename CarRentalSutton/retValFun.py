import poisEventFun as pef
import numpy as np
import reallotFun as rllt
import queueFun as qf

def returnVal(valVec,carPol,iniCars,epsDltBase,conArr,repArr,upCarNum,rhoVal,tm1,tm2):
    # Simulation START here
    while True:
        gg=[]
        # (numCar1,numCar2): the current cars of the two sites
        for numCar1 in range(upCarNum):
            for numCar2 in range(upCarNum):
                oldVal = valVec[numCar1][numCar2]
                iniCarsUp, mvNumAbs = rllt.moveCar(iniCars, carPol, upCarNum)

                # (reqCar1,reqCar2): the updated cars of the two sites
                for reqCar1 in range(upCarNum):
                    for reqCar2 in range(upCarNum):
                        arrProb1 = tm1[iniCarsUp[0]][reqCar1]
                        arrProb2 = tm2[iniCarsUp[1]][reqCar2]
                        joinProb = arrProb1 * arrProb2
                        vt = rllt.calVal(rentVec, mvNumAbs)
                        valBellTmp = joinProb * (vt + rhoVal * valVec[iniCarsUp[0]][iniCarsUp[1]])

                        epsDlt = 0.0
                                iniRaw = iniCars

                                diffNum = abs(iniCars[0] - iniCars[1])
                                tmpVal = valVec[iniCars[0]][iniCars[1]]
                                optSol = 0

                                tmpArr = [reqCar1,reqCar2]
                                tmpRep = [turnCar1,turnCar2]
                                nuVal = nuVal *(oo)/(oo+1) + float(valBellTmp / (oo+1))

                    # Policy improvement
                diffVal = abs(valVec[iniRaw[0]][iniRaw[1]] - oldVal)
                gg.append(diffVal)
        if (max(gg) < epsDltBase) and (max(gg)>=0):
            break
    return valVec
