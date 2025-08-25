                                                    #FOR PYTHON


# MyStudent=[]
# for index in range(0,5):
#     MyStudent.append(input("enter student name"))
   
# print(MyStudent)




                                                    #FOR PSEUDOCODE


myStudent = ["","","","",""]

for index in range (0,4):
    
    myStudent[index] =input("enter student name")

print(myStudent)




                                                    #TO TAKE OUT ONE VALUE FROM THE LIST

Student=["ali","muhammad","ayaan","amir"]

Student.pop(1)

print(Student)




                                                    #INPUTING DATA AND THEN STORING IT IN A FILE

myfile=open("PythonCourse.txt","w")
for index in range(0,10):
    
    id= input("enter student 1D \t")
    Name=input("enter student name \t")
    percentage=input("enterpercentage \t")

    myline=id+" "+Name+" "+percentage+"\n"

    myfile.write(myline)

myfile.close()



                                                    #TO OPEN A FILE ON RUN THE CONTENTS THROUGH

myfile=open("PythonCourse.txt","r")
count=0
oneline=myfile.readline()

while oneline !="":
    X=oneline.split()
    count=count+1
    print(X[1])

    # print(oneline.strip())

    oneline=myfile.readline()

print("total number of records is",count)


 
myfile=open("PythonCourse.txt","r")
count=0
oneline=myfile.readline()

while oneline !="":
    id,name,percentage=oneline.split()
    count=count+1
    print(id,name,percentage)

    oneline=myfile.readline()

print("total number of records is",count)