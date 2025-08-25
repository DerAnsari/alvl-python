data = []
def InsertionSort(data):
    for index in range(1, len(data)):
        key = data[index]
        count = index - 1
        while count >= 0 and key < data[count]:
            data[count + 1] = data[count]
            count -= 1
        data[count + 1] = key
    return data
