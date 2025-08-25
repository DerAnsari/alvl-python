file1= open(r"C:\Users\Dell\Desktop\PythonCourse.txt","r")
file2= open("MyNewFile.txt","w")

searchID= input("Enter Student ID")

mystring= file1.readline()

while mystring!="":

    if searchID != mystring[:4]:
        file2.write(mystring)

    mystring = file1.readline()

file2.close
file1.close