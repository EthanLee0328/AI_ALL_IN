'''
该案例演示了求整数的阶乘
 5! = 5 * 4 * 3 * 2 *1
'''


def get_factorial(num):
    res = 1
    for n in range(1, num + 1):
        res *= n
    return res


print(get_factorial(5))
print("-" * 20)

def get_factorial2(num):
   return num* get_factorial2(num-1) if num > 1 else 1

print(get_factorial2(5))

