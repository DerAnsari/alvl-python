mylist = [1,4,6,8,9,12,667,999]

def binarySearch (Num):
    global mylist
    top= 0
    bottom= 7
    while top <= bottom:
        middle = int((top+bottom)/2)
        if mylist[middle] == Num:
            return (middle)
        elif Num> mylist[middle]:
            top= middle+1
        else:
            bottom=middle -1
    return -1
found= False
while found != True:
    
    searchNum = int(input("Enter desired number"))
    foundStatus= binarySearch(searchNum)
    if foundStatus == -1:
        print("Couldnt find the number")
    else:
        print("Number found as:",foundStatus)
        found = True
