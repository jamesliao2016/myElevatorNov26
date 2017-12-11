import numpy as np
import itertools as its
import pandas as pd
from allotFun import allotGenerate

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

