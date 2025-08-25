                                                        #MAKING THE FUNCTION 

def getGrade(Percentage):
    if Percentage>= 90 and Percentage <=100:
        grade="A*"
    elif Percentage >= 80 and Percentage<= 90:
        grade="A"
    elif Percentage >= 70 and Percentage<= 80:
        grade="B"        
    elif Percentage >= 60 and Percentage<= 70:
        grade="C "        
    else:
        grade="D" 

    return grade


X= getGrade(75)

print(X)


                                                        #second function


def checkEqual(n1,n2):

    if n1==n2:
        return True
    else:
        return False
    

Y=checkEqual(1,1)

print (X)

                                                    #THIRD FUNCTION

def greaterNum(num1,num2):

    if num1> num2:
       return num1
    else:
        return num2
    

Z=greaterNum(1,5)

print(Z)




def greaterNum(num1,num2,num3):

    if num1> num2 and num3:
       return num1
    elif num3> num1 and num2:
        return num3
    else:
        return num2
    

Z=greaterNum(1,5,8)

print(Z)