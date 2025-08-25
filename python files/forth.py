# for index in range(1,11):
    # if index % 2 == 0:
    
    #    print(index)
# total=0
# for index in range(1,6):
#     x=int(input("enter percentage \t"))
#     total=total + x
# avg=total/5
# print("average percentage is: ", avg)    



# C=0
# B=0
# A=0
# for index in range(1,11):
#     x=int(input("enter percentage "))
#     if x  >= 80:
#         A=A+1
#     if x >= 60 and x <= 80:
#         B=B+1
#     if x <= 60:
#         C=C+1
# print(A,B,C)


low=101
high=0
for index in range (1,4):
    y= int(input("enter percentage   "))
    if y> high:
        high=y
    if y< low:
        low=y    
print(low,high)        

