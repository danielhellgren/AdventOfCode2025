def checkValContainsOnlyDuplicateChunks(valStr, width):
    valLength = len(valStr)
    repeatedChunk = valStr[:width]
    amountOfChunks = int(valLength / width)

    return valStr == repeatedChunk * amountOfChunks

def scanForInvalidIdByWidth(valStr, scanWidth):
    valLength = len(valStr)
    valIsNotDivisibleByCurrentWidth = valLength % scanWidth != 0

    if(valIsNotDivisibleByCurrentWidth):

        return False
    
    valContainedOnlyDuplicates = checkValContainsOnlyDuplicateChunks(valStr, scanWidth)

    return valContainedOnlyDuplicates

def getInvalidValue(val):
    valStr = str(val)
    valLength = len(valStr)
    valLengthCantBeInvalid = valLength == 0

    if(valLengthCantBeInvalid):

        return 0
        
    valMiddleIndex = int(valLength/2)
    scanRange = range(1, valMiddleIndex+1)

    for scanWidth in scanRange:
        if scanForInvalidIdByWidth(valStr, scanWidth):
            
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