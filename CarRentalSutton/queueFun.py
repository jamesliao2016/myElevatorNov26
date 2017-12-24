
import numpy as np

lamx = 2.0
mux = 2.0
horizon = 10

def arriveTime(lamx):
    gg = np.random.rand()
    tt = -np.log(1.0-gg)/lamx
    return tt

def transitFreq(iniCarNum,sampleSize,timeHo,lamx,mux):
    # iniCarNum = 10
    # sampleSize = 1000
    # timeHo = 20
    thVal = lamx / (mux + lamx)
    freqVec = np.zeros(timeHo)
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
    return (freqVec)

if __name__ == '__main__':

    lamx = 2.0
    mux = 2.0
    iniCarNum = 20
    sampleSize = 1000
    timeHo = 20
    freqVec = transitFreq(iniCarNum,sampleSize,timeHo,lamx,mux)
    sumval = np.sum(freqVec)
    freqVec2 = [(round((ww / sumval),1)) for ww in freqVec]
    freqVec2 = [(round(ww,1)) for ww in freqVec2]
    print(freqVec2)
