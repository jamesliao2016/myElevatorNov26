
import numpy as np
import itertools as its

floorNum = 21
elevaNum = 8
ppNumPerFloor = 300

timePerFloor = 2
timeOpenWait = 5

floorAlocation = [(ii + 1) for ii in range(elevaNum)]

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

floorComb = its.combinations(range(1,(floorNum+1)),(elevaNum-1))    
