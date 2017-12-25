
import numpy as np

lamx = 2.0
mux = 2.0
horizon = 10

def arriveTime(lamx):
    gg = np.random.rand()
    tt = -np.log(1.0-gg)/lamx
    return tt

def transitFreq(iniCarNum,sampleSize,timeHo,lamx,mux):
    thVal = lamx / (mux + lamx)
    freqVec = np.zeros(timeHo)  # Vector of people served

    for nn in range(sampleSize):
        qNum = 0 # Number of queued people
        sNumt = 0 # Number of served people
        cNum = iniCarNum  # Number of present cars
        for qq in range(timeHo):
            mm = np.random.rand()
            if mm < thVal:
                # Event: new consumer arrives
                if cNum > 0:  # When there are cars available
                    sNum = min(qNum+1,cNum)
                    qNum = max(0,(qNum + 1 - sNum))
                    cNum = max(0,(cNum - sNum))
                else:
                    qNum += 1
                    sNum = 0
            else:
                # Event: new car returns
                if qNum>0:  # When there are people are requesting cars
                    sNum = min(qNum, cNum + 1)
                    qNum = max(0, (qNum - sNum - 1))
                    cNum = max(0, (cNum + 1 - sNum))
                else:
                    sNum = 0
                    cNum += 1
            sNumt += sNum
        freqVec[sNumt] += 1

    sumval = np.sum(freqVec)
    freqVec2 = [float(round((ww / sumval), 2)) for ww in freqVec]
    return (freqVec2)

def freqSerLeft(iniCarNum,sampleSize,timeHo,lamx,mux):
    thVal = lamx / (mux + lamx)
    freqVec = [list(np.zeros(timeHo)) for cc in range(timeHo)]  # Vector of people served
    for nn in range(sampleSize):
        qNum = 0 # Number of queued people
        sNumt = 0 # Number of served people
        cNum = iniCarNum  # Number of present cars
        for qq in range(timeHo):
            mm = np.random.rand()
            if mm < thVal:
                # Event: new consumer arrives
                if cNum > 0:  # When there are cars available
                    sNum = min(qNum+1,cNum)
                    qNum = max(0,(qNum + 1 - sNum))
                    cNum = max(0,(cNum - sNum))
                else:
                    qNum += 1
                    sNum = 0
            else:
                # Event: new car returns
                if qNum>0:  # When there are people are requesting cars
                    sNum = min(qNum, cNum + 1)
                    qNum = max(0, (qNum - sNum - 1))
                    cNum = max(0, (cNum + 1 - sNum))
                else:
                    sNum = 0
                    cNum += 1
            sNumt += sNum
        freqVec[sNumt][cNum] += 1

    sumval = np.sum(freqVec)
    freqVec2 = [[float(round((gg / sumval), 2)) for gg in ww] for ww in freqVec]
    return (freqVec2)

def transitFull(sampleSize,timeHo,lamx,mux):
    dd = [[transitFreq(ff,sampleSize,timeHo,lamx,mux)] for ff in range(timeHo)]
    return dd

if __name__ == '__main__':

    lamx = 2.0
    mux = 2.0
    iniCarNum = 2
    sampleSize = 1000
    timeHo = 20
    freqVec = transitFreq(iniCarNum,sampleSize,timeHo,lamx,mux)
    sumval = np.sum(freqVec)
    # freqVec2 = [float(round((ww / sumval),2)) for ww in freqVec]

    # print(freqVec2)
    #
    # dd = [[transitFreq(ff,sampleSize,timeHo,lamx,mux)] for ff in range(timeHo)]
    # print(dd)
    # ff = transitFull(sampleSize,timeHo,lamx,mux)
    # print(ff)
    #
    thVal = lamx / (mux + lamx)
    freqVec = [list(np.zeros(timeHo)) for cc in range(timeHo)]  # Vector of people served

    for nn in range(sampleSize):
        qNum = 0 # Number of queued people
        sNumt = 0 # Number of served people
        cNum = iniCarNum  # Number of present cars
        for qq in range(timeHo):
            mm = np.random.rand()
            if mm < thVal:
                # Event: new consumer arrives
                if cNum > 0:  # When there are cars available
                    sNum = min(qNum+1,cNum)
                    qNum = max(0,(qNum + 1 - sNum))
                    cNum = max(0,(cNum - sNum))
                else:
                    qNum += 1
                    sNum = 0
            else:
                # Event: new car returns
                if qNum>0:  # When there are people are requesting cars
                    sNum = min(qNum, cNum + 1)
                    qNum = max(0, (qNum - sNum - 1))
                    cNum = max(0, (cNum + 1 - sNum))
                else:
                    sNum = 0
                    cNum += 1
            sNumt += sNum
        freqVec[sNumt][cNum] += 1
        # stateVec[cNum - 1] += 1
    sumval = np.sum(freqVec)
    freqVec2 = [[float(round((gg / sumval), 3)) for gg in ww] for ww in freqVec]
    print(freqVec2)
    print(np.sum(freqVec2))
