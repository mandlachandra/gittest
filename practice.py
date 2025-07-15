import threading
import time

def print_numbers():
    for i in range(5):
        print("Thread:",i)
        time.sleep(2)

#create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers)

t1.start()
t2.start()

t1.join()
t2.join()
print("Done!")