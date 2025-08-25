#DECLARE QueueData : ARRAY [1:20] OF INTEGER
#DECLARE StartPointer,EndPointer : INTEGER
QueueData = [None]*20
StartPointer = 0
EndPointer = 0
count = 0
     
def Enqueue(data):
    global QueueData, StartPointer, EndPointer, count
    if count == 20:
        return -1
    else:
        QueueData[EndPointer] = data
        count += 1
        if EndPointer == 19:
            EndPointer = 0
        else:
            EndPointer +=1
    return 1

def remove():
    global count, QueueData, StartPointer
    if count < 2:
        return "No Items"
    else:
        String = ""
        for _ in range(2):
            String += str(QueueData[StartPointer]) + " "
            count -= 1 
            if StartPointer == 19:
                StartPointer = 0
            else:
                StartPointer+=1
        return String.strip()

def readfile():
    fileAddress = str(input("Enter the file name"))
    try:
        with open (f"TextFiles-P4./{fileAddress}","r") as file:
            for line in file:
                value = line.readfile().strip()
                results = Enqueue(value)
                if results == -1:
                    return 1
            return 2
    except FileNotFoundError:
        return -1

ans = readfile()
if ans == -1:
    print("No such text file found")
elif ans == 1:
    print("The queue was full")
else:
    print("Successfully Updated the queue")