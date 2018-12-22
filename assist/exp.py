from pets import pet, wood, fire, fly
from assist import cap,evolve,show
from battle import learnskill
import math
import random
import time


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


def getBattleSuccessExp(obj,exp_basic = 1):
    '''
    战斗获胜经验
    :param lv:
    :return:
    '''
    if obj.autoAi == True:
        ai_index = 1
    else:
        ai_index = 1.5

    if 'ST999' in obj.exp_status:
        exp_basic = 0.5

    print("经验基数",exp_basic)

    #后续版本 随身道具
    #if withExpfruit == True:
    #    fruit_index = 1.5
    #else:
    #    fruit_index = 1

    got_exp = int((obj.level * obj.basic_exp_value)/7 * ai_index * exp_basic)

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
        #增加点执行时间
        time.sleep(1)

        #判断是否学习可以学习新技能
        if obj.level in obj.skill_tree:
            realize_or_not =learnskill.learnSkill(obj,obj.skill_tree[obj.level])

            if realize_or_not == False:
                print("技能已经领悟")
                pass

        return isLevelUp(obj)
    else:
        return True


def levelUp(obj):
    '''
    升级 属性增加
    :param obj:
    :return:
    '''
    health_up = cap.gethpCapValue(obj.health_basic, obj.level, obj.health_indi,obj.health_base_point) - obj._max_health
    attack_up = cap.getCapValue(obj.attack_basic, obj.level, obj.attack_indi,obj.attack_base_point) - obj.attack
    defense_up = cap.getCapValue(obj.defense_basic, obj.level, obj.defense_indi,obj.defense_base_point) - obj.defense
    spell_power_up = cap.getCapValue(obj.spell_power_basic, obj.level, obj.spell_power_indi,obj.spell_power_base_point) - obj.spell_power
    spell_defense_up = cap.getCapValue(obj.spell_defense_basic, obj.level, obj.spell_defense_indi,obj.spell_defense_base_point) -obj.spell_defense
    speed_up = cap.getCapValue(obj.speed_basic, obj.level, obj.speed_indi,obj.speed_base_point) - obj.speed

    #属性改变
    obj._max_health += health_up
    obj.health += health_up
    obj.attack += attack_up
    obj.defense += defense_up
    obj.spell_power += spell_power_up
    obj.spell_defense += spell_defense_up
    obj.speed += speed_up

    show.propertyUp(health_up,attack_up,defense_up,spell_power_up,spell_defense_up,speed_up)


