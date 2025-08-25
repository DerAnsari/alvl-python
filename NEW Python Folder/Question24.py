class Card:
    def __init__(self):
        self.Number = 0
        self.Colour = ""

    def Constructor(self,N,C):
        self.Number = N
        self.Colour = C

    def GetNumber(self):
        return self.Number
    
    def GetColour(self):
        return self.Colour
    def __str__(self):
        return f"Card(Number={self.Number}, Colour={self.Colour})"

Choice = [] 
CardArray = [Card() for _ in range(30)]
    
def ChoseCard(Num):
    global Choice , CardArray

    if Num > 0 and Num <= 30 : 
        if Num in Choice:
            print("Already CHose Chose another one")
            return -1
        Choice.append(Num)
        return CardArray[Num - 1]
    else:
        print("Invalid Range Try again")
        return -1

def main():   
    global Choice, CardArray
    Player1 = [Card() for _ in range(4)]

    with open("TextFiles-P4/CardValues.txt") as file:
        
        for i in range(30):
            Number = int(file.readline().strip()) 
            Colour = str(file.readline().strip())
            CardArray[i].Constructor(Number, Colour)
    
    while len(Choice) != 4:
        ChooseNum = int(input("enter Number"))
        mainChoice = ChoseCard(ChooseNum)
        if mainChoice != -1 : 
            Player1[len(Choice) - 1] = mainChoice
        
    for card in Player1:
        print(card)  

if __name__ == '__main__':
    main()