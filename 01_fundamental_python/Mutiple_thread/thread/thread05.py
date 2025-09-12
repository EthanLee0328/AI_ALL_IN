import time
import threading


def func():
    global g_num
    for _ in range(10):
        lock.acquire()
        tmp = g_num + 1
        time.sleep(0.01)
        g_num = tmp
        lock.release()
        print(f"{threading.current_thread().name}: {g_num}\n", end="")


if __name__ == "__main__":
    g_num = 0
    lock = threading.Lock()
    threads = [threading.Thread(target=func, name=f"线程{i}") for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(g_num)  # 30
