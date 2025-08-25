Scores = [None]*11
Names = [None]*11
ScoreInfo = [Scores, Names]

def ReadHighScores():
    try:
        with open("TextFiles-P4/HighScore.txt", "r") as file:
            for index, line in enumerate(file):
                if index >= 22:
                    break
                info = line.strip()
                if index % 2 == 0:
                    Names[index // 2] = info
                else:
                    Scores[index // 2] = info
    except FileNotFoundError:
        print("File not Found")

def OutputHighScores():
    for col in range(len(ScoreInfo[0])):
        colItem = [ScoreInfo[1][col], ScoreInfo[0][col]]
        print(" ".join(map(str, colItem)))


def AddNewScore(name, score):
    NewScoreList = [ScoreInfo[0][:], ScoreInfo[1][:]]
    if None in NewScoreList[0]:
        emptyidx = NewScoreList[0].index(None)
    else:
        emptyidx = len(NewScoreList[0])

    NewScoreList[0][emptyidx] = score
    NewScoreList[1][emptyidx] = name

    for index in range(len(NewScoreList[0]) - 1):
        for i in range(len(NewScoreList[0]) - 1 - index):
            if int(NewScoreList[0][i]) < int(NewScoreList[0][i + 1]):

                NewScoreList[0][i], NewScoreList[0][i + 1] = NewScoreList[0][i + 1], NewScoreList[0][i]
                NewScoreList[1][i], NewScoreList[1][i + 1] = NewScoreList[1][i + 1], NewScoreList[1][i]
    NewScoreList[0] = NewScoreList[0][:10]
    NewScoreList[1] = NewScoreList[1][:10]
    ScoreInfo[0] = NewScoreList[0]
    ScoreInfo[1] = NewScoreList[1]


def main():
    check = True
    while check:
        name = input("Enter name (3 letters)").upper()
        score = input("Enter Score (1-100000)")

        if len(name) != 3:
            print("Incorrect name. Name must be exactly 3 letters.")
        elif not score.isdigit() or int(score) > 100000 or int(score) < 1:
            print("Invalid score. Score must be between 1 and 100000.")
        else:
            check = False

    ReadHighScores()
    OutputHighScores()
    AddNewScore(name, int(score))
    print("\nUpdated High Scores:")
    OutputHighScores()


if __name__ == '__main__':
    main()
