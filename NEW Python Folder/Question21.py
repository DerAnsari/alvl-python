class TreasureChest:
    # Private question : STRING
    #Private answer : INTEGER
    #Private points : INTEGER
    def __init__(self, q, n, p):
        self.__question = q
        self.__answer = n
        self.__points = p

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, ans):
        return int(self.__answer) == int(ans)

    def getPoints(self, attempts):
        match attempts:
            case 1:
                return self.__points
            case 2:
                return self.__points // 2
            case 3 | 4:
                return self.__points // 4
            case _:
                return 0 

def readData():
    global arrayTreasure
    try:
        with open("TextFiles-P4/TreasureChestData.txt", "r") as file:
            for _ in range(5):
                question = str(file.readline().strip())
                number = int(file.readline().strip())
                points = int(file.readline().strip())
                arrayTreasure.append(TreasureChest(question, number, points))  # <-- moved inside loop
    except FileNotFoundError:
        print("File not found")

arrayTreasure = []
readData()

choice = int(input("Enter question number, between 1 and 5 inclusively: "))
if 1 <= choice <= 5:
    attempt = 0
    result = False
    while not result:
        answer = int(input(arrayTreasure[choice-1].getQuestion() + " "))  # add space for neatness
        result = arrayTreasure[choice-1].checkAnswer(answer)
        attempt += 1 
    print(arrayTreasure[choice-1].getPoints(attempt))
else:
    print("Invalid choice!")
