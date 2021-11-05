import asyncio
import multiprocessing
import math
import time


async def cubic(n):
    return pow(n, 2)


def cubic_(n):
    return pow(n, 2)


async def squares(n):
    return pow(n, 2)


def squares_(n):
    return pow(n, 2)


async def factorial(n):
    return math.factorial(n)


def factorial_(n):
    return math.factorial(n)


async def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fib_(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


async def gather_task():
    l1, l2, l3, l4 = [], [], [], []
    for i in range(1, 11):
        temp = await asyncio.gather(
            cubic(i),
            squares(i),
            factorial(i),
            fib(i),
        )
        l1.append(temp[0])
        l2.append(temp[1])
        l3.append(temp[2])
        l4.append(temp[3])
    return l1, l2, l3, l4


def main():
    # r1, r2, r3, r4 = [], [], [], []
    # for i in range(1, 11):
    #     r1.append(pool.apply_async(cubic_, (i,)).get())
    #     r2.append(pool.apply_async(squares_, (i,)).get())
    #     r3.append(pool.apply_async(factorial_, (i,)).get())
    #     r4.append(pool.apply_async(fib_, (i,)).get())             Так повільніше
    with multiprocessing.Pool(processes=4) as pool:
        r1 = pool.map(cubic_, range(1, 11))
        r2 = pool.map(squares_, range(1, 11))
        r3 = pool.map(factorial_, range(1, 11))
        r4 = pool.map(fib_, range(1, 11))
        return r1, r2, r3, r4


if __name__ == '__main__':
    time_bef_async = time.time()
    loop = asyncio.get_event_loop().run_until_complete(gather_task())
    time_aft_async = time.time() - time_bef_async
    print(f'\n{loop} \ntime {time_aft_async}\n')

    time_bef_def = time.time()
    r = main()
    time_aft_def = time.time() - time_bef_def
    print(f"{r} \ntime {time_aft_def}")
