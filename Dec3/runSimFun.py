import numpy as np
import itertools as its
import pandas as pd
from calTimeFun import calTime
from allotFun import allotGenerate

def runSimulation(floorNum, elevaNum, ppNumPerFloor,timeOpenWait, timePerFloor,outputFile):
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
