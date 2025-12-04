def loadRollMap(content):
    map = []
    for row in content:
        map.append(row)

def checkAccessibleNumberOnRow(rollMap, rowNumber):
    LIMIT_ACCESSABLE = 4
    mapSize = len(rollMap)
    aboveRow = "..." if rowNumber == 0 else rollMap[rowNumber-1]
    currentRow = rollMap[rowNumber]
    belowRow = "..." if rowNumber == mapSize-1 else rollMap[rowNumber+1]
    rowSize = len(currentRow)
    accCount = 0
    for index in range(rowSize):
        if(currentRow[index] == "@"):
            leftIndex = index-1 if index > 0 else index
            rightIndex = index+2 if index < rowSize else index+1
            neighbours = ""
            #above
            if(rowNumber > 0):
                neighbours += aboveRow[leftIndex:rightIndex]
            #current
            neighbours += currentRow[leftIndex:rightIndex]
            #below
            if(rowNumber < mapSize):
                neighbours += belowRow[leftIndex:rightIndex]
            if(neighbours.count("@") < LIMIT_ACCESSABLE+1):
                accCount += 1

    return accCount

def countAccessiblePaperRolls(content):
    count = 0
    mapSize = len(content)

    for rowNumber in range(mapSize):
        count += checkAccessibleNumberOnRow(content, rowNumber)

    print("# of accessible rolls: " + str(count))

def main():
    with open("Day4_PrintingDepartment\\input.txt", "r") as file:
        content = file.read().split("\n")
        countAccessiblePaperRolls(content)

if __name__ == "__main__":
    main()