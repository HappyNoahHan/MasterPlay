from pets import pet, wood, fire, fly
from assist import cap
import math
import random


def getExpForUp(lv):
    '''
    求升级经验值
    :param lv:
    :return:
    '''
    if lv > 1:
        return pow(lv + 1, 3) - pow(lv, 3)
    else:
        return 1


def getBattleSuccessExp(obj):
    '''
    战斗获胜经验
    :param lv:
    :return:
    '''
    if obj.autoAi == True:
        ai_index = 1
    else:
        ai_index = 1.5

    #后续版本 随身道具
    #if withExpfruit == True:
    #    fruit_index = 1.5
    #else:
    #    fruit_index = 1

    got_exp = round((obj.level * obj.basic_exp_value)/7 * ai_index * 1)

    return got_exp




def isLevelUp(obj):
    '''
    判断是否升级
    :param obj:
    :return:
    '''
    if obj.level == 100:
        print("%s 已经是最高等级" % obj.name)
        return True

    if obj.exp_for_current >= getExpForUp(obj.level):

        obj.exp_for_current -= getExpForUp(obj.level)

        print('%s 升到 %s 级！' % (obj.name,obj.level))
        levelUp(obj)
        obj.level += 1
        return isLevelUp(obj)
    else:
        return True


def levelUp(obj):
    '''
    升级 属性增加
    :param obj:
    :return:
    '''
    one_up = propUp(obj)

    health_up = random.randint(int(one_up[0]),int(one_up[0])+1)
    print("生命 up %s !" % health_up)
    obj._max_health += health_up
    obj.health += health_up

    attack_up = random.randint(int(one_up[1]),int(one_up[1]+1))
    obj.attack += attack_up
    print("攻击 up %s !" % attack_up)

    defense_up = random.randint(int(one_up[2]),int(one_up[2]+1))
    obj.defense += defense_up
    print("防御 up %s !" % defense_up)

    spell_power_up = random.randint(int(one_up[3]),int(one_up[3])+1)
    obj.spell_power += spell_power_up
    print("法攻 up %s !" % spell_power_up)

    spell_defense_up = random.randint(int(one_up[4]),int(one_up[4])+1)
    obj.spell_defense += spell_defense_up
    print("法防 up %s !" % spell_defense_up)

    speed_up = random.randint(int(one_up[5]),int(one_up[5])+1)
    obj.speed += speed_up
    print("速度 up %s !" % speed_up)


def propUp(obj):
    '''
    升1级属性判定
    :param obj:
    :return:
    '''
    health_up = cap.gethpCapValueForOne(obj.health_basic)
    attack_up = cap.getCapValueForOne(obj.attack_basic)
    defense_up = cap.getCapValueForOne(obj.defense_basic)
    spell_power_up = cap.getCapValueForOne(obj.spell_power_basic)
    spell_defense_up = cap.getCapValueForOne(obj.spell_defense_basic)
    speed = cap.getCapValueForOne(obj.speed_basic)

    return [health_up,attack_up,defense_up,spell_power_up,spell_defense_up,speed]