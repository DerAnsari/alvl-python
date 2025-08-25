class Card:
    #PRIVATE Number : INTEGER
    #PRIVATE Colour : STRING
    def __init__(self,N,C):
        self.__Number = N 
        self.__Colour = C
    
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour

class Hand:
    def __init__(self,Card1,Card2,Card3,Card4,Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5 
    
    def GetCard(self,num):
        return self.__Cards[num]

def CalculateValue(playerHand):
    score = 0 
    for count in range(4):
        cardRecieved = playerHand.GetCard(count)
        cardData = cardRecieved.GetColour()
        match cardData:
            case "red" :
                score = score + 5
            case "blue":
                score = score + 10
            case "yellow":
                score = score + 15
    return score

OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

player1 = Hand(OneRed,TwoRed,ThreeRed,FourRed,OneYellow)
player2 = Hand(TwoYellow,ThreeYellow,FourYellow,FiveYellow,OneBlue)
player1Score = CalculateValue(player1)
player2Score = CalculateValue(player2)
if player1Score > player2Score : 
    print("player1 wins")
elif player2Score > player1Score : 
    print("player 2 wins")
else: 
    print("its a tie")