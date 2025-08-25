class Character:
    def __init__(self,N,X,Y):
        self.__Name = N
        self.__XPosition = X
        self.__YPosition = Y

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self,nX):
        self.__XPosition += nX
        if (self.__XPosition < 0):
            self.__XPosition = 0
        elif (self.__XPosition > 10000):
            self.__XPosition = 10000

    def SetYPosition(self,nY):
        self.__YPosition += nY
        if (self.__YPosition < 0):
            self.__YPosition = 0
        elif (self.__YPosition > 10000):
            self.__YPosition = 10000

    def Move(self,Direction):
        if (Direction == "right" or Direction == "left") :
            if (Direction == "right"):
                Character.SetXPosition(10)
            else:
                Character.SetXPosition(-10)
        else:
            if (Direction == "Up"):
                Character.SetYPosition(10)
            else:
                Character.SetYPosition(-10)

class BikeCharacter(Character):
    def __init__(self,N,X,Y):
        super().__init__(N,X,Y)

    def Move(self,Direction):
        if (Direction == "right" or Direction == "left") :
            if (Direction == "right"):
                super().SetXPosition(20)
            else:
                super().SetXPosition(-20)
        else:
            if (Direction == "Up"):
                super().SetYPosition(20)
            else:
                super().SetYPosition(-20)

CharJack = Character("Jack",50,50)
CharKarla = BikeCharacter("Karla",100,50)

UsrChar = input("Which of the two character would you like to move?").lower()
UsrDirection = input("Chose which direction you would like to move the char to")
if UsrChar == "jack":
    CharJack.Move(UsrDirection)
    print("Jack's new position is X =", CharJack.GetXPosition(), "Y =", CharJack.GetYPosition())
else:
    CharKarla.Move(UsrDirection)
    print("Karla's new position is X =", CharKarla.GetXPosition(), "Y =", CharKarla.GetYPosition())