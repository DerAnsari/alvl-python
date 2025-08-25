class HiddenBoxes:
    def __init__(self,newboxname,newcreator,newdate,newlocation):
        self.boxName = newboxname
        self.creator = newcreator
        self.dateHidden = newdate
        self.gameLocation = newlocation
        self.lastFinds = [["" for _ in range(2)] for _ in range(10)]
        self.active = False

    def getBoxesName(self):
        return self.boxName
    
    def getGameLocation(self):
        return self.gameLocation
    
def NewBox():
    global TheBoxes
    newboxname = input("enter box name")
    newcreator = input("enter creator name")
    newdate = input("enter date")
    newlocation = input("enter location")
    TheBoxes.append(HiddenBoxes(newboxname,newcreator,newdate,newlocation))
    return len(TheBoxes)
    
TheBoxes = [HiddenBoxes("","","","") for _ in range(10000)]
total = NewBox()