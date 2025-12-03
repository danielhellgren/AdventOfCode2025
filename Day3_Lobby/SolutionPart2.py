def sumBiggestBatteries(numbers):
    batterySum = 0
    NUMBER_OF_BATTERIES = 12

    for number in numbers:
        strNum = str(number)
        finalBattery = ""
        for n in reversed(range(1, NUMBER_OF_BATTERIES + 1)):
            if(n > 1):
                strNumLeftPart = strNum[:-(n-1)]
            else:
                strNumLeftPart = strNum
            largestDigitLeft = max(strNumLeftPart)
            indexOfLargestDigitLeft = strNumLeftPart.index(largestDigitLeft)
            strNumRightPart = strNum[indexOfLargestDigitLeft+1:]
            strNum = strNumRightPart
            finalBattery += largestDigitLeft

        largestBattery = int(finalBattery)
        batterySum += largestBattery

    print(batterySum)


def main():
    with open("Day3_Lobby\\input.txt", "r") as file:
        content = file.read().split("\n")
        sumBiggestBatteries(content)

if __name__ == "__main__":
    main()