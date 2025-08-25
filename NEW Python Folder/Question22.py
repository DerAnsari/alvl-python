class Pictures:
    #PRIVATE Description : STRING
    #PRIVATE Width : INTEGER
    #PRIVATE Height : INTEGER
    #PRIVATE FrameColor : STRING
    def __init__(self,d,w,h,fc):
        self.__Description = d
        self.__Width = w
        self.__Height = h
        self.__FrameColor = fc
    def getDescription(self):
        return self.__Description
    def getWidth(self):
        return self.__Width
    def getHeight(self):
        return self.__Height
    def getFrameColor(self):
        return self.__FrameColor
    def setDescription(self,D):
        self.__Description = D

def readData():
    try:
        with open("TextFiles-P4/Pictures.txt","r") as file:
            count = 0
            Desc = str(file.readline().strip().lower())
            while Desc:
                width = int(file.readline().strip())
                height = int(file.readline().strip())
                framecol = str(file.readline().strip())
                PictureNode = Pictures(Desc,width,height,framecol)
                PictureArray.append(PictureNode)
                Desc = str(file.readline().strip().lower())
                count += 1 
    except FileNotFoundError:
        print("file not found")


PictureArray = []
readData()
usrFramcol = str(input("enter the color of your frame")).lower()
usrWidth = int(input("enter the maximum width you'd like"))
usrHeight =  int(input("enter the maximum height you'd like"))
print("frames that match your requirements:")
found = False

for Picture in PictureArray:
    if Picture.getFrameColor() == usrFramcol:
        if Picture.getWidth() <= usrWidth:
            if Picture.getHeight() <= usrHeight:
                print(Picture.getDescription()," ",str(Picture.getWidth())," ",str(Picture.getHeight()))
                found = True

if not found:
    print("No frames match your requirements :(")