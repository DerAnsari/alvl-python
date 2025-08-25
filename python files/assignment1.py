# myfile=open(r"C:\Users\Dell\Desktop\PythonCourse.txt","r")

# found=False

# searchID= input("Enter Student ID")

# oneline = "abc"

# while oneline!= "" and found== False:
#     oneline=myfile.readline()

#     id= oneline[:4]
#     name= oneline[5:-3]
#     percentage= oneline[-3:]

#     if searchID== id:
#         found=True

# if found == True:

#     print("Student ID:",id)
#     print("Student Name:",name)
#     print("Student percentage",percentage)
# else:
#     print("record not found not found...")

# myfile.close






myfile=open(r"C:\Users\Dell\Desktop\PythonCourse.txt","r")

count=0

oneline= myfile.readline()
sum =0
while oneline!="":
    
    sum=sum+ (int(oneline[-2:]))
    count=count+1

    oneline=myfile.readline()

myfile.close

avg=sum/count
print("Class Average",avg)
