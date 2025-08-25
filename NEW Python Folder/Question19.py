myList = [[-1,-1,-1] for _ in range(20)]
freeNode = 6
rootPointer = 0

myList[0] = [1,20,5]
myList[1] = [2,15,-1]
myList[2] = [-1,3,3]
myList[3] = [-1,9,4]
myList[4] = [-1,10,-1]
myList[5] = [-1,58,-1]

def searchValue(root, Valuetofind):
    if root == -1 :
        return -1
    else:
        if myList[root,1] == Valuetofind :
            return (
                myList[root]
            )
        else:
            if myList[root,1] == -1 : 
                return -1
    if myList[root,1] > Valuetofind : 
        return searchValue(myList[root,0], Valuetofind)
    if myList[root,1] < Valuetofind :
        return searchValue(myList[root,2], Valuetofind)

