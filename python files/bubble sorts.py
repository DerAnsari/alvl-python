# temp=0
# X=5
# Y=7
# if X<Y:
#     temp=Y
#     Y=X
#     X=temp
# print(X,Y)

mystudent=["ali","umer","jim","jojo","dio"]
for X in range(0,4):
    for Y in range(X+1,5):

        if mystudent[X]>mystudent[Y]:
            temp=mystudent[X]
            mystudent[X]=mystudent[Y]
            mystudent[Y]=temp

print(mystudent)

