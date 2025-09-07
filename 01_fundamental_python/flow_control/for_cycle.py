for i in range(10, -10, -3):
    print(i)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end="\t")
    print()

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
