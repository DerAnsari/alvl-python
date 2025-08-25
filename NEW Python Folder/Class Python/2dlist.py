# mylist = [
#     [None],
#     [None],
#     [None]
#     ]

# myListimproves = [
#     [0,0] for _ in range(5)
# ]

# myListimproves[0] = [2000,304]


# myList = [[0 for col in range(5)] for row in range(5)]
# print(myList)

#!Question begins 


myList = [[0,0] for index in range(5)]

myList[0] = [1001,56]
myList[1] = [1002,57]
myList[2] = [1003,58]
myList[3] = [1004,59]
myList[4] = [1005,60]

print(myList)


def LinearSearch(Array,ID):
 for row in range(len(Array)):
  if myList[row][0] == ID:
    return myList[row][1]
 return -1


x = LinearSearch(myList,1009)
print(x)