import threading

# Create two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_1_task():
    with lock1:
        print("Thread 1 acquired lock1")
        with lock2:
            print("Thread 1 acquired lock2")

def thread_2_task():
    with lock2:
        print("Thread 2 acquired lock2")
        with lock1:
            print("Thread 2 acquired lock1")

# Create two threads
thread1 = threading.Thread(target=thread_1_task)
thread2 = threading.Thread(target=thread_2_task)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()
