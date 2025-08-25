StackData = [None]*10
StackPointer = 0

def DisplayElements():
    for index in StackData:
        print(index)

def Push(Value):
    global StackPointer
    if StackPointer >= len(StackData) :
        return False
    else:
        StackData[StackPointer] = Value
        StackPointer += 1
        return True
def pop():
    global StackPointer
    if StackPointer == 0:
        print("Stack is empty, cannot remove")
        return -1
    else:
        item = StackData[StackPointer-1]
        StackPointer -= 1
        return item

def main():
    for index in range(len(StackData)+1):
        Value = input("Enter value")
        result = Push(Value)
        if result:
            print("Added value succesfully")
        else:
            print("Cannot Add more, Stack Full")
    print(StackData)

    for i in range(1):
        result = pop()
    for line in range(StackPointer-1):
        print(StackData[StackPointer])

if __name__ == '__main__':
    main()