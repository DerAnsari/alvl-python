                                        #MAKING A FILE AND ENTERING

# myfile=open("ClassAtt.txt", "a")

# for index in range (0,20):

#     id=input("Enter Student ID\t")
#     date=input("Enter date")
#     oneline= id+date+ "\n" 

#     myfile.write(oneline)

# myfile.close

                                    #SEARCHING THE FILE

myfile=open("ClassAtt.txt", "r")

count=0

searchid=input("enter student id\t")

oneline= myfile.readline()

while oneline != "":
    id=oneline[:4]
    date=oneline[4:]

    if id==searchid:
        print("Date\t",date)
        count=count+1

    oneline=myfile.readline()

myfile.close()

print("The Student id",searchid,"was present for",count,"days.")