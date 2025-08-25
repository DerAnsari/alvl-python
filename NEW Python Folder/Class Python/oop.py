class rectangle():
    def __init__(self):
        self.__length=0
        self.__width=0
    def set__length(self,l):
        self.__length=l
    def set__width(self,w):
        self.__width = w

    def get__Area(self):
        return (
            self.get_length() * self.get_width() 
        ) 
    
    def get__Parameter(self):
        return (
            2 * (self.get_length() + self.get_width())
        )
    
    def get__length(self):
        return self.__length
    def get__width(self):
        return self.__length
    
red=rectangle()
red.set__length(8)
print(red.get__length())