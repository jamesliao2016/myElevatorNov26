import numpy as np
import itertools as its
import pandas as pd
from runSimFun import runSimulation
from allotFun import allotGenerate
from calTimeFun import calTime

# Parameters
floorNum = 20
elevaNum = 10
ppNumPerFloor = 300

timePerFloor = 2
timeOpenWait = 5

outputFile = 'export_floor' + str(floorNum) + '_elevator_' + str(elevaNum) + '.csv'
floorAllot = [(ii + 1) for ii in range(elevaNum - 1)]
floorAllot.append(floorNum)

# run the file
if __name__ == '__main__':
    runSimulation(floorNum, elevaNum, ppNumPerFloor, timeOpenWait, timePerFloor,outputFile)