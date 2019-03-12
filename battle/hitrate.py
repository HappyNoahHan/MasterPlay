import random
from pets import statusmap

def hitOrNot(skill,rate,obj_attack,obj_defense,dodge):
    #ST107 电磁飘浮 免疫地面
    if skill.property == 'ground' and  'ST107' in obj_defense.status:
        print("电磁飘浮 免疫地面属性技能")
        return False
    #ST104 锁定状态 技能必定命中
    if skill.hit_rate == 0 or 'ST104' in obj_defense.status:
        print("%s 必定命中！" % skill.show_name)
        return True

    dodge = statusmap.checkDogeBeforHitCount(obj_defense,dodge)
    print("闪避等级 %s 级" % dodge)

    if obj_attack.level > obj_defense.level:
        level_index = 1 + (obj_attack.level - obj_defense.level) / obj_attack.level
    else:
        level_index = obj_attack.level / obj_defense.level
    real_rate = int((rate * level_index - dodge * 10) * 2.55)
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


def hitForOneHitKill(obj_attack,obj_defense):
    if obj_attack.level < obj_defense.level:
        return False
    else:
        if 'ST104' in obj_defense.status:
            return True
        else:
            hit = 30+obj_attack.level-obj_defense.level
            real_rate = int(hit * 2.55)
            print("真实命中率:", real_rate)

            if real_rate >= 255:
                print("技能命中！")
                return True

            random_number = random.randint(1, 255)

            # 测试
            # print(random_number)

            if random_number <= real_rate:
                print("技能命中！")
                return True
            else:
                print("技能未命中！")
                return False