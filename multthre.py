import threading
import time

count=0
lock =threading.Lock()
def task(name):
    global count
    for i in range(100000000):
        # print(f"{name}: {i}")
        # time.sleep(5)
        count=count+1
        # time.sleep(1)



def task1(name):
    for i in range(10):
        print(f"{name}: {i}")
        print(input("enter number"))
        time.sleep(1)

t1=threading.Thread(target=task, args=("Thread-1",))
t2=threading.Thread(target=task, args=("Thread-2",))
t3=threading.Thread(target=task1, args=("Thread-2",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(count)
print("Done")