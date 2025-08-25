#DECLARE ArrayData : ARRAY [0 TO 10][0 TO 10] OF INTEGER
import random as rn
ArrayData = [[0]*10 for _ in range(10)]
for x in range(10):
    for y in range(10):
        ArrayData[y][x] = rn.randint(1,100)

def printArray(ArrayData):
    for row in range(10):
        for col in range(10):
            print(ArrayData[row][col],"",end='')
        print("")

def BinarySearch(SearchArray, Lower, Upper, SearchVal):
    if Upper >= Lower:
        Mid = int((Lower + (Upper-1))/2)
        if SearchArray[0][Mid] == SearchVal:
            return Mid
        elif SearchArray[0][Mid] > SearchVal:
            return(BinarySearch(SearchArray, Lower, Mid -1, SearchVal))
        else:
            return(BinarySearch(SearchArray, Mid +1, Upper, SearchVal))
    return -1    

print("Before sorting")
printArray(ArrayData)
print("After Sorting")
ArrayLength = 10
for x in range(ArrayLength-1):
    for y in range(ArrayLength-2):
        for z in range(ArrayLength - y - 2):
            if ArrayData[x][z] > ArrayData[x] [z + 1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = TempValue
printArray(ArrayData)
for _ in range(2):
    SearchVal = int(input("EnterValue to find"))
    answer = BinarySearch(ArrayData,0,9,SearchVal)
    print(answer)