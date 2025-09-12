import time
import threading
from sys import flags


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        flag = 0
        while True:
            print(f"\r{self.name}:{str(flag) * 5}", end="")
            flag = flag ^ 1
            time.sleep(0.2)
if __name__ == '__main__':
    t1 = Worker("线程1")
    t2 = Worker("线程2")
    t1.start()
    t2.start()
