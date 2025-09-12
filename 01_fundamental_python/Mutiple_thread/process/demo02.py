import os
import multiprocessing


class Worker(multiprocessing.Process):
    def run(self):
        print("进程id：", os.getpid(), "\t父进程id：", os.getppid())


if __name__ == "__main__":
    for i in range(5):
        p = Worker()
        p.start()
