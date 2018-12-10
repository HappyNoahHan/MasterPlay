'''
基础伤害＝⌊⌊⌊攻击方等级×2÷5＋2⌋×技能威力×攻击力÷防御力⌋÷50⌋
如果基础伤害＞997，基础伤害＝997。
基础伤害＝基础伤害＋2。
技能伤害结算
:return:
判断是否会心一击
会心一击判定
设X＝攻击方速度，如果X＞255，X＝255。
如果技能是空手刀、飞叶快刀、蟹钳锤或切裂，X＝X×4，如果X＞255，X＝255；否则X＝⌊X÷2⌋。
从0～255
中产生随机数R，如果R＜X，发生会心一击
'''

from battle import buff,skill,skilllistmap
from assist import petattr,ppvalue,show
import random

def basicDamage(obj,level,skill,attack_value,defense_value):
    '''
    基础伤害
    :param obj:
    :param level:
    :param skill:
    :param attack_value:
    :param defense_value:
    :return:
    '''
    if luckyAttack(obj.speed,skill):
        print("%s 会心一击" % obj.name )
        level *= 2


    basic_damage = ((level * 2)/5 + 2)*skill.skill_power * attack_value / defense_value / 50
    if basic_damage > 997:
        basic_damage = 997
    basic_damage += 2



    return basic_damage

def luckyAttack(speed,skill):
    '''
    判断会心一击
    :param speed:
    :return:
    '''
    if speed > 255:
        speed = 255

    if skill.skill_show_name == '飞叶快刀':
        speed *= 4
        if speed > 255:
            speed = 255
        else:
            speed /= 2

    if random.randint(0,255) < speed :
        return True
    else:
        return False


def skillDamage(obj_attack,obj_defense,skill):
    '''
    伤害计算
    :param obj_attack:
    :param obj_defense:
    :param skill:
    :return:
    '''
    # 计算属性增幅，道具增幅等后续
    pro_buff_index = 1
    if obj_attack.property_buff:
        pro_buff_list = buff.proBuffCount(obj_attack)
        if pro_buff_list:
            pro_buff_index = sum(pro_buff_list)
    #计算属性相克关系 有点问题 克制问题
    attr_index_number = petattr.getAttrMap(skill,obj_defense)
    print(attr_index_number)
    #计算是否使用的是本属性的技能
    if skill.property in obj_attack.property:
        skill_prop_match_obj_prop = 1.5
    else:
        skill_prop_match_obj_prop = 1


    #判断是物理攻击还是元素攻击
    if skill.spell_skill == True:
        basic_damage = basicDamage(obj_attack,obj_attack.level,skill,obj_attack.getSpellPower(),obj_defense.getSpellDefense())

    else:
        basic_damage = basicDamage(obj_attack,obj_attack.level,skill,obj_attack.getAttack(),obj_defense.getDefense())


    damage = round(basic_damage * pro_buff_index * attr_index_number * skill_prop_match_obj_prop)

    if damage > 0:
        obj_defense.health -= damage
        print("造成了%s 的伤害" % damage)
    else:
        obj_defense.health -= 1
        show.noDamage()