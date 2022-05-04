import multiprocessing
import time
import math
import os

def do_work(lower, upper, printLock) :
    printLock.acquire()
    print("Parent process ID:", os.getppid(), "Process ID:", os.getpid())
    printLock.release()
    for i in range(lower, upper) :
        math.sqrt(i)

if __name__ == "__main__":

    printLock = multiprocessing.Lock()
    processes = [multiprocessing.Process(
        target=do_work, 
        args=(i*100_000_000, (i+1)*100_000_000 - 1, printLock)) for i in range(10)]
    
    for p in processes :
        p.start()
    print("All processes started!")

    for p in processes :
       p.join()

    print("All processes joined!")
    
