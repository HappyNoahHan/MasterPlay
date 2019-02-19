'''
基础伤害＝⌊⌊⌊攻击方等级×2÷5＋2⌋×技能威力×攻击力÷防御力⌋÷50⌋
如果基础伤害＞997，基础伤害＝997。
基础伤害＝基础伤害＋2。
技能伤害结算

加入随机数217~255 平衡伤害
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
from pets import talentmap,pettalent,statusmap,status
from props import propmap
import random

def basicDamage(obj,level,skill,skill_power,attack_value,defense_value,speed):
    '''
    基础伤害
    :param obj:
    :param level:
    :param skill:
    :param attack_value:
    :param defense_value:
    :return:
    '''

    if luckyAttack(speed,skill):
        print("%s 会心一击" % obj.name )
        level *= 2


    basic_damage = ((level * 2)/5 + 2)*skill_power * attack_value / defense_value / 50
    if basic_damage > 997:
        basic_damage = 997
    basic_damage += 2

    random_index = random.randint(217,255)

    basic_damage = int(basic_damage * random_index / 255)



    return basic_damage

def luckyAttack(speed,skill):
    '''
    判断会心一击
    :param speed:
    :return:
    '''
    if speed > 255:
        speed = 255

    if skill.show_name == '飞叶快刀':
        speed *= 4
        if speed > 255:
            speed = 255
        else:
            speed /= 2

    if random.randint(0,255) < speed :
        return True
    else:
        return False


def skillDamage(obj_attack,obj_defense,skill,pro_buff_index):
    '''
    伤害计算
    :param obj_attack:
    :param obj_defense:
    :param skill:
    :return:
    '''

    #计算属性相克关系
    attr_index_number = petattr.getAttrMap(skill,obj_defense)
    print("属性克制关系: ",attr_index_number)
    #计算是否使用的是本属性的技能
    if skill.property in obj_attack.prop:
        skill_prop_match_obj_prop = 1.5
    else:
        skill_prop_match_obj_prop = 1

    # 检查战斗前天赋技能
    power = skill.skill_power
    attack = obj_attack.getAttack()
    defense = obj_defense.getDefense()
    spell_power = obj_attack.getSpellPower()
    spell_defense = obj_defense.getSpellDefense()
    speed = obj_attack.getSpeed()
    print("技能威力: ",power)

    #加入战斗前天赋计算  技能威力提升
    if obj_attack.talent != None:
        if talentmap.checkTalent(obj_attack, 'before'):
            if talentmap.talent_dict[obj_attack.talent].talent_type == '技能威力类型':
                power = talentmap.talent_dict[obj_attack.talent].talentEffect(power)


    #print("技能威力",power)
    # 检查是否有威力加强的道具
    tmp_power_up = propmap.checkCarryPropForSkill(obj_attack, skill)
    #print("威力提升", tmp_power_up)
    power += tmp_power_up
    #print("技能威力", power)
    #判断是物理攻击还是元素攻击
    if skill.spell_skill == True:
        basic_damage = basicDamage(obj_attack,obj_attack.level,skill,power,spell_power,spell_defense,speed)

    else:
        basic_damage = basicDamage(obj_attack,obj_attack.level,skill,power,attack,defense,speed)


    damage = round(basic_damage * pro_buff_index * attr_index_number * skill_prop_match_obj_prop)
    print("基础伤害:",damage)
    #战斗中天赋计算
    if obj_attack.talent != None:
        if talentmap.checkTalent(obj_attack,'middle'):
            damage = talentmap.talentEffectMiddle(obj_attack,skill,damage)
            print("天赋加成伤害",damage)

    #战斗后敌方状态加成
    if obj_defense.status:
        damage = statusmap.checkStatusAfterBattle(obj_defense,skill,damage)
        print("状态加成伤害",damage)

    if damage > 0:
        obj_defense.health -= damage
        print("造成了%s 的伤害" % damage)
    else:
        obj_defense.health -= 1
        show.noDamage()