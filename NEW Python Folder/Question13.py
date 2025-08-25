#DECLARE QueueArray : ARRAY [1:10] OF STRING
#DECLARE headPointer, tailPointer, numberOfItems : INTEGER

QueueArray = [None]*10
headPointer = 0
tailPointer = 0
numberOfItems = 0

def enqueue(AddData):
    global QueueArray,headPointer,tailPointer,numberOfItems
    if numberOfItems == 10:
        return False
    QueueArray[tailPointer] = AddData
    if tailPointer >= 9:
        tailPointer = 0 
    else:
        tailPointer += 1
    numberOfItems += 1 
    return True

def dequeue():
    global QueueArray, numberOfItems, headPointer
    if numberOfItems == 0:
        return False
    else:
        numberOfItems -= 1
        if headPointer == 9:
            headPointer = 0
        else:
            headPointer += 1 
    return QueueArray[headPointer]

for i in range(11):
    value = str(input("Enter value to add"))
    result = enqueue(value)
    if result == True:
        print("Successfully Added")
    else:
        print("Cannot Add, full")
for _ in range(2):
    callback = dequeue()
    print(callback)