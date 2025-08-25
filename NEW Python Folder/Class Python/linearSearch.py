def linear_search(mylist, target):
    for i in range(len(mylist)):
        if mylist[i] == target:
            return i  
    return -1  

mylist = [10, 23, 45, 70, 11, 15]

target = input("entered desired num")
result = linear_search(mylist, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
