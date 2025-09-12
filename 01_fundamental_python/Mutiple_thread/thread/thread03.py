import concurrent.futures
# 算法作用：对字符串每个字符 ^ 1，实现解密 "idmmn!vnsme" → "hello world"。
#
# 线程部分：3 个线程同时在改全局变量 word，所以输出是混乱的、交替的。
#
# 最终结果正确的原因：
#
# 异或 1 的操作本身是可逆的（异或两次就回到原样），所以多线程乱搞也不会破坏最终结果。
#
# 主程序依次取线程返回值，最后 print("".join(word)) 打印出 "hello world"。

def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}: {word}\n", end="")
    return word


if __name__ == "__main__":
    word = list("idmmn!vnsme")
    # 使用 with 语句来确保线程被迅速清理
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(func, "线程1")
        future2 = executor.submit(func, "线程2")
        future3 = executor.submit(func, "线程3")
        word = future1.result()
        word = future2.result()
        word = future3.result()
    print("".join(word))  # hello world
