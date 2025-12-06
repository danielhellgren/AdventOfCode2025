def parseKeyLine(file):
    splits = file.read().split("\n")
    keyLine = splits[len(splits)-1]

    chunks = []
    i = 0
    amountOfKeys = len(keyLine)

    while i < amountOfKeys:
        if keyLine[i].isspace():
            i += 1
            continue

        chunk = keyLine[i]
        i += 1

        while i < amountOfKeys and keyLine[i].isspace():
            chunk += keyLine[i]
            i += 1
        #cut separating space if not on last
        if(i < amountOfKeys):
           chunk = chunk[:-1] 
        chunks.append(chunk)

    return splits, chunks

def splitByKey(inStr, key):
    splits = []
    indexOffset = 0
    for i, part in enumerate(key):
        partSize = len(part)
        split = inStr[indexOffset:indexOffset+partSize]
        splits.append(split)
        indexOffset += partSize + 1

    return splits



def readInputToColumnList(file):
    columns = []
    splits, valueKey = parseKeyLine(file)

    for line in splits[:-1]:
        items = splitByKey(line , valueKey)
        if not items:
            continue
        while len(columns) < len(items):

            columns.append([])

        for i, item in enumerate(items):
            columns[i].append(item)

    return columns, valueKey
    
def rearrangeNumbers(valueList):
    newNumbers = []
    numbersSize = len(valueList[0])
    for i in range(numbersSize):
        number = ""
        for value in valueList:
            number += value[i]
        newNumbers.append(int(number))

    return newNumbers

def sumOpartionsLists(valueLists, operationList):
    totalSum = 0

    for i, valueList in enumerate(valueLists):
        operator = operationList[i][0]
        valueList = rearrangeNumbers(valueList)
        if(operator == "+"):
            totalSum += summation(valueList)
        if(operator == "*"):
            totalSum += multiplication(valueList)
    return totalSum

def summation(inputList):
    result = 0
    for x in inputList:
        result += x
    return result

def multiplication(inputList):
    result = 1
    for x in inputList:
        result *= int(x)
    return result

def main():
    with open("Day6_TrashCompactor\\input.txt", "r") as file:
        valueLists, operationList = readInputToColumnList(file)
        print(str(valueLists))
        totalSum = sumOpartionsLists(valueLists, operationList)
        print("Total: " + str(totalSum))

if __name__ == "__main__":
    main()