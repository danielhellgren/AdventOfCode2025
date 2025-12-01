def getPassword(turns):
    DIAL_INIT = 50
    dialValue = DIAL_INIT
    completedRotations = 0

    for turn in turns:
        completedRotations, dialValue = turnDial(completedRotations, dialValue, turn.replace("\n", ""))

    print(completedRotations)

def turnDial(completedRotations, dialValue, turn):
    DIAL_SIZE = 100
    isLeftTurn = turn[0] == "L"
    extraRotations = 0
    turnValue = int(turn[1:])
    if(turnValue > DIAL_SIZE):
        extraRotations, turnValue = divmod(turnValue, DIAL_SIZE)
    if(isLeftTurn):
        turnValue = -turnValue

    newDialValue = (dialValue + turnValue)
    passedZeroNotStartedFromZero = dialValue != 0 and (newDialValue <= 0 or newDialValue >= DIAL_SIZE)

    if(passedZeroNotStartedFromZero):
        extraRotations += 1

    newDialValue = newDialValue % DIAL_SIZE
    completedRotations += extraRotations

    return (completedRotations, newDialValue)

def main():
    file = open("Day1_SecretEntrance\\input.txt", "r")
    getPassword(file)

if __name__ == "__main__":
    main()