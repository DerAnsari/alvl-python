import threading
import time 

def walk_dog():
    time.sleep(8)
    print("you finished walking the dog") 

def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def get_mail():
    time.sleep(4)
    print("you got mail")

chore1 = threading.Thread(target = walk_dog)
chore2 = threading.Thread(target = take_out_trash)
chore3 = threading.Thread(target = get_mail)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores have been completed successfully")
