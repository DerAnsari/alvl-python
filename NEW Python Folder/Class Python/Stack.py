stackFull = 10
stack = [None] * stackFull
topPointer = -1

def pop():
    global topPointer
    if topPointer == -1:  # stack is empty    
        print("Stack is empty, cannot remove")
        return None
    else:
        item = stack[topPointer]
        topPointer -= 1
        return item

def push(item):
    global topPointer
    if topPointer < stackFull - 1:
        topPointer += 1
        stack[topPointer] = item  
        print("added the number to the stack ")  
    else:
        print("Stack is full, cannot add the data")


print("Please press 1 if you wish to add and 2 if you wish to remove")

while True:
    try:
        Num = int(input("Enter your choice (1 to add, 2 to remove, 3 to exit): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if Num == 1:
        item = input("What do you wish to add? ")
        push(item)
    elif Num == 2:
        removed = pop()
        if removed is not None:
            print(f"Removed {removed} from the stack.")
    elif Num == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")