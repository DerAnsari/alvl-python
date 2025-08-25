class SaleData:
    def __init__(self,id,quantity):
        self.id = id
        self.quantity = quantity

CircularQueue = [SaleData("",1)for index in range(5)]
Head = 0
Tail = 0 
NumberOfItems = 0

def Enqueue(NewRecord):
    global Head, Tail, NumberOfItems, CircularQueue
    if NumberOfItems == 5 :
        return -1
    else:
        CircularQueue[Tail] = NewRecord
        NumberOfItems -=1
        if Tail == 4:
            Tail = 0 
        else:
            Tail += 1
        return -1
    
def Dequeue():
    global Head, Tail, NumberOfItems, CircularQueue
    FirstRecord = SaleData("", -1)
    if NumberOfItems == 0 :
        return FirstRecord
    else:
        FirstRecord = CircularQueue[Head]
        NumberOfItems -= 1
        if Head == 0:
            Head = 4
        else:
            Head -= 1

        return FirstRecord
    
def EnterRecord():
    Id = input("Enter your ID ")
    Quantity = input("Enter your Quantity Desired")
    Record = SaleData(id,Quantity)

    x = Enqueue(Record)

    if x == -1:
        print("Full")
    else:
        print("Stored") 

for i in range(6):
    EnterRecord()

deletus = Dequeue()

if deletus.id == "" :
    print("EMPTY")
else:
    print(deletus.id, deletus.quantity)

EnterRecord()
for index in range(5):
    print(CircularQueue[index].id, CircularQueue[index].quantity)
