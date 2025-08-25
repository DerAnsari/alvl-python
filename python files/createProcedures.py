                                                                    #THIRD PROCEDURE

# def getOutput():

#     print("Minhas Rupsi")

# getOutput()
                                                                    #SECOND PROCEDURE

#MENU BASED PROCEDURE

def addrecords():

    file1= open(r"C:\Users\Dell\Desktop\PythonCourse.txt","a")

    id= input("Enter Student ID")
    name=input("Enter Student Name")
    percentage=input("Enter Student Percentage")

    mystring= id+" "+name+" "+percentage+"\n"

    file1.write(mystring)

    file1.close()

def displayRecords():
    file1=open(r"C:\Users\Dell\Desktop\PythonCourse.txt","r")

    mystring= file1.readline()

    while mystring != "":
        
        print(mystring)

        mystring=file1.readline()

    file1.close()

def searchRecords():
    file1=open(r"C:\Users\Dell\Desktop\PythonCourse.txt","r")
    found=False
    searchID= input("Enter Student ID\t")

    mystring = file1.readline()

    while mystring != "" and found== False:

        if searchID== mystring[0:4]:
            found=True
        else:
            mystring=file1.readline()

    if found==True:
        print(mystring)
    else:
        print("records not found...")
    
    file1.close

def backupfile():
    file1= open(r"C:\Users\Dell\Desktop\PythonCourse.txt","r")
    file2= open("NewPythonCourse.txt","w")

    searchline=file1.readline()

    while searchline != "":
        file2.write(searchline)
        
        searchline=file1.readline()

    file1.close()
    file2.close ()   
def menu():
     choice=0

     while choice !=5:
         print("1- Add Records")
         print("2- Display records")
         print("3- search records")
         print("4= Backup File")
         print("5- Exit")
         print()
         choice=int(input("enter your choice:"))

         if choice==1:
             addrecords()
         elif choice==3:
             searchRecords()
         elif choice==2:
              displayRecords()
         elif choice ==4:
              backupfile()

print(menu())
