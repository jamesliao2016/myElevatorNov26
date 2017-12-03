import numpy as np
import itertools as its
import pandas as pd

# Parameters
floorNum = 30
elevaNum = 10
ppNumPerFloor = 300

timePerFloor = 2
timeOpenWait = 5

outputFile = 'export_floor' + str(floorNum) + '_elevator_' + str(elevaNum) + '.csv'
floorAlocation = [(ii + 1) for ii in range(elevaNum - 1)]
floorAlocation.append(floorNum)


# This function compute the (time, avg_time) for any allocation scheme
def calTime(floorNum, elevaNum, ppNumPerFloor,
           timeOpenWait, timePerFloor, floorAlocation):
    # The allocation scheme: floorAlocation, like [3,6,10]
    checknum = 0
    timeSpend = []
    # floorAlocation.append(floorNum)
    for eleva_i in floorAlocation:
        # Break down the allocation scheme to floors
        if checknum < 1:
            floorPathEleva_i = [(ii + 1) for ii in range(eleva_i)]
        elif checknum < (elevaNum - 1):
            floorPathEleva_i = [(ii + 1) for ii in range(floorAlocation[checknum - 1], floorAlocation[checknum])]
        else:
            floorPathEleva_i = [(ii + 1) for ii in range(floorAlocation[elevaNum - 2], floorNum + 1)]

        # Compute the running and openning time for each floor
        # floorEleva_i: the specific floor in the floor pool of elevator_i
        # floorPathEleva_i: the allocated floors for elevator_i
        for floorEleva_i in floorPathEleva_i:
            tmpTimeClimb = timePerFloor * floorEleva_i
            if checknum < 1:
                climbNum = floorEleva_i
            else:
                climbNum = floorEleva_i - floorAlocation[checknum - 1]
            tmpTimeOpen = timeOpenWait * floorEleva_i
            tmpTimeClimb = (timeOpenWait + timePerFloor) * climbNum
            tmpTime = tmpTimeOpen + tmpTimeClimb
            timeSpend.append(tmpTime)
        checknum = checknum + 1
    return timeSpend, np.mean(timeSpend)

# ff, ffMean = simRun(floorNum, elevaNum, ppNumPerFloor, timeOpenWait, timePerFloor, floorAlocation)

# All possible combinations of the floor allocation to the elevators
# floorComb = its.combinations(range(1, (floorNum + 1)), (elevaNum - 1))
def allotGenerate(floorAllot,timeSpend,floorNum):
    tBase = 999999999
    for ii in timeSpend:

        tt,tMean = calTime(floorNum, elevaNum, ppNumPerFloor, \
                        timeOpenWait, timePerFloor, floorAllot)
tmpTime = pd.DataFrame([{'time': 0}])

# Save the allocation scheme to the Pandas Dataframe
for cc in range(1, (elevaNum + 1)):
    tmpTime[('elevator' + str(cc))] = cc

# Save the spent time to the Pandas Dataframe
for cc in range(1, (floorNum + 1)):
    tmpTime[('floorTime' + str(cc))] = 0

# Compute all the (time,avg_time) and fill into the table
tableFull = pd.DataFrame()
for floorComb_i in floorComb:
    floorAllot = [(ii) for ii in floorComb_i]
    # Fill the floors into the allocated elevators
    floorAllot.append(floorNum)
    tt = 1
    for cc in (floorAllot):
        tmpTime[('elevator' + str(tt))] = cc
        tt = tt + 1

    ff, ffMean = calTime(floorNum, elevaNum, ppNumPerFloor, \
                        timeOpenWait, timePerFloor, floorAllot)

    for dd in range(floorNum):
        tmpTime[('floorTime' + str(dd))] = ff[dd]
    tmpTime['time'] = ffMean
    tableFull = pd.concat([tableFull, tmpTime], ignore_index=True)

# run the file
if __name__ == '__main__':
    tableFull.to_csv(outputFile, index=False)
