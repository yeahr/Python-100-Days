import random

num = random.randint(0,100)
while True:
    gus=int(input("猜一下"))
    if num>gus:
        print("大一点")
    elif num<gus:
        print("小一点")
    else:
        print("Great")
        break
