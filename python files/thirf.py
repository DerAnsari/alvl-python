X= int(input("enter percentage:"))
if X >= 65 :
    print("YES YOU PASS")
else:
    print("OH NO YOU FAILED")    
 

X= int(input("ENTER THE PERCENTAGE"))

if X >= 90 and X<= 100:
    grade="A*"
elif X >= 80 and X<= 90:
    grade="A"
elif X >= 70 and X<= 80:
    grade="B"        
elif X >= 60 and X<= 70:
    grade="C "        
elif X >= 50 and X<= 60:
    grade="D"        
elif X >= 0 and X<= 50:
    grade="CONGRAGULATION YOU'RE A FAILURE" 
else:
    grade= "invalid percentage"
print("your Grade is:",(grade))               
        
        
X= int(input("enter first number"      ))
Y= int(input("enter your second number"))
if X==Y :
    print("the numbers are same")
else :
    print("the numbers are not same")


X= input("enter your first name" )
Y= input("enter your second name")
C= int(input("enter your comp marks"   ))
P= int(input("enter your physics marks"))
M= int(input("enter your maths marks"  ))
sum=(C+P+M)
avg= sum/3
if avg >= 90 and avg<= 100:
    grade="A*"
elif avg >= 80 and avg<= 90:
    grade="A"
elif avg >= 70 and avg<= 80:
    grade="B"        
elif avg >= 60 and avg<= 70:
    grade="C "        
elif avg >= 50 and avg<= 60:
    grade="D"        
elif avg >= 0 and avg<= 50:
    grade="CONGRAGULATION YOU'RE A FAILURE" 
else:
    grade= "invalid percentage"
print("the grade of",X , Y ,"is",grade,"the sum is",sum)

for index in range (10):
    print("DIO")