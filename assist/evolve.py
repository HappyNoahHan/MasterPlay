'''
    进化表
    继承  技能列表  已领悟技能
'''

from pets import fire,rock
from assist import  show
import time

evolve_dict={
    '小火龙': [fire.Charmeleon,11,'level_up'],
    '小拳石': [rock.Graveler,'岩之心','stone_up'],
}
def canEvolveOrNot(obj,stone=None):
    '''
    判断是否又进化形态
    :param obj:
    :return:
    '''
    if obj.name in evolve_dict:
        if evolve_dict[obj.name][2] == 'level_up':
            if obj.level >= evolve_dict[obj.name][1]:
                return True
        elif evolve_dict[obj.name][2] == 'stone_up':
            if stone == evolve_dict[obj.name][1]:
                return True

    return False


def isEvolve(obj):
    '''
    进化属性 重载
    :param obj:
    :return:
    '''
    new_obj = evolve_dict[obj.name][0](level= obj.level,
                                    skill_list=obj.skill_list,
                                    exp_for_current=obj.exp_for_current,
                                    #realize_skill_list=obj.realize_skill_list,
                                    #status=obj.status,
                                    carry_prop=obj.carry_prop,
                                    base_points_list = [obj.health_base_point,
                                                       obj.attack_base_point,
                                                       obj.defense_base_point,
                                                       obj.spell_power_base_point,
                                                       obj.spell_defense_base_point,
                                                       obj.speed_base_point],
                                    has_trainer=True,
                                    autoAi=False)
    new_obj.realize_skill_list = obj.realize_skill_list
    new_obj.status = obj.status
    new_obj.health_indi = obj.health_indi,
    new_obj.attack_indi = obj.attack_indi
    new_obj.defense_indi = obj.defense_indi
    new_obj.spell_power_indi = obj.spell_power_indi
    new_obj.spell_defense_indi = obj.spell_defense_indi
    new_obj.speed_indi = obj.speed_indi

    print("你的 %s 进化成了 %s ！" % (obj.name, new_obj.name))
    time.sleep(5)
    evolveUp(obj,new_obj)

    show.showPetStatus(new_obj)
    return new_obj

def evolveUp(obj,new_obj):
    health_up = new_obj._max_health - obj._max_health
    new_obj.health = obj.health + health_up
    attack_up = new_obj.attack - obj.attack
    defense_up = new_obj.defense - obj.defense
    spell_power_up = new_obj.spell_power - obj.spell_power
    spell_defense_up = new_obj.spell_defense - obj.spell_defense
    speed_up = new_obj.speed -obj.speed

    show.propertyUp(health_up,attack_up,defense_up,spell_power_up,spell_defense_up,speed_up)