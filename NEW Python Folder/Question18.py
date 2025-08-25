#DECLARE ArrayNodes : ARRAY [1:3][1:20] OF INTEGER
#DECLARE RootPointer, FreePointer : INTEGER

ArrayNodes = [[0]*3 for _ in range(20)]
rootPointer = -1
freePointer = 0

def addNodes():
    global ArrayNodes,rootPointer,freePointer
    val = int(input("Enter the data"))
    if freePointer <= 19:
        ArrayNodes[freePointer][0] = -1
        ArrayNodes[freePointer][1] = val
        ArrayNodes[freePointer][2] = -1
        if rootPointer == -1:
            rootPointer = 0
        else:
            placed = False
            currentNode = rootPointer
            while placed == False:
                if val < ArrayNodes[currentNode][1]:
                    if ArrayNodes[currentNode][0] == -1:
                        ArrayNodes[currentNode][0] = freePointer
                        placed = True
                    else:
                        currentNode = ArrayNodes[currentNode][0]
                else:
                    if ArrayNodes[currentNode][2] == -1:
                        ArrayNodes[currentNode][2] = freePointer
                        placed = True
                    else:
                        currentNode = ArrayNodes[currentNode][2]
        freePointer += 1 
    else:
        print("Tree is full")

def printAll():
    for i in range(20):
        print(f"{ArrayNodes[i][0]} {ArrayNodes[i][1]} {ArrayNodes[i][2]}")        

def inOrder(ArrayNodes, rootPointer):
    if rootPointer == -1:
        return
    if ArrayNodes[rootPointer][0] != -1: 
        inOrder(ArrayNodes, ArrayNodes[rootPointer][0])
    print(str(ArrayNodes[rootPointer][1]))
    if ArrayNodes[rootPointer][2] != -1:
        inOrder(ArrayNodes, ArrayNodes[rootPointer][2])


for _ in range(10):
    addNodes()
printAll()
inOrder(ArrayNodes,rootPointer)