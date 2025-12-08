import math

BOX_SPLIT_CHAR = ","
CONNECTION_LIMIT = 1000

def getDistance(box, compareBox):
    boxCoords = box.split(BOX_SPLIT_CHAR)
    compareCoords = compareBox.split(BOX_SPLIT_CHAR)

    dx =  int(compareCoords[0]) - int(boxCoords[0])
    dy =  int(compareCoords[1]) - int(boxCoords[1])
    dz = int(compareCoords[2]) - int(boxCoords[2])

    #print(f"DX: {dx}, DY: {dy}, DZ: {dz}")
    distance = math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2)
    #print(f"Resulting distance: {distance}")
    #print("---------")
    return math.ceil(distance)

def getDistances(uniqueBoxPairs, amountOfBoxes):
    distances = []
    amountOfpairs = len(uniqueBoxPairs)

    for i in range(amountOfpairs):
        curPair = uniqueBoxPairs[i]
        curBox = curPair[0]
        compBox = curPair[1]
        dist = getDistance(curBox, compBox)
        distances.append([curBox, compBox, int(dist)])

    distances.sort(key=lambda x: x[2])
    distances = distances[:CONNECTION_LIMIT+1]

    #print(str(distances))
    #print("-----")

    return distances

def findIndex(circuits, box):
    i = 0
    for circ in circuits:
        if box in circ:
            return i
        i += 1
    return -1

def connectCircuits(distance, circuits, connectedBoxes):
    toConnect = distance[1]
    connectToBox = distance[0]

    #if distance[0] not in connectedBoxes and distance[1] in connectedBoxes:
    #    toConnect = distance[0]
    #    connectToBox = distance[1]

    ind1 = findIndex(circuits, connectToBox)
    ind2 = findIndex(circuits, toConnect)

    if ind1 == ind2:
        #print(str(distance[0]) + " and " + str(distance[1]) + " are both already connected")
        #print("-----")
        return

    toConnectActual = circuits.pop(ind2)
    for values in toConnectActual:
        circuits[ind1].append(values)
    if(toConnect not in connectedBoxes):
        connectedBoxes.append(toConnect)
    if(connectToBox not in connectedBoxes):
        connectedBoxes.append(connectToBox)

def initCircuits(boxes):
    circuits = []
    for box in boxes:
        circuits.append([box])

    return circuits

def connectBoxes(distances, boxes):
    circuits = initCircuits(boxes)
    connectedBoxes = []

    for i, distance in enumerate(distances):
        
        connectCircuits(distance, circuits, connectedBoxes)
        total = sum(len(sub) for sub in circuits)
        if total != len(boxes):
            raise Exception("YOU LOST SOMETHING")
        if i >= CONNECTION_LIMIT-1:
            break
        
    circuits = sorted(circuits, key=len, reverse=True)
    n = 3
    res = 1
    for i in range(n):
        res *= len(circuits[i])

    #print(*circuits, sep="\n")
    print("result: " + str(res))

def getUniqueBoxPairs(boxes):
    pairs = []
    n = len(boxes)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append([boxes[i], boxes[j]])
    return pairs

def main():
    with open("Day8_Playground\\input.txt", "r") as file:
        boxes = file.read().split("\n")
        amountOfBoxes = len(boxes)
        uniqueBoxPairs = getUniqueBoxPairs(boxes)
        #print("Amount of pairs: " + str(len(uniqueBoxPairs)))
        #print()
        #print(*uniqueBoxPairs, sep="\n")
        distances = getDistances(uniqueBoxPairs, amountOfBoxes)
        connectBoxes(distances, boxes)


if __name__ == "__main__":
    main()