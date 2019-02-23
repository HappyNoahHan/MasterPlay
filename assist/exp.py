from assist import cap,show
from battle import learnskill
from pets import  skilltree
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


def getBattleSuccessExp(player,obj,exp_basic = 1,ai_index=1,carry_prop=1):
    '''
    战斗获胜经验
    :param lv:
    :return:
    '''
    if obj.autoAi == True:
        if obj.has_trainer == None:
            ai_index = 10

    if len(player.battle_pet_list) > 1:
        exp_basic = 0.5

    print("经验基数",exp_basic)
    print("调整基数",ai_index)
    print("经验学习机器基数",carry_prop)

    #后续版本 随身道具
    #if withExpfruit == True:
    #    fruit_index = 1.5
    #else:
    #    fruit_index = 1

    got_exp = int((obj.level * obj.basic_exp_value)/7 * ai_index * exp_basic * carry_prop)

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
        try:
            if obj.level in skilltree.pet_skill_tree[obj.pet_no]:
                realize_or_not =learnskill.learnSkill(obj,skilltree.pet_skill_tree[obj.pet_no][obj.level])

                if realize_or_not == False:
                    print("技能已经领悟")
                    pass
        except AttributeError:
            print("测试代码,该精灵未添加技能树")


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


