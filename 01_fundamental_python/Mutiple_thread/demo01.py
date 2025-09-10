import time
import multiprocessing
import os

print(os.getcwd())

def write_file():
    with open('test.txt', 'a') as f:
        while True:
            f.write('hello world\n')
            f.flush()
            time.sleep(1)


def read_file():
    with open('test.txt', 'r') as f:
        while True:
            time.sleep(1)
            print(f.readline().strip())


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)
    p1.start()
    p2.start()

