def showBalance(Balance):
    print(f"Your Balance is {Balance:2f}")

def deposit():
    addnum = float(input("Enter Ammount to be deposited"))
    if addnum <= 0:
        print("invalid try again")
        return 0
    else:
        return addnum

def withdraw(Balance):
    takeout= float(input("Enter Withdrawal ammount"))
    if takeout <= 0 or takeout>Balance:
        print("invalid try again")
        return 0
    else:
        return takeout

def main():
     Balance = 0
     running = True

     while running:
         print("Banking App")
         print("Chose the following options")
         print("1. Show Balance")
         print("2. Deposite ammount")
         print("3. Withdraw Ammount")
         print("4. Exit programe")
         action = str(input("Enter your desired function"))
         match action:
            case 1 :
                showBalance(Balance)
            case 2:
                Balance += deposit()
            case 3:
                Balance-= withdraw(Balance)
            case 4:
                running= False
            case _:
                print("invalid command try again")
     print("thank you have a nice day")

if __name__ == '__main__':
    main()