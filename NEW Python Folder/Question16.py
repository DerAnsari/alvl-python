#DECLARE Queue : ARRAY [1:100] OF INTEGER
#DECLARE headPointer, tailPointer : INTEGER
Queue = [None]*100
headPointer = 0 
tailPointer = 0 
count = 0

def enqueue(value):
    global count, tailPointer, Queue
    if count == 100:
        return False
    else:
        Queue[tailPointer] = value
        count += 1 
        if tailPointer == 99:
            tailPointer = 0
        else:
            tailPointer += 1 
    return True

def IterativeOutput(Start):
    global Queue, headPointer
    if Start <= headPointer:
        return 0
    else:
        return Queue[Start - 1] + IterativeOutput(Start - 1)


def dequeue():
    pass

for index in range(1,21):
    successrate =enqueue(index)
    if successrate == False:
        print("couldn't already full")
    else:
        print("Success")
answer = IterativeOutput(count)
print(answer)