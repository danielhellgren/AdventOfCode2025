def getInvalidValue(val):
    valStr = str(val)
    valLength = len(valStr)
    valLengthCantBeInvalid = valLength == 0 or valLength % 2 != 0
    if(valLengthCantBeInvalid):
        return 0
    valMiddleIndex = int(valLength/2)
    valPart1 = valStr[:valMiddleIndex]
    valPart2 = valStr[valMiddleIndex:]
    if(valPart1 == valPart2):
        return val
    return 0
    
def getPartialSum(fromAndTo):
    partialSum = 0
    fromVal = int(fromAndTo[0])
    to = int(fromAndTo[1]) + 1
    for val in range(fromVal, to):
        partialSum += getInvalidValue(val)
    return partialSum

def sumInvalidIds(inputIdRanges):
    idRanges = inputIdRanges.split(",")
    invalidSum = 0
    for idRange in idRanges:
        fromAndTo = idRange.split("-")
        invalidSum += getPartialSum(fromAndTo)

    print("Sum of Invalid: " + str(invalidSum))


def main():
    with open("Day2_GiftShop\\input.txt", "r") as file:
        content = file.read().replace("\n", "")
        sumInvalidIds(content)

if __name__ == "__main__":
    main()