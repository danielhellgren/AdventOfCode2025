def readInputToColumnList(file):
    columns = []

    for line in file:
        items = line.split()
        if not items:
            continue
        while len(columns) < len(items):
            columns.append([])
        for i, item in enumerate(items):
            columns[i].append(item)

    return columns
    
def sumOpartionsLists(operationsLists):
    totalSum = 0

    for operationList in operationsLists:
        operator = operationList.pop(len(operationList)-1)
        if(operator == "+"):
            totalSum += summation(operationList)
        if(operator == "*"):
            totalSum += multiplication(operationList)
    return totalSum

def summation(inputList):
    result = 0
    for x in inputList:
        result += int(x)
    return result

def multiplication(inputList):
    result = 1
    for x in inputList:
        result *= int(x)
    return result

def main():
    with open("Day6_TrashCompactor\\input.txt", "r") as file:
        operationsLists = readInputToColumnList(file)
        print(str(operationsLists))
        totalSum = sumOpartionsLists(operationsLists)
        print("Total: " + str(totalSum))

if __name__ == "__main__":
    main()