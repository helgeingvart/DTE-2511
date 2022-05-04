from multiprocessing import Process, Lock
import math
import os


def do_work(lower, upper, lock) :

    lock.acquire()
    print("Parent pid:", os.getppid(), ", process id:", os.getpid())
    lock.release()
    for i in range(lower, upper) :
        math.sqrt(i)

if __name__ == "__main__":
    
    lock = Lock()
    processes = [ Process(
        name = f"Worker {i}", 
        target=do_work, 
        args=(i*10_000_000, (i+1)*10_000_000 - 1, 
        lock) 
    ) for i in range(10)
    ]

    for p in processes :
        p.start()

    print("All processes started")

    for p in processes :
        p.join()

