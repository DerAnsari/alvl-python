import time

timer = int(input("Enter the time to count down in sec"))

for index in range (timer,0,-1):
    sec = index % 60
    mins = int(index/60) %60
    hour = int(index/3600)
    print(f"{hour:02}:{mins:02}:{sec:02}")
    time.sleep(1)

print("Time up")