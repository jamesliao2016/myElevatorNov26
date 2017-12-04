import numpy as np
import itertools as its
import pandas as pd
# Parameters

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
