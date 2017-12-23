
import numpy as np

lamx = 2.0
mux = 1.0
horizon = 10

def arriveTime(lamx):
    gg = np.random.rand()
    tt = -np.log(1.0-gg)/lamx
    return tt
gg = []
t0 = 0.0
for tt in range(horizon):
    t1 = arriveTime(lamx)
    gg.append(t1+t0)
    t0 += t1

sampleSize = 1000
timeHo = 20
thVal = lamx / (mux + lamx)
freqVec = np.zeros(timeHo)
for nn in range(sampleSize):
    qNum = 0
    sNum = 0
    for qq in range(timeHo):
        mm = np.random.rand()
        if mm < thVal:
            # Event: new consumer arrives
            qNum += 1
        else:
            if qNum>0:
                sNum += 1
                qNum -= 1
    freqVec[sNum] += 1
print(freqVec)
sumval = np.sum(freqVec)
freqVec2 = [round((ww / sumval),3) for ww in freqVec]
print(freqVec2)

# print(arriveTime(lamx))
# print(gg)