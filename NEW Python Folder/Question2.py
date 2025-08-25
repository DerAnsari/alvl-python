Animals = [""]*5

def SortDescending():
    for i in range(len(Animals)-1):
        for y in range(len(Animals)- i -1 ):
            if Animals[y][:2] < Animals[y+ 1][:2]:
                Animals[y],Animals[y+1] = Animals[y+1],Animals[y]

for index in range(len(Animals)):
    Animal = input("Enter Animal name").lower()
    Animals[index]= Animal

SortDescending()
for x in Animals:
    print(x)