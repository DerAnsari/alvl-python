fileread= open(r"C:\Users\Dell\Desktop\PythonCourse.txt","r")

filewrite= open("MyNewFile.txt","w")

myString= fileread.readline()

while myString!="":
    filewrite.write(myString)

    myString= fileread.readline()

fileread.close
filewrite.close
