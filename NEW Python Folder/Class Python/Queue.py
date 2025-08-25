queueFull = 10
queueLen = 0
frontPoint = 0
endPoint = -1
queue = [None] * queueFull

def enQueue(item):
    global queueLen, endPoint,queueFull

    if queueLen < queueFull:    #!what
        if endPoint < len(queue):
            endPoint += 1
        else:
            endPoint = 0
        queueLen += 1
        queue[endPoint] = item
    else:
        print("Queue is Full")

def deQueue():
    global queueLen, frontPoint, item
    if queueLen == 0:
        print("Queue is empty")
        return None
    else:
        item = queue[frontPoint]
        if frontPoint == len(queue) - 1:
            frontPoint = 0
        else:
            frontPoint += 1 
    queueLen -= 1
    return item

print("Please press 1 if you wish to add (enqueue) and 2 if you wish to remove (dequeue), 3 to exit")

while True:
    try:
        Num = int(input("Enter your choice (1 to enqueue, 2 to dequeue, 3 to exit): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if Num == 1:
        item = input("What do you wish to enqueue? ")
        enQueue(item)    #!WHAT
    elif Num == 2:
        removed = deQueue()
        if removed is not None:
            print(f"Removed {removed} from the queue.")
    elif Num == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")