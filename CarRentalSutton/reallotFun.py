
def reallot(iniCars,tmpArr,tmpRep,lostSale,upCarNum):
    rentVec = []
    for tt in range(len(iniCars)):
        lstIx = tt - 1
        if (iniCars[lstIx] - tmpArr[lstIx] + tmpRep[lstIx] > 0):
            rentNum = tmpArr[lstIx]
            iniCars[lstIx] = iniCars[lstIx] - tmpArr[lstIx] + tmpRep[lstIx]
            iniCars[lstIx] = min(iniCars[lstIx],upCarNum)

        else:
            iniCars[lstIx] = 0
            rentNum = iniCars[lstIx]
            lostSale[lstIx] += -(iniCars[lstIx] - (tmpArr[lstIx]) + tmpRep[lstIx])
        rentVec.append(rentNum)
    return iniCars,lostSale,rentVec

def calVal(vt,rentVec,mvNumAbs):
    for yy in rentVec:
        vt += yy * 10
    return vt - mvNumAbs * 2

def moveCar(iniCars,carPol):
    car1 = iniCars[0]
    car2 = iniCars[1]
    moveNum = carPol[car1][car2]
    if abs(moveNum) > 5:
        moveNum = 5 * moveNum /abs(moveNum)
    iniCars[0] -= moveNum
    iniCars[1] += moveNum
    return iniCars, abs(moveNum)