X= int(input("enter first number\t"))
Y= int(input("enter second number\t"))
print("The sum is \t\t",(X+Y))
print("the difference is \t",(X-Y))
print("the product is\t",(X*Y))
print("the division is\t",(X/Y))
print("the power is\t",(X**Y))
print("the mod is\t",(X%Y))
print("the DIV is\t",(X//Y))
print("is X>Y???\t",(X>Y))
print("is X<Y???\t",(X<Y))
print("is X>=Y???\t",(X>=Y))
print("is X<=Y???\t",(X<=Y))

X= True
Y= True

print(X and Y)
print(X or Y)

X= input("ENTER YOUR FIRST NAME\t")
Y= input("ENTER YOUR LAST NAME\t")
P= int(input("ENTER YOUR PHYSICS TEST RESULT"))
M= int(input("ENTER YOUR MATHS TEST RESULT"))
C= int(input("ENTER YOUR COMPUTER TEST RESULT"))
sum= (P+M+C)
avg=(sum/int(3))
print("the total,avg of",(X+Y),"is",sum,avg)
