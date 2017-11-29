
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
    # The allocation scheme
    for eleva_i in range(floorNum):
        # Break down the allocation scheme to floors
        floorPathEleva_i = [(ii + 1) for ii in range(eleva_i)]
        timeSpend = []
        # Compute the running and openning time for each floor
        for floorEleva_i in floorPathEleva_i:
            tmpTime = (timeOpenWait + timePerFloor) * floorEleva_i
            timeSpend.append(tmpTime)
    return timeSpend,np.mean(timeSpend)
    
ff,ffMean = simRun(floorNum,elevaNum,ppNumPerFloor,timeOpenWait,timePerFloor,floorAlocation)

# All possible combinations of the floor allocation to the elevators
floorComb = its.combinations(range(1,(floorNum+1)),(elevaNum))    

import pandas as pd
tmpTime = pd.DataFrame([{'time':0}])

# Save the allocation scheme to the Pandas Dataframe
for cc in range(1,(elevaNum+1)):
    tmpTime[('elevator'+str(cc))] = cc

# Save the spent time to the Pandas Dataframe
for cc in range(1,(floorNum+1)):
    tmpTime[('floorTime'+str(cc))] = 0

# Compute all the (time,avg_time) and fill into the table
tableFull = pd.DataFrame()
for floorComb_i in floorComb:
    # Fill the floors into the allocated elevators
    tt = 1
    for cc in (floorComb_i):
        tmpTime[('elevator'+str(tt))] = cc
        tt =tt+1
    floorAlocation = [(ii) for ii in floorComb_i]
    ff,ffMean = simRun(floorNum,elevaNum,ppNumPerFloor,\
                       timeOpenWait,timePerFloor,floorAlocation)
        
    for cc in range(floorNum):
        tmpTime[('floorTime'+str(cc))] = ff[cc-1]
    tmpTime['time'] = ffMean
    tableFull = pd.concat([tableFull, tmpTime],ignore_index =True)

