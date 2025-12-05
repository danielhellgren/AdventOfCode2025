def checkIngredientIsFresh(ingredientNumber, freshList):
    for freshRange in freshList:
        freshRanges = freshRange.split("-")
        bot = freshRanges[0]
        top = freshRanges[1]
        if int(bot) <= int(ingredientNumber) <= int(top):
            return 1
    return 0
    

def countFreshIngredients(freshList, ingredientList):
    count = 0
    for ingredient in ingredientList:
        count += checkIngredientIsFresh(ingredient, freshList)

    print("# of fresh ingredients: " + str(count))

def main():
    with open("Day5_Cafeteria\\input.txt", "r") as file:
        content = file.read().split('\n\n', 1)
        freshList = content[0].split("\n")
        ingredientList = content[1].split("\n")
        countFreshIngredients(freshList, ingredientList)

if __name__ == "__main__":
    main()