Animals = [None]*20
Colour = [None]*10
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimals(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animals[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

def PopAnimals():
    global AnimalTopPointer
    Data = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        Data == Animals[AnimalTopPointer-1]
        AnimalTopPointer -= 1
        return Data

def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

def PopColours():
    global ColourTopPointer
    Data = ""
    if ColourTopPointer == 0:
        return ""
    else:
        Data = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return Data


def ReadData():
    try:
        with open("TextFiles-P4/AnimalData.txt", "r") as file:
            for i,index in enumerate(file):
                DataToPush = index.strip()
                PushAnimals(DataToPush)
    except FileNotFoundError:
        print("file not found")

    try:
        with open("TextFiles-P4/ColourData.txt", "r") as secfile:
            for i,index in enumerate(secfile):
                DataToPush = index.strip()
                PushColour(DataToPush)

    except FileNotFoundError:
        print("file not found")

def OutputItems():
    animal = PopAnimals()
    colour = PopColours()
    print(animal)
    if animal == "":
        print("No Animal")
    elif colour == "":
        print("No Colour")
    print(f"result:{animal},{colour}")

def main():
    ReadData()
    for index in range(3):
        OutputItems()

if __name__ == '__main__':
    main()
