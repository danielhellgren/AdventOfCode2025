from collections import defaultdict
import matplotlib.pyplot as plt


def printCoordinates(coordinates):
    xs, ys = [], []

    for x, y_list in coordinates.items():

        for y in y_list:
            xs.append(x)
            ys.append(y)

    plt.scatter(xs, ys)

    #for x, y in zip(xs, ys):
    #    plt.annotate(f"({x}, {y})", (x, y),
    #                textcoords="offset points", xytext=(5, 5))

    plt.show()

def validateArea(left, right, bot, top, borders):
    leftYs = borders[left]
    rightYs = borders[right]
    overlapLeft = min(leftYs) > bot or max(leftYs) < top
    overlapRight = min(rightYs) > bot or max(rightYs) < top

    if (overlapLeft or overlapRight):
        return False
    for y in range(bot + 1, top):
        if y in borders[bot] or y in borders[top]:
            return False
    
    return True

def getLargestArea(coords, borders):
    largestArea = 0

    n = len(coords)
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i + 1, n):
            x2, y2 = coords[j]
            left = min(x1, x2)
            right = max(x1, x2)
            bot = min(y1, y2)
            top = max(y1, y2)
            
            dx = right - left + 1
            dy = top - bot + 1
            area = dx * dy
           
            if area > largestArea:
                validArea = validateArea(left, right, bot, top, borders)
                if validArea:
                    largestArea = area
            
    print("MAX: " + str(largestArea))

def findXNeighbour(x, y, coords): 
    for xN, yN in coords: 
        if x != xN and y == yN: 
            return xN, yN 
    return -1, -1

def getAreaBorder(coords):
    coordsGrpd = defaultdict(list)

    for x, y in coords:
        coordsGrpd[x].append(y)

    edges = []

    for x, yCoords in coordsGrpd.items():
        yStart = min(yCoords)
        yEnd = max(yCoords)
        edges.append((x, yStart))
        edges.append((x, yEnd))

        for y in range(yStart, yEnd):
            if y in yCoords:
                continue
            coordsGrpd[x].append(y)
    
    for i in range(len(edges)):
        if len(edges) <= 1:
            break
        edge = edges[0]
        x, y = edge
        xN, yN = findXNeighbour(x, y, edges)
        if(xN == -1):
            continue
        xStart = min(x, xN)
        xEnd = max(x, xN)

        for curX in range(xStart, xEnd):
            if y not in coordsGrpd[curX]:
                coordsGrpd[curX].append(y)
        edges.remove(edge)
        edges.remove((xN,yN))

    return coordsGrpd

def sortCoordinates(coordinates):
    coordinates.sort(key=lambda p: (p[0], p[1]))

def main():
    with open("Day9_MovieTheater\\input.txt", "r") as file:
        cinemaMap = [
            tuple(map(int, line.split(",")))
            for line in file.read().strip().splitlines()
            if line.strip()
        ]

        sortCoordinates(cinemaMap)
        areaBorder = getAreaBorder(cinemaMap)
        getLargestArea(cinemaMap, areaBorder)

        #printCoordinates(greenArea)

if __name__ == "__main__":
    main()