import numpy as np
import itertools as its
import pandas as pd

# Parameters
floorNum = 20
elevaNum = 10
ppNumPerFloor = 300

timePerFloor = 2
timeOpenWait = 5

outputFile = 'export_floor' + str(floorNum) + '_elevator_' + str(elevaNum) + '.csv'
floorAllot = [(ii + 1) for ii in range(elevaNum - 1)]
floorAllot.append(floorNum)

# This function compute the (time, avg_time) for any allocation scheme
def calTime(floorNum, elevaNum, ppNumPerFloor,
           timeOpenWait, timePerFloor, floorAllot):
    # The allocation scheme: floorAllot, like [3,6,10]
    checknum = 0
    timeSpend = []
    timeAllot = []
    # floorAllot.append(floorNum)
    for eleva_i in floorAllot:
        tmpTimeFloor = []
        # Break down the allocation scheme to floors
        if eleva_i == 0:
            timeSpend.append(0)
        else:
            if checknum < 1:
                floorPathEleva_i = [(ii + 1) for ii in range(eleva_i)]
            elif checknum < (elevaNum - 1):
                floorPathEleva_i = [(ii + 1) for ii in range(floorAllot[checknum - 1], floorAllot[checknum])]
            else:
                floorPathEleva_i = [(ii + 1) for ii in range(floorAllot[elevaNum - 2], floorNum + 1)]

            # Compute the running and openning time for each floor
            # floorEleva_i: the specific floor in the floor pool of elevator_i
            # floorPathEleva_i: the allocated floors for elevator_i
            for floorEleva_i in floorPathEleva_i:
                tmpTimeClimb = timePerFloor * floorEleva_i
                if checknum < 1:
                    climbNum = floorEleva_i
                else:
                    climbNum = floorEleva_i - floorAllot[checknum - 1]
                tmpTimeOpen = timeOpenWait * floorEleva_i
                tmpTimeClimb = (timeOpenWait + timePerFloor) * climbNum
                tmpTime = tmpTimeOpen + tmpTimeClimb
                tmpTimeFloor.append(tmpTime)
                timeSpend.append((tmpTime))
            timeAllot.append(np.mean(tmpTimeFloor))
        checknum = checknum + 1
    return timeAllot, np.mean(timeSpend)

# ff, ffMean = simRun(floorNum, elevaNum, ppNumPerFloor, timeOpenWait, timePerFloor, floorAllot)

# All possible combinations of the floor allocation to the elevators
# floorComb = its.combinations(range(1, (floorNum + 1)), (elevaNum - 1))
def allotGenerate(floorAllot,timeSpend,floorNum):
    tBase = 999999999
    changeNum = 0
    for ii in range(len(timeSpend)):
        if timeSpend[ii] < tBase:
            changeNum = (ii)
            tBase = timeSpend[ii]
    for ii in range(changeNum,(len(floorAllot)-1)):
        floorAllot[ii] = floorAllot[ii] + 1
    return floorAllot

def runSimulation(floorNum, elevaNum, ppNumPerFloor,timeOpenWait, timePerFloor):
    tmpDt = pd.DataFrame([{'time': 0}])
    tableFull = pd.DataFrame()
    # Save the allocation scheme to the Pandas Dataframe
    for cc in range(1, (elevaNum + 1)):
        tmpDt[('elev' + str(cc))] = cc
    # Save the spent time to the Pandas Dataframe
    for gg in range(1, (elevaNum + 1)):
        tmpDt[('elevTime' + str(gg))] = 0
    floorAllot = [(ii ) for ii in range(elevaNum - 1)]
    floorAllot[1] = 1
    # Fill the floors into the allocated elevators
    floorAllot.append(floorNum)
    timeSpend, ffMean = calTime(floorNum, elevaNum, ppNumPerFloor, \
                                timeOpenWait, timePerFloor, floorAllot)
    for dd in range(elevaNum+1):
        floorAllot = allotGenerate(floorAllot,timeSpend,floorNum)
        timeSpend, ffMean = calTime(floorNum, elevaNum, ppNumPerFloor, \
                             timeOpenWait, timePerFloor, floorAllot)

        for gg in range(1,(elevaNum+1)):
            tmpDt[('elev' + str(gg))] = floorAllot[gg-1]
            tmpDt[('elevTime' + str(gg))] = timeSpend[gg-1]
            tmpDt['time'] = ffMean
        tableFull = pd.concat([tableFull, tmpDt], ignore_index=True)
    tableFull.to_csv(outputFile, index=False)

# run the file
if __name__ == '__main__':
    runSimulation(floorNum, elevaNum, ppNumPerFloor, timeOpenWait, timePerFloor)