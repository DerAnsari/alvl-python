class node:
    def __init__(self,thisData,thisNode):
        self.Data = thisData
        self.NextNode = thisNode

def outputNode(Array,startPointer):
    while startPointer != -1:
        print(str(Array[startPointer].Data))
        startPointer = Array[startPointer].NextNode

def addNode(linkedList, currentPointer, emptyList):
    dataToAdd = input("Enter the data to add: ")
    if emptyList < 0 or emptyList > 9:
        return False, emptyList

    nextFree = linkedList[emptyList].NextNode  # Save the next free spot
    newNode = node(int(dataToAdd), -1)
    linkedList[emptyList] = newNode

    previousPointer = 0
    while currentPointer != -1:
        previousPointer = currentPointer
        currentPointer = linkedList[currentPointer].NextNode

    linkedList[previousPointer].NextNode = emptyList
    emptyList = nextFree  # Update freelist

    return True, emptyList


linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(58,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5
print("before")
outputNode(linkedList,startPointer)
print("after")
result = addNode(linkedList,startPointer,emptyList)
if result == False:
    print("error already full")
else:
    print("successfully added")
outputNode(linkedList,startPointer)