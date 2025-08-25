                              #While Loops
count = 1
while count != 11:
    print(f"while loop number {count}")
    count += 1

                              #For Loops

for index in range (1,11):
    print(f"for loop number {index}")


                                    #Case of

day = input("Enter Day")
def weekcheck(day):
    match day:
        case 1 :
            print("monday")
        case 2 :
            print("tuesday")
        case _ :
            print("No days found")
