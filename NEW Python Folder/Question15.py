Queue = [None for _ in range(50)]
HeadPointer = -1
TailPointer = 0

def enQueue(word):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 50:
        print("Queue is Full")
    else:
        Queue[TailPointer] = word
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0

def deQueue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1:
        print("Queue is Empty")
        return None
    answer = Queue[HeadPointer]
    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0
    else:
        HeadPointer += 1
    return answer

def readData():
    with open("TextFiles-P4/QueueData.txt", 'r') as file:
        for index in file:
            word = index.strip()
            enQueue(word)

class RecordData:
    def __init__(self):
        self.ID = ""
        self.Total = 0
    
    def set_ID(self, i):
        self.ID = i
    
    def set_Total(self, t):
        self.Total = t
    
    def get_Id(self):
        return self.ID
    
    def get_Total(self):
        return self.Total

Record = [RecordData() for _ in range(50)]
numberRecords = 0

def TotalData():
    global numberRecords
    DataAccessed = deQueue()
    if DataAccessed is None:
        return
    flag = False
    if numberRecords == 0:
        Record[0].set_ID(DataAccessed)
        Record[0].set_Total(1)
        flag = True
        numberRecords += 1
    else:
        for x in range(numberRecords):
            if Record[x].get_Id() == DataAccessed:
                currentTotal = Record[x].get_Total()
                Record[x].set_Total(currentTotal + 1)
                flag = True
                break
        if not flag and numberRecords < 50:
            Record[numberRecords].set_ID(DataAccessed)
            Record[numberRecords].set_Total(1)
            numberRecords += 1

def outputRecords():
    for i in range(numberRecords):
        outId = Record[i].get_Id()
        outTotal = Record[i].get_Total()
        print(f"ID: {outId} Total: {outTotal}")

def main():
    readData()
    while HeadPointer != -1:
        TotalData()
    outputRecords()

if __name__ == '__main__':
    main()