import datetime


class Character:
    # self.__CharacterName : STRING
    # self.__DateOfBirth : STRING
    # self.__Intelligence : STRING
    # self.__Speed : INTEGER

    def __init__(self,N,Date,I,S):
        self.__CharacterName = N
        self.__DateOfBirth = Date
        self.__Intelligence = I
        self.__Speed = S

    def SetIntelligence(self,newI):
        self.__Intelligence = newI
    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year

    def Learn(self):
        self.__Intelligence = (self.__Intelligence * 1.1)

class MagicCharacter(Character):
    def __init__(self,E,N,Date,I,S):
        super().__init__(N,Date,I,S)
        self.__Element = E

    def Learn(self):
        match self.__Element:
            case "fire" | "water":
                super().SetIntelligence(super().GetIntelligence() * 1.2)
            case "earth":
                super().SetIntelligence(super().GetIntelligence() * 1.3)
            case _ :
                super().SetIntelligence(super().GetIntelligence() * 1.1)


FirstCharacter = Character("Royal", datetime.datetime(2019,1,1), 70, 30)
FirstCharacter.Learn()
print(FirstCharacter.GetName(), "is", FirstCharacter.ReturnAge(), "years old and has intelligence" , FirstCharacter.GetIntelligence())

FirstMagic = MagicCharacter("fire", "Light", datetime.datetime(2018, 3, 3), 75, 22)
FirstMagic.Learn()
print(FirstMagic.GetName(), "is", FirstMagic.ReturnAge(), "years old and has intelligence",FirstMagic.GetIntelligence())