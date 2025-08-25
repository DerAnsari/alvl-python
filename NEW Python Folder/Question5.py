#DECLARE Jobs : ARRAY [0:99 , 0:1] OF INTEGER
#DECLARE NumberOfJobs : INTEGER

Jobs = []
NumberOfJobs = None

def Initialize():
    global Jobs, NumberOfJobs
    for _ in range(100):
        Jobs.append([-1,-1])
        NumberOfJobs = 0

def AddJobs(JobNum,Priority):
    global Jobs, NumberOfJobs
    if NumberOfJobs == 100:
        print("Not Added, Full")
    else:
        Jobs[NumberOfJobs] = [JobNum, Priority]
        print("Added")
        NumberOfJobs += 1

def InsertionSort():
    global Jobs , NumberOfJobs
    for index in range(1,NumberOfJobs):
        key = Jobs[index]
        place = index - 1 
        while place >= 0 and key[1] < Jobs[place][1]:
            Jobs[place+1] = Jobs[place]
            place -=1
        Jobs[place + 1] = key

def printArray():
    for i in range(NumberOfJobs):
        print(f"{Jobs[i][0]} Priority {Jobs[i][1]}")


Initialize()
AddJobs(12,10)
AddJobs(526,9)
AddJobs(33,8)
AddJobs(12,9)
AddJobs(78,1)
InsertionSort()
printArray()
