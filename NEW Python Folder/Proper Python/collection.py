                                    # List

myList = ["apple", "orange", "mango","apple", "pomegranate"]

for index in myList:
    print(index)
myList.append("pineapple")
myList.remove("mango")
myList.insert(0,"carrot")
myList.sort()
myList.reverse()
myList.count("apple")

                                    # Sets

mySet= {"apple", "orange", "mango", "pomegranate"}

mySet.add("carrot")
mySet.remove("apple")
mySet.pop()
mySet.clear()

                                        #Tuples

myTuple = ("apple", "orange", "mango", "pomegranate","apple")

myTuple.count("apple")

                                        #2D List

fruit = ["apple","banana", "coconut", "orange"]
vegetable = ["celery", "cucumber", "spring onion", "Tomatos"]
meat = ["beef", "chicken", "lamb", "pork"]

groceries = [fruit,vegetable,meat]

for basket in groceries:
    for food in basket:
        print(food, end=" ")
    print()

                                        #Dictionaries

capitals = {"USA":"Washington D.C",
            "China":"Beijing",
            "Pakistan":"Islamabad"
            }

capitals.get("USA")
capitals.update({"Germany":"Berlin"})
capitals.pop("China")
capitals.popitem()
capitals.clear()
capitals.keys()
capitals.values()

                                                #List comprehensions

doubles = []
for index in range (1,11):
    doubles.append(index*2)

print(doubles)
#ShortCut
doubles= [x*2 for index in range (1,11)]