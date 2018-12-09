from pets import pet, wood, fire, fly
from assist import cap,evolve
from battle import learnskill
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
        obj.level += 1
        print('%s 升到 %s 级！' % (obj.name, obj.level))

        levelUp(obj)

        #判断是否学习可以学习新技能
        if obj.level in obj.skill_tree:
            learnskill.learnSkill(obj,obj.skill_tree[obj.level])


        return isLevelUp(obj)
    else:
        return True


def levelUp(obj):
    '''
    升级 属性增加
    :param obj:
    :return:
    '''
    health_up = cap.gethpCapValueForOne(obj.health_basic, obj.level, obj.health_indi)
    attack_up = cap.getCapValueForOne(obj.attack_basic, obj.level, obj.attack_indi)
    defense_up = cap.getCapValueForOne(obj.defense_basic, obj.level, obj.defense_indi)
    spell_power_up = cap.getCapValueForOne(obj.spell_power_basic, obj.level, obj.spell_power_indi)
    spell_defense_up = cap.getCapValueForOne(obj.spell_defense_basic, obj.level, obj.spell_defense_indi)
    speed_up = cap.getCapValueForOne(obj.speed_basic, obj.level, obj.speed_indi)


    print("生命 up %s !" % health_up)
    obj._max_health += health_up
    obj.health += health_up


    obj.attack += attack_up
    print("攻击 up %s !" % attack_up)


    obj.defense += defense_up
    print("防御 up %s !" % defense_up)


    obj.spell_power += spell_power_up
    print("法攻 up %s !" % spell_power_up)


    obj.spell_defense += spell_defense_up
    print("法防 up %s !" % spell_defense_up)


    obj.speed += speed_up
    print("速度 up %s !" % speed_up)