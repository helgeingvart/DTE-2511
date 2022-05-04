from multiprocessing import Pool
import time

delta = 1_000
range_starts = range(100_000_000, 160_000_001, delta)

def sum_squares(num_start) :
    return sum(i*i for i in range(num_start, num_start + delta))

def find_sum_multiprocessing() :
    with Pool() as pool :
        res = pool.map(sum_squares, range_starts)
        total = sum(res)
        print(total)

def find_sum_nomultiprocessing() :
    sum = 0
    for i in range_starts :
        sum += sum_squares(i)
    print(f"{sum:,}")


if __name__ == "__main__" :
    start_time = time.time()
    find_sum_nomultiprocessing()
    duration = time.time() - start_time
    print("Multiprocessing used", duration, "number of seconds")

