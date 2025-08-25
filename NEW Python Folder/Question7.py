
DataArray = [""]*100

def ReadFile():
    try:
        with open("TextFiles-P4\IntegerData.txt","r") as file:
            for i,index in enumerate(file):
                num = index.strip()
                DataArray[i] = num
    except FileNotFoundError:
        print("File Not found")

def FindValue():
    FindVal = input("Enter your desired value")
    count= 0
    for index in range(len(DataArray)):
        if DataArray[index] == FindVal:
            count += 1
    return count

def BubbleSort():
    for index in range(len(DataArray)-1):
        for i in range(len(DataArray)-1-index):
            if int(DataArray[i]) > int(DataArray[i+1]):
                DataArray[i],DataArray[i+1] = DataArray[i+1],DataArray[i]


def main():
    ReadFile()
    BubbleSort()
    print(DataArray)
    result = FindValue()
    print(f"Your Desired stiring shows up {result} times")

if __name__ == '__main__':
    main()