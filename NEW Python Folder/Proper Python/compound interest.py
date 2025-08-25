flag = False
while not flag:
    initial = float(input("Enter your principal amount"))
    rate = float(input("Enter your interest rate"))
    time = int(input("Enter the duration"))
    if initial <0 :
        print("invalid principal")
    elif rate > 100 or rate <0:
        print("invalid interest rate try again")
    else:
        flag = True
        final = initial * pow((1+ rate/100),time)
        print(f"answe is : ${final:.2f}")



