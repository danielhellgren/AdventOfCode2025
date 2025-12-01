def main():
    file = open("Day1_SecretEntrance\input.txt", "r")
    getPassword(file)

def getPassword(turns):
    dialValue = 50
    zerosHit = 0
    for turn in turns:
        zerosHit, dialValue = turnDial(zerosHit, dialValue, turn)
    print(zerosHit)

def turnDial(zerosHit, dialValue, turn):
    DIAL_SIZE = 100
    isLeftTurn = turn[0:1] == "L"
    turnValue = int(turn[1:].replace("\n", ""))
    if(isLeftTurn):
        turnValue = -turnValue
    newDialValue = (dialValue + turnValue) % DIAL_SIZE
    if(newDialValue == 0):
        zerosHit += 1

    return (zerosHit, newDialValue)

if __name__ == "__main__":
    main()