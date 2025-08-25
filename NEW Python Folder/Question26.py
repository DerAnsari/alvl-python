class Character:
    def __init__(self,N,X,Y):
        self.__Name = N
        self.__Xcoordinate = X
        self.__Ycoordinate = Y
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__Xcoordinate
    def GetY(self):
        return self.__Ycoordinate
    def ChangePosition(self,newX,newY):
        self.__Xcoordinate = self.__Xcoordinate + newX
        self.__Ycoordinate = self.__Ycoordinate + newY

characterArray = []
with open("TextFiles-P4/Characters.txt","r") as file:
    Name = file.readline().strip().lower()
    try:
        while Name:
            X_coordinate = int(file.readline().strip())
            Y_coordinate = int(file.readline().strip())
            charObj = Character(Name,X_coordinate,Y_coordinate)
            characterArray.append(charObj)
            Name = file.readline().strip().lower()
    except FileNotFoundError:
        print("File not found")

position = -1
while position == -1:
    characterInput = input("Enter character name to move: ").lower()
    for i in range(10):
        characterName = characterArray[i].GetName().lower()
        if characterName == characterInput:
            position = i
found = False
while not found:
    characterDirection = str(input("enter the directiopn you want your character to move").lower())
    if characterDirection == 'w' or characterDirection == 'a' or characterDirection == 's' or characterDirection == 'd':
        found = True

match characterDirection:
    case "w":
        characterArray[position].ChangePosition(-1,0)
    case "a":
        characterArray[position].ChangePosition(0,1)
    case "s":
        characterArray[position].ChangePosition(0,-1)
    case "d":
        characterArray[position].ChangePosition(1,0)

print(characterName, " has changed coordinate to X = ",
str(characterArray[position].GetX()), " Y = ",
str(characterArray[position].GetY()))