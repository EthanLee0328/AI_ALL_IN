import os
import time
import multiprocessing


def func():
    for i in range(10):
        print(os.getpid(), i)
        time.sleep(0.5)


if __name__ == '__main__':
    process_num = 5
    pool = multiprocessing.Pool(process_num)
    for i in range(process_num):
        pool.apply_async(func)
    pool.close()
    pool.join()

    print('end')
