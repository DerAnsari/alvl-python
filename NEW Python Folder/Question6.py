#DECLARE DataArray : ARRAY [1:25] OF INTEGER
DataArray = [None]*25

def printArray(DataArray):
    for line in DataArray:
        print(line," ",end='')

def LinearSearch(SearchArray, SearchVal):
    global DataArray
    count = 0
    found = False
    for num in SearchArray:
        if num == SearchVal:
            count+= 1 
            found = True
    if found == True:
        print("Value found")
        return count
    return -1

try:
    with open ("TextFiles-P4/Data.txt") as file:
        for index in range(25):
            value = int(file.readline().strip())
            DataArray[index] = value
except FileNotFoundError:
    print("File Not Found")

printArray(DataArray)
print("")
SearchValue = int(input("Enter the Value to search"))
while SearchValue < 0 or SearchValue > 100:
    SearchValue = int(input("Enter the Value to search (between 0 and 100 inclusively)"))
result = LinearSearch(DataArray, SearchValue)
if result == -1:
    print("Result Not found")
else:
    print(f"The number {SearchValue} is found {result} times.")