#DECLARE arrayData: ARRAY (0:10) OF INTEGER
arrayData= [10,5,6,7,1,12,15,21,8]

def bubbleSort():
    global arrayData
    #DECLARE Temp: INTEGER

    for X in range(0,10):
        for Y in range(0,9):
            if arrayData[Y]< arrayData[Y+1]:
                Temp = arrayData[Y]
                arrayData[Y] = arrayData[Y+1]
                arrayData[Y+1]= Temp
