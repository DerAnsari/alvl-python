X="1001 sarmad 25"

Y=len(X)

id=X[:4]

#print(id)
percentage=X[-2:]

name=X[5:-3]

print(id)
print(percentage)
print(name.upper())
print(Y)



#A WAY TO SPLIT THE STRINGS

X="1001 ALI 85"

Y=X.split()

print(Y[0])
print(Y[1])
print(Y[2])



#AN EASIER WAY 

X="1001 ALI 85"

id,name,percentage=X.split()

print(id)
print(name)
print(percentage)