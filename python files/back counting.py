#long way (works in most programming languages)

count=10
for index in range(1,11):                               
    print(count)
    count=count-1

#  easy way (works in python)

for index in range (10,0):                               
    print(index)

#to print in same line 

for index in range (10,0,-1):
    print(index,end=" ")    

#double loop and table format

for index in range(1,6):
    for secindex in range(1,6):
        print(index,secindex,end=" ")
    print()    