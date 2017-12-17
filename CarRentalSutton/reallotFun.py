
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

def calVal(rentVec,mvNumAbs):
    vt = 0
    for yy in rentVec:
        vt += yy * 10
    return vt - mvNumAbs * 2

def moveCar(iniCars,action, upCarNum):

    car1 = iniCars[0]
    car2 = iniCars[1]
    moveNum = action
    if (action > 0):
        action = min(action,car1,car2)
        car1 = max(car1 - action,0)
        car2 = min(car2 + action,upCarNum)
        moveNum =
    else:
        action = min(-action, car1, car2)
        car1 = min(car1 - action, upCarNum)
        car2 = max(car2 + action, 0)
    return [car1,car2], abs(moveNum)