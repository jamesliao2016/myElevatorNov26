
import numpy as np
import itertools as its

floorNum = 21
elevaNum = 8
ppNumPerFloor = 300

timePerFloor = 2
timeOpenWait = 5

floorAlocation = [(ii + 1) for ii in range(elevaNum)]

# This function compute the (time, avg_time) for any allocation scheme
def simRun(floorNum,elevaNum,ppNumPerFloor,
           timeOpenWait,timePerFloor,floorAlocation):
    for eleva_i in range(elevaNum):
        floorPathEleva_i = [(ii + 1) for ii in range(eleva_i)]
        timeSpend = []
        for floorEleva_i in floorPathEleva_i:
            tmpTime = (timeOpenWait + timePerFloor) * floorEleva_i
            timeSpend.append(tmpTime)
    return timeSpend,np.mean(timeSpend)
    
ff,ffMean = simRun(floorNum,elevaNum,ppNumPerFloor,timeOpenWait,timePerFloor,floorAlocation)

# All possible combinations of the floor allocation to the elevators
floorComb = its.combinations(range(1,(floorNum+1)),(elevaNum-1))    

# Compute all the (time,avg_time) and fill into the table
for floorComb_i in floorComb:
    floorAlocation = [(ii + 1) for ii in floorComb_i]
    ff,ffMean = simRun(floorNum,elevaNum,ppNumPerFloor,timeOpenWait,timePerFloor,floorAlocation)


    
