def checkAccessibleNumberOnRow(rollMap, rowNumber):
    LIMIT_ACCESSABLE = 4
    mapSize = len(rollMap)
    aboveRow = "" if rowNumber == 0 else rollMap[rowNumber-1]
    currentRow = rollMap[rowNumber]
    belowRow = "" if rowNumber == mapSize-1 else rollMap[rowNumber+1]
    rowSize = len(currentRow)
    accCount = 0
    newRow = ""
    
    for index in range(rowSize):
        if(currentRow[index] == "@"):
            leftIndex = index-1 if index > 0 else index
            rightIndex = index+2 if index < rowSize else index+1
            neighbours = ""
            if(rowNumber > 0):
                neighbours += aboveRow[leftIndex:rightIndex]
            neighbours += currentRow[leftIndex:rightIndex]
            if(rowNumber < mapSize):
                neighbours += belowRow[leftIndex:rightIndex]
            if(neighbours.count("@") <= LIMIT_ACCESSABLE):
                accCount += 1
                newRow += "x"
            else:
                newRow += "@"
        else:
            newRow += "."

    return accCount, newRow

def countAccessiblePaperRolls(content):
    count = 0
    mapSize = len(content)
    rollMap = content
    
    while(True):
        newMap = []
        for rowNumber in range(mapSize):
            n, newRow = checkAccessibleNumberOnRow(rollMap, rowNumber)
            count += n
            newMap.append(newRow)
        if(newMap == rollMap):
            break
        rollMap = newMap

    print("# of accessible rolls: " + str(count))

def main():
    with open("Day4_PrintingDepartment\\input.txt", "r") as file:
        content = file.read().split("\n")
        countAccessiblePaperRolls(content)

if __name__ == "__main__":
    main()