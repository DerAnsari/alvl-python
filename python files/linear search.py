names=["minhas", "ali", "saemas", "jim"," muhammmad"]
found=False
index=0

X=input("enter a name in search")

while found == False and index<5:
    if X==names[index]:
        found=True
    else:
        index=index+1

if found ==True:
    print("name found at",index)
else:
    print("name not found")
    

