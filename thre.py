import threading
import time
# def task():
#     print("Task Running")
#     time.sleep(5)
#     print("Sleeping")
# t=threading.Thread(target=task)
# t.start()
# t.join(ti)
# print(t.is_alive())
# def background_task():
#     while True:
#         print("Daemon thread working")
#         time.sleep(1)

# t=threading.Thread(target=background_task)
# t.daemon = True
# t.start()

# print("Main program ends in 3 second ...")
# time.sleep(3)
# print("Main program ends!!!")

def logger():
    while True:
        Print("Log: system running")
        time.sleep(2)
log_thread=threading.Thread(target=logger, daemon=True)
log_thread.start()

print("Main program doing important work")
time.sleep(5)
print("Main program ends")