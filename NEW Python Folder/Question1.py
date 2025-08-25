#DECLARE arrayData: ARRAY (0:10) OF INTEGER
arrayData= [10,5,6,7,1,12,15,21,8]

def linearSearch(searchNum):
    for index in range(9):
        if arrayData[index]== searchNum:
            return index
    return -1

searchNum= input("enter desired number")
found = linearSearch(searchNum)
if found != -1:
    print("Number found at {found}")
else:
    print("Number coundn't be found")