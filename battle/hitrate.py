import random

def hitOrNot(rate,obj_attack,obj_defense,dodge):
    if obj_attack.level > obj_defense.level:
        level_index = 1 + (obj_attack.level - obj_defense.level) / obj_attack.level
    else:
        level_index = obj_attack.level / obj_defense.level
    real_rate = int((rate * level_index - dodge) * 2.55)
    print("真实命中率:",real_rate)

    if real_rate >= 255:
        print("技能命中！")
        return True

    random_number = random.randint(1,255)

    #测试
    #print(random_number)

    if random_number <= real_rate:
        print("技能命中！")
        return True
    else:
        print("技能未命中！")
        return False