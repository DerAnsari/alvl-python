list = [2,3,5,6,3]

def recursivelyAdd(value):
    global list
    if value == 0:
        return 0 
    else:
        return list[value - 1] + recursivelyAdd(value - 1)

value = int(input("enter til how long you wanna go for "))
answer = recursivelyAdd(value)
print(answer)