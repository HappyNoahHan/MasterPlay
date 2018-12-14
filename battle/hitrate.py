import random

def hitOrNot(rate):
    if rate >= 100:
        print("技能命中！")
        return True

    random_number = random.random() * 100

    #测试
    #print(random_number)

    if random_number <= rate:
        print("技能命中！")
        return True
    else:
        print("技能未命中！")
        return False