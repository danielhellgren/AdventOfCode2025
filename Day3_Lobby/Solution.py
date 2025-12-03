def sumBiggestBatteries(numbers):
    batterySum = 0

    for number in numbers:
        strNum = str(number)
        strNumLeftPart = strNum[:-1]
        largestDigitLeft = max(strNumLeftPart)
        indexOfLargestDigitLeft = strNumLeftPart.index(largestDigitLeft)
        strNumRightPart = strNum[indexOfLargestDigitLeft+1:]
        largestDigitRight = max(strNumRightPart)
        #print("largest Battery Left Side: " + largestDigitLeft + " on index " + str(indexOfLargestDigitLeft))
        #print("largest battery Right Side (" + strNumRightPart + ") " + largestDigitRight)
        largestBattery = int(largestDigitLeft + largestDigitRight)
        batterySum += largestBattery

    print(batterySum)


def main():
    with open("Day3_Lobby\\input.txt", "r") as file:
        content = file.read().split("\n")
        sumBiggestBatteries(content)

if __name__ == "__main__":
    main()