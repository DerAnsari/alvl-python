StackVowels = [None]*100
StackConsonants = [None]*100
VovelTop = 0
ConsonantsTop = 0
Vowels = ["a","e","i","o",'u']

def VowelPush(Char):
    global VovelTop
    if VovelTop < len(StackVowels)-1:
        VovelTop += 1
        StackVowels[VovelTop] = Char
    else:
        print("Stack is full")


def ConsonantPush(Char):
    global ConsonantsTop
    if ConsonantsTop < len(StackVowels)-1:
        ConsonantsTop += 1
        StackConsonants[ConsonantsTop] = Char
    else:
        print("Stack is full")

def PushData(Char):
    if Char in Vowels:
        VowelPush(Char)
    else:
        ConsonantPush(Char)

def PopVowels():
    global VovelTop
    if VovelTop == 0:
        print("No Data")
        return None
    else:
        item = StackVowels[VovelTop]
        VovelTop -= 1
        return item

def PopConsonants():
    global ConsonantsTop
    if ConsonantsTop == 0:
        print("No Data")
        return None
    else:
        item = StackConsonants[ConsonantsTop]
        ConsonantsTop -= 1
        return item

def ReadData():
    try:
        with open("TextFiles-P4\StackData.txt", "r") as file:
            for line in file:
                Char = line.strip()
                PushData(Char)
    except FileNotFoundError:
        print("Error File wasnt Found")

def main():
    finalRez =""
    ReadData()
    for index in range(5):
        user = input("Enter your Choice").lower()
        result = None
        if user == "vowel":
            result= PopVowels()
        elif user== "consonants":
            result = PopConsonants()
        if result is not None:
            finalRez += result
    print(finalRez)

if __name__ == '__main__':
    main()