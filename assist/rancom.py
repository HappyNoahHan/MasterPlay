import random

def randomRange():
    '''
    概率随机数
    :return:
    '''
    x = random.randint(1,100)
    if x in range(1,71):
        return 1
    elif x in range(71,81):
        return 2
    elif x in range(81,91):
        return 3
    else:
        return 4

def statusRandom(value):
    x = random.randint(1,100)

    if x <= value:
        return True
    else:
        return False

