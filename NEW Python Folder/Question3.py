#DECLARE The Data : ARRAY [1 TO 9] OF INTEGER
TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]


def InsertionSort(TheData):
    for Count in range(0, len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while(NextValue >= 0 and Inserted != 1):
            if(DataToInsert < TheData[NextValue]):
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue+1] = DataToInsert
            else:
                Inserted = 1

def PrintArray(TheData):
    for index in range(len(TheData)):
        print(TheData[index])

def SearchNum(num):
    for i in range(len(TheData)):
        if TheData[i] == num:
            print("Found")
            return(True)
    print("Not Found")
    return(False)

print("Before Sorting")
PrintArray(TheData)
print("After Sorting")
InsertionSort(TheData)
PrintArray(TheData)
num = 9
SearchNum(num)