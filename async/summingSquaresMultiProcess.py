import multiprocessing
import time

delta = 1000

def sum_squares(number_start):
    return sum(i * i for i in range(number_start, number_start*delta))


def find_sums_multiprocessing():
    # Create various range starts:
    range_starts = range(10_000, 20_000, delta)
    # range_starts = print(list(range_starts))
    with multiprocessing.Pool() as pool:
        res = pool.map(sum_squares, range_starts)
        print(res)
        total = sum(res)
        print(total)

def find_sums_nomultiprocessing() :
    range_starts = range(10_000, 20_000, delta)
    sum = 0
    for i in range_starts:
        sum += sum_squares(i)
    print(sum)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums_multiprocessing()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

    start_time = time.time()
    find_sums_nomultiprocessing()
    duration = time.time() - start_time

    print(f"Duration {duration} seconds")
