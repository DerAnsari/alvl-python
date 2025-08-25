count=0
x= "Minhas Rupsi"
found=False
letter=input("enter desicerd character")
for index in x:
    if index== letter:
        found=True
        count=count+1        
print(count)        

# if found==True:

print("character:",letter,"is found",count,"times")
    
# else:
#     print("character is not found")    