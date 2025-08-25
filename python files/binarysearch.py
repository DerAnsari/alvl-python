myNum=[34,75,6,8,56,88,64,78,36,9]

top=0
bottom=9
found=False

searchnum=int(input("enter a number to search"))

while found == False and top<= bottom:

    middle=int((top+bottom)/2)

    if searchnum==myNum[middle]:
        found=True
    elif searchnum>myNum[middle]:
        top=middle+1
    else:
        bottom=middle-1

if found== True:
    print("number found is",middle)
else:
    print("number not found")
        