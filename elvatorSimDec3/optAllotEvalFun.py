def allotEvaluate(floorAllot,ffMean,optAllot,optValue):
    if ffMean < optValue:
        optAllot = floorAllot
        optValue = ffMean
    return optAllot,optValue