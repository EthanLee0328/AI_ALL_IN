rabbit = 2
week = 1
while week < 10:
    rabbit = rabbit + rabbit * 2
    week += 1
    print(f"第{week}周的兔子数量是:{rabbit}")

print("==========")

import time

num = 1
while num < 100:
    print("\r" + "=" * num, end="")
    num += 1
    time.sleep(0.5)

print("==========")

rabbit1 = 2
week1 = 1
while week1 < 10:
    rabbit1 = rabbit1 + rabbit1 * 2
    week1 += 1
    if (week1 == 10):  break
else:
    print(f"第{week1}周有{rabbit1}只兔子")
