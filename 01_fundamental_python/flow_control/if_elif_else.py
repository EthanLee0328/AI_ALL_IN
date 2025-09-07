from random import randint

print("此人年龄是:", age := randint(1, 100))

if age<=1:
    print("婴儿")

elif age<=12:
    print("儿童")

elif age<=18:
    print("青少年")

elif age<=65:
    print("成年人")

elif age<=70:
    print("老年")

else:
    print("老Delegate")