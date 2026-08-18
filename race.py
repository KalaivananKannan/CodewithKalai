import threading
import time

TOTAL_MB=100
processed_mb=0

lock=threading.Lock()

def processor():
    global processed_mb

    while processed_mb < TOTAL_MB:
        time.sleep(2)
        with lock:
            processed_mb = processed_mb + 2

def progress():
    while True:
        with lock:
            current = processed_mb
        stars = "*" * (current // 2)
        percent = (current/TOTAL_MB) * 100

        print(
            f"\r[{stars:<50}] {current}/{TOTAL_MB} MB ({percent:.0f}%)", end=""
        )

        if current >= TOTAL_MB:
            break
        time.sleep(0.1)
    print("\nProcessing Completed")

t1=threading.Thread(target=processor)
t2=threading.Thread(target=progress)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program Finished")