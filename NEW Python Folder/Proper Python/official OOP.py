from opcode import name_op


class car:

    class_wheels = 4                                        #Class Variable

    def __init__(self,model,year,color,for_sale):

        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = car("Mustang",2024,"red",True)
print(f"the number of wheels in {car1.model} is {car.class_wheels}")

                        #Polymorphism

class Shapes:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

class Circle(Shapes):
    def __init__(self,radius,color,filled):
        super().__init__(color,filled)
        self.radius = radius

class Square(Shapes):
    def __init__(self,width,color,filled):
        super().__init__(color,filled)
        self.width= width
class Triange(Shapes):
    def __init__(self,radius,height,color,filled):
        super().__init__(color,filled)
        self.radius = radius
        self.heigth = height

                    #Duck Typing

class Animal:
    pass

class cat(Animal):
    def speak(self):
        print("Meow")

class dog(Animal):
    def speak(self):
        print("woof")

class bike:
    def speak(self)
        print("beep")

Animals = [cat(),dog(),bike()]
for ani in Animals:
    ani.speak()

            #Static methods

class Employee:

    def __init__(self,name, position):
        self.name = name
        self.position = position

    def getInfo(self):
        return (f"{self.name} = {self.position})

    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager", "cashier","cook"]
        return posion in valid_position

Employee.is_valid_position("jesse")

            #Class methods

class Student:
    count = 0
    total_gpa = 0

    def __init__(self):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

        #Instance Method

        def get_info(self):
            return (f"{self.name}  {self.gpa}")

        @classmethod
        def get_average_gpa(cls):
            if cls.count == 0:
                return 0
            else:
                return f"Average gpa: {cls.total/cls.count:.2f}"

            #Majic methods

class Book:
    def __init__(self,title,author,num_pages):
       self.title = title
       self.author = author
       self.num_pages = num_pages

    def __str__(self):
        return(f"{self.title} by {self.author}")

    def __eq__(self, other):
        return (self.title == other.title and self.author == other.author)

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return (f"{self.num_pages + other.num_pages} pages")

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        pass

            #Property decorator

class Square:
    def __init__(self,length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.deleter
    def length(self):
        del self._length

    @length.setter
    def length(self,L):
        self._length = L

