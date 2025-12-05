def getRange(rangeStr):
   
    rangeParts = rangeStr.split("-")
    bot = int(rangeParts[0])
    top = int(rangeParts[1])
    
    return bot, top

def mergeRanges(freshList):
    ranges = [getRange(r) for r in freshList]
    ranges.sort(key=lambda x: x[0])
    merged = []
    curBot, curTop = ranges[0]

    for nextBot, nextTop in ranges[1:]:
        if curTop >= nextBot:
            curTop = max(curTop, nextTop)
        else:
            merged.append((curBot, curTop))
            curBot, curTop = nextBot, nextTop

    merged.append((curBot, curTop))

    return merged
        

def countUniqueFreshIngredients(freshList):
    amountOfFresh = 0

    mergedRanges = mergeRanges(freshList)

    for bot, top in mergedRanges:
        n = top - bot + 1
        amountOfFresh += n

    print("# of fresh ingredients: " + str(amountOfFresh))

def main():
    with open("Day5_Cafeteria\\input.txt", "r") as file:
        content = file.read().split('\n\n', 1)
        freshList = content[0].split("\n")
        countUniqueFreshIngredients(freshList)

if __name__ == "__main__":
    main()