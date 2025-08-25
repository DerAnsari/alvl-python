class Balloon:
    #PRIVATE Health : INTEGER
    #PRIVATE Colour : STRING
    #PRIVATE DefenceItem : STRING
    def __init__(self,C,D):
        self.__Health = 100
        self.__Colour = C
        self.__DefenseItem = D
    def getDefenseItem(self):
        return self.__DefenseItem
    def changeHealth(self,NewHealth):
        self.__Health = NewHealth
    def checkHealth(self):
        if self.__Health >= 0:
            return True
        else:
            return False
        
def defend(balloon):
    oppStrength = int(input("Enter the strength of the opponent"))
    newHealth = balloon.changeHealth(100-oppStrength)
    print(balloon.getDefenseItem())
    clashResult = balloon.checkHealth()
    if clashResult == True:
        print("Still Alive")
    else:
        print("dead :(")
    balloon.changeHealth(newHealth)
    

newbaloonDefenseItem = str(input("Enter your balloon defense item"))
newbaloonColor = str(input("Enter the balloon color"))
Baloon1 = Balloon(newbaloonColor,newbaloonDefenseItem)
defend(Baloon1)