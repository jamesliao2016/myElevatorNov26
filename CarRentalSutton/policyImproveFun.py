import poisEventFun as pef
import numpy as np
import reallotFun as rllt
import queueFun as qf
import retValFun as rvf

def polImprove(valVec,carPol,iniCars,epsDltBase,conArr,repArr,upCarNum,rhoVal,cm1,cm2,rm1,rm2):
    # Simulation START here
    carPolRlt = [[0 for x in range(upCarNum + 1)] for y in range(upCarNum + 1)]

    for numCar1 in range(upCarNum):
        for numCar2 in range(upCarNum):
            iniRaw = [numCar1,numCar2]
            iniCars = [numCar1, numCar2]
            oldVal = valVec[numCar1][numCar2]
            optVal = valVec[numCar1][numCar2]
            # optAction = carPol[numCar1][numCar2]
            for action in range(-5,6):
                iniCarsUp, mvNumAbs, polTmp = rllt.moveCar(iniCars, action, upCarNum)
                valBellTmp = 0.0
                for con1 in range(len(cm1)):
                    for con2 in range(len(cm2)):
                        for ret1 in range(len(rm1)):
                            for ret2 in range(len(rm2)):
                                tmpArr = [con1,con2]
                                tmpRep = [ret1,ret2]
                                iniCarsTmp, rentVec = rllt.reallot(iniCarsUp, tmpArr, tmpRep, upCarNum)
                                joinProb = cm1[con1] * cm2[con2] * rm1[ret1] * rm2[ret2]

                                vt = rllt.calVal(rentVec, mvNumAbs)
                                valBellTmp += joinProb * (vt + rhoVal * valVec[iniCarsTmp[0]][iniCarsTmp[1]])
                if valBellTmp > (optVal):
                    optVal = valBellTmp
                    # optAction = action
                    carPolRlt[numCar1][numCar2] = polTmp
    return carPolRlt

if __name__ == '__main__':
    import poisEventFun as pef
    import numpy as np
    import reallotFun as rllt
    import retValFun as rvf
    import queueFun as qf
    import time

    start_time = time.time()

    # Parameters
    locNum = 2
    conArr = [3, 4]
    repArr = [3, 2]
    upCarNum = 10
    rhoVal = 0.9
    epsEval = 0.1

    # Policy
    w, h = upCarNum, upCarNum;
    carPol = [[0 for x in range(w + 1)] for y in range(h + 1)]
    valVec = [[(0.0) for x in range(w + 1)] for y in range(h + 1)]

    # Simulation parameters
    simPeriod = 2
    iniCars = [10, 10]
    lostSale = [(i - i) for i in range(len(iniCars))]
    vt = 0
    mvNumAbs = 0
    epsDltBase = 1e-2
    epsDlt = 100
    ww = 1
    vtHist = [2]

    # Generate distribution
    arrBound = 10
    cm1 = [pef.poisProbDen(conArr[0],jj,arrBound) for jj in range(arrBound)]
    cm2 = [pef.poisProbDen(conArr[1], jj, arrBound) for jj in range(arrBound)]
    rm1 = [pef.poisProbDen(repArr[0], jj, arrBound) for jj in range(arrBound)]
    rm2 = [pef.poisProbDen(repArr[1], jj, arrBound) for jj in range(arrBound)]

    # Simulation START here
    yy = 0
    while yy<10:

        valVec = rvf.returnVal(valVec, carPol, iniCars, epsDltBase, conArr, repArr, upCarNum, rhoVal,cm1,cm2,rm1,rm2)
        print(valVec)
        print("--- %s seconds ---" % (time.time() - start_time))

        carPolNew = polImprove(valVec, carPol, iniCars, epsDltBase, conArr, repArr, upCarNum, rhoVal,cm1,cm2,rm1,rm2)
        print(carPolNew)
        print("--- %s seconds ---" % (time.time() - start_time))
        if carPolNew == carPol:
            break
        carPol = carPolNew
