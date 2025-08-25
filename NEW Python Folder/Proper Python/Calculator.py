Operator = input("Enter a Operator (+,-,*,/) ")
Num1 = float(input("Enter First number"))
Num2 = float(input("Enter Second number"))

if Operator == "+" :
    print(Num1 + Num2)
elif Operator == "-" :
    print(Num1 - Num2)
elif Operator == "*":
    print(Num1 * Num2)
elif Operator == "/":
    print(Num1 / Num2)
else:
    print("Incorrect Operator")


