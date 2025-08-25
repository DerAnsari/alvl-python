#Task 1
print("|------Task 1------|")
returnStr = ""
for i in range(1,10):
    for j in range(i):
        returnStr += str(i)
    print(returnStr)
    returnStr = ""

#Task 2 
print("|------Task 2------|")
star = ""
for x in range(8):
    for y in range(x):
        star+= "*"
    print(star)
    star = ""
#Task 3 
print("|------Task 3------|")
starReverse = ""
for w in range(8,-1,-1):
    for v in range(w):
        starReverse+= "*"
    print(starReverse)
    starReverse = ""
#Task 4
print("|------Task 4------|")
#import time 
# returnCount = ""
# for count in range(1,6):
#     for index in range(5,0,-1):
#         time.sleep(1)
#     returnCount += str(count)
#     print(returnCount)

import time

def clear_line():
    print('\r' + ' ' * 10, end='\r', flush=True)  # Clear current line

for count in range(1, 6):
    for _ in range(count):
        print(f"\r{count}", end='', flush=True)
        time.sleep(1)
        clear_line()
        time.sleep(5)

print("\n|---finished---|")
print("|---finished---|")
