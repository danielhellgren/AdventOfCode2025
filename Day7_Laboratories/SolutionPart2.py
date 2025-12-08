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

def addBeamOnPos(s, pos):
    if not (0 <= pos < len(s)):
        return s
    return s[:pos] + BEAM_CHAR + s[pos+1:]

def propagateBeams(splitterMap, index, beams, beamPositions):
    if not (0 <= index < len(splitterMap)):
        return splitterMap, 0
    
    nextRow = splitterMap[index+1]

    for beamPos in beamPositions:
        currentBeamCount = beams[index][beamPos]
        nextRowTile = nextRow[beamPos]

        if nextRowTile != SPLITTER_CHAR:
            nextRow = addBeamOnPos(nextRow, beamPos)
            beams[index+1][beamPos] += currentBeamCount

        if nextRowTile == SPLITTER_CHAR:
            nextRow = addBeamOnPos(nextRow, beamPos - 1)
            nextRow = addBeamOnPos(nextRow, beamPos + 1)
            beams[index+1][beamPos - 1] += currentBeamCount
            beams[index+1][beamPos + 1] += currentBeamCount
            
    splitterMap[index+1] = nextRow
        
    return splitterMap, beams

def runRayTracing(splitterMap):
    rows = len(splitterMap)
    cols = len(splitterMap[0])
    beams = [[0 for _ in range(cols)] for _ in range(rows)]
    startindex = splitterMap[0].find("S")
    beams[0][startindex] = 1

    for index, row in enumerate(splitterMap):

        if index == rows-1:
            break

        if index == 0:
            row = splitterMap[0].replace("S", BEAM_CHAR)
            
        beamPos = findBeamPositions(row)
        splitterMap, beams = propagateBeams(splitterMap, index, beams, beamPos)

    print(str(sum(beams[rows-1])))

def main():
    with open("Day7_Laboratories\\input.txt", "r") as file:
        splitterMap = file.read().split("\n")
        runRayTracing(splitterMap)


if __name__ == "__main__":
    main()