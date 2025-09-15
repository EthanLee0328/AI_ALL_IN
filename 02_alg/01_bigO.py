import time

# list = [i for i in range(100000000)]
list = [i for i in range(10)]


def num_sun(nums):
    start_time = time.time()
    sum_num = 0
    i = -1
    while (i := i + 1) < len(nums):
        sum_num += nums[i]
    end_time = time.time()
    print(f'while循环耗时:{end_time-start_time}')
    return sum_num



print(num_sun(list))


def max_num(nums):
    max_num=nums[0]
    i=0
    while(i:=i+1)<len(nums):
        if nums[i]>max_num:
            max_num=nums[i]
    return max_num



print(max_num(list))



print(1<<10)