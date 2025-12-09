import math

BOX_SPLIT_CHAR = ","

def getDistance(box, compareBox):
    boxCoords = box.split(BOX_SPLIT_CHAR)
    compareCoords = compareBox.split(BOX_SPLIT_CHAR)

    dx =  int(compareCoords[0]) - int(boxCoords[0])
    dy =  int(compareCoords[1]) - int(boxCoords[1])
    dz = int(compareCoords[2]) - int(boxCoords[2])

    distance = math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2)
 
    return math.ceil(distance)

def getDistances(boxes):
    distances = []
    amountOfBoxes = len(boxes)

    for i in range(amountOfBoxes):
        curBox = boxes[i]
        for j in range(i+1, amountOfBoxes):
            compBox = boxes[j]
            dist = getDistance(curBox, compBox)
            distances.append([curBox, compBox, int(dist)])

    distances.sort(key=lambda x: x[2])

    return distances

def findRoot(parent_map, box):

    if parent_map[box] == box:

        return box

    parent_map[box] = findRoot(parent_map, parent_map[box])
    return parent_map[box]

def unionCircuits(circuitsMap, box1, box2):

    root1 = findRoot(circuitsMap, box1)
    root2 = findRoot(circuitsMap, box2)

    if root1 != root2:

        circuitsMap[root1] = root2
        return True
    return False # 

def countNumberOfCircuits(circuitMap, boxes):
    unique_roots = set()
    for box in boxes:
        root = findRoot(circuitMap, box)
        unique_roots.add(root)
        
    return len(unique_roots)

def connectBoxes(distances, boxes):
    res = 0
    circuitsMap = {box: box for box in boxes}
    
    i = 0
    while True:
        if i >= len(distances):
            res = -1
            break
        box1, box2, dist = distances[i]
        merged = unionCircuits(circuitsMap, box1, box2)
        
        if(merged):
            amountOfCircuits = countNumberOfCircuits(circuitsMap, boxes)
        if amountOfCircuits == 1:
            x1, y1, z1 = box1.split(",", 3)
            x2, y2, z2 = box2.split(",", 3)
            res = int(x1) * int(x2)
            break
        i += 1
        
    
    print("result: " + str(res))

def getUniqueBoxPairs(boxes):
    pairs = []
    n = len(boxes)
    for i in range(n):
        for j in range(i + 1, n):
            
            pairs.append([boxes[i], boxes[j]])
    return pairs

def main():
    CONNECTION_LIMIT = 1000
    with open("Day8_Playground\\input.txt", "r") as file:
        boxes = file.read().strip().splitlines()

        distances = getDistances(boxes)
        connectBoxes(distances, boxes)


if __name__ == "__main__":
    main()