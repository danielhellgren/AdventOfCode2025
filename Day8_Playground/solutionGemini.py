import math
import sys

# Increase recursion depth limit for DSU path compression if input is huge
# sys.setrecursionlimit(2000) 

BOX_SPLIT_CHAR = ","

# --- Helper Functions (Your Style) ---

def getDistance(box, compareBox):
    # Note: Assumes box/compareBox are the original strings
    boxCoords = box.split(BOX_SPLIT_CHAR)
    compareCoords = compareBox.split(BOX_SPLIT_CHAR)

    dx = int(compareCoords[0]) - int(boxCoords[0])
    dy = int(compareCoords[1]) - int(boxCoords[1])
    dz = int(compareCoords[2]) - int(boxCoords[2])

    # The problem uses straight-line distance squared for comparison
    distance_sq = math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2)
    return math.ceil(distance_sq)

def getDistances(boxes):
    distances = []
    amountOfBoxes = len(boxes)

    for i in range(amountOfBoxes):
        curBox = boxes[i]
        for j in range(i+1, amountOfBoxes):
            compBox = boxes[j]
            dist = getDistance(curBox, compBox)
            # Store references to the original box strings
            distances.append([curBox, compBox, int(dist)])

    # Sort by the distance (index 2)
    distances.sort(key=lambda x: x[2])

    return distances

def find_root(parent_map, box):
    """Finds the representative/root of the circuit the box belongs to, with path compression."""
    if parent_map[box] == box:
        return box
    # Path compression: make the node point directly to the root
    parent_map[box] = find_root(parent_map, parent_map[box])
    return parent_map[box]

def union_circuits(parent_map, box1, box2):
    """Merges the circuits of box1 and box2 if they are not already in the same circuit."""
    root1 = find_root(parent_map, box1)
    root2 = find_root(parent_map, box2)

    if root1 != root2:
        # Merge by arbitrarily assigning one root to the other's parent
        parent_map[root1] = root2
        return True # Merge occurred
    return False # No merge needed

def connectBoxes(distances, boxes, connectionLimit):
    # Initialize every box to be its own parent (its own circuit)
    parent_map = {box: box for box in boxes}

    # Process exactly the first 'connectionLimit' shortest distances
    for i in range(connectionLimit):
        if i >= len(distances):
            break
        
        # Get the next closest pair from the sorted list
        box1_str, box2_str, dist = distances[i]
        
        # Attempt to union (merge) their circuits
        # The union function handles the 'if they are already connected' logic
        union_circuits(parent_map, box1_str, box2_str)
        
    # After processing all 1000 connections, calculate circuit sizes
    
    # We need to consolidate the final sizes
    final_circuit_sizes = {}
    for box in boxes:
        root = find_root(parent_map, box)
        if root not in final_circuit_sizes:
            final_circuit_sizes[root] = 0
        final_circuit_sizes[root] += 1
    
    # Sort sizes descending
    sorted_sizes = sorted(final_circuit_sizes.values(), reverse=True)

    # Multiply the top 3 largest circuits
    n = 3
    res = 1
    for i in range(n):
        if i < len(sorted_sizes):
            print(f"size {i+1}: " + str(sorted_sizes[i]))
            res *= sorted_sizes[i]
        else:
            break

    print("result: " + str(res))


def main():
    CONNECTION_LIMIT = 1000
    # Make sure your input file path is correct
    with open("Day8_Playground\\input.txt", "r") as file:
        boxes = file.read().strip().splitlines()

        distances = getDistances(boxes)
        connectBoxes(distances, boxes, CONNECTION_LIMIT)


if __name__ == "__main__":
    main()
