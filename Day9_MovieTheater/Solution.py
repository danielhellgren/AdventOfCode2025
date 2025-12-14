import math

def getAreas(cinemaMap):
    areas = []
    cinemaSize = len(cinemaMap)
    for i in range(cinemaSize):
        x1, y1 = cinemaMap[i].split(",", 2)

        for j in range(i+1, cinemaSize):
            x2, y2 = cinemaMap[j].split(",", 2)
            dx = abs(int(x1) - int(x2)) + 1
            dy = abs(int(y1) - int(y2)) + 1
            area = dx * dy
            areas.append((cinemaMap[i], cinemaMap[j], area))

    return areas

def getLargestArea(cinemaMap):
    
    areas = getAreas(cinemaMap)
    areas.sort(key=lambda x: x[2], reverse=True)
    #print(str(areas))
    print("Largest Area: " + str(areas[0]))
    

def main():
    CONNECTION_LIMIT = 10
    with open("Day9_MovieTheater\\input.txt", "r") as file:
        cinemaMap = file.read().strip().splitlines()

        
        getLargestArea(cinemaMap)


if __name__ == "__main__":
    main()