BEAM_CHAR = '|'
SPLITTER_CHAR = '^'
PASSTHROUGH_CHAR = '.'

def findBeamPositions(row):
    pos = []
    indexOffset = 0

    while True:
        searchWindow = row[indexOffset:]
        index = searchWindow.find(BEAM_CHAR)
        if index == -1:
            break
        pos.append(index+indexOffset)
        indexOffset += index + 1

    return pos

def replaceChar(s, pos, ch):
    if not (0 <= pos < len(s)):
        return s  # or raise IndexError
    return s[:pos] + ch + s[pos+1:]

def propagateBeams(splitterMap, index, beamPositions):
    if not (0 <= index < len(splitterMap)):
        return splitterMap, 0
    nextRow = splitterMap[index+1]
    splitCount = 0
    for beamPos in beamPositions:
        nextRowTile = nextRow[beamPos]
        if nextRowTile == PASSTHROUGH_CHAR:
            nextRow = replaceChar(nextRow, beamPos, BEAM_CHAR)
        if nextRowTile == SPLITTER_CHAR:
            nextRow = replaceChar(nextRow, beamPos - 1, BEAM_CHAR)
            nextRow = replaceChar(nextRow, beamPos + 1, BEAM_CHAR)
            splitCount += 1
        splitterMap[index+1] = nextRow

    return splitterMap, splitCount


def runRayTracing(splitterMap):
    firstRow = splitterMap[0].replace("S", BEAM_CHAR)
    mapSize = len(splitterMap)
    beamIndexes = findBeamPositions(firstRow)
    totalSplits = 0
    for index, row in enumerate(splitterMap):
        if index == mapSize-1:
            break
        if index == 0:
            row = splitterMap[0].replace("S", BEAM_CHAR)
        beamPos = findBeamPositions(row)
        splitterMap, splitCount = propagateBeams(splitterMap, index, beamPos)
        print(*splitterMap, sep="\n")
        print("beam was split x: " + str(splitCount))
        print("------")
        totalSplits += splitCount


    print("totalSplits: " + str(totalSplits))
    


def main():
    with open("Day7_Laboratories\\input.txt", "r") as file:
        splitterMap = file.read().split("\n")
        runRayTracing(splitterMap)


if __name__ == "__main__":
    main()