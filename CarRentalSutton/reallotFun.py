
def reallot(iniCars,tmpArr,tmpRep,lostSale):

    for tt in range(len(iniCars)):
        lstIx = tt - 1
        if (iniCars[lstIx] - tmpArr[lstIx] + tmpRep[lstIx] > 0):
            iniCars[lstIx] = iniCars[lstIx] - tmpArr[lstIx] + tmpRep[lstIx]

        else:
            iniCars[lstIx] = 0
            lostSale[lstIx] += -(iniCars[lstIx] - (tmpArr[lstIx]) + tmpRep[lstIx])
    return iniCars,lostSale