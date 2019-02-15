'''
    辅助计算 包括战前 战后
    计算获得的 基础点数
'''
from battle import buff


def checkBuffBeforeBattle(obj_attack,obj_defense):
    '''
    检查buff收益
    :param obj_attack:
    :param obj_defense:
    :return:
    '''
    if obj_attack.buff_dict:
        buff.buffCount(obj_attack)
        buff.buffIndex(obj_attack)
    else:
        print("目标没有buff")

    if obj_defense.buff_dict:
        buff.buffCount(obj_defense)

def checkBuffAfterBattle(obj_attack):
    '''
    战后buff 计算
    :param obj_attack:
    :param obj_defense:
    :return:
    '''
    if obj_attack.debuff_dict:
        buff.damageDebuffCount(obj_attack) #行动后debuff 计算

    if obj_attack.property_buff:
        buff.proBuffindex(obj_attack) #属性增强buff 次数计算

def getBasePoint(obj_attack,obj_defense):
    '''
    计算获得的基础点数
    :param obj_attack:
    :param obj_defense:
    :return:
    '''
    if obj_defense.can_get_base_point_type == 'health':
        obj_attack.health_base_point += obj_defense.can_get_base_point
        if obj_attack.health_base_point > 255:
            obj_attack.health_base_point = 255

    if obj_defense.can_get_base_point_type == 'attack':
        obj_attack.attack_base_point += obj_defense.can_get_base_point
        if obj_attack.attack_base_point > 255:
            obj_attack.attack_base_point = 255

    if obj_defense.can_get_base_point_type == 'defense':
        obj_attack.defense_base_point += obj_defense.can_get_base_point
        if obj_attack.defense_base_point > 255:
            obj_attack.defense_base_point = 255

    if obj_defense.can_get_base_point_type == 'spell_power':
        obj_attack.spell_power_base_point += obj_defense.can_get_base_point
        if obj_attack.spell_power_base_point > 255:
            obj_attack.spell_power_base_point = 255

    if obj_defense.can_get_base_point_type == 'spell_defense':
        obj_attack.spell_defense_base_point += obj_defense.can_get_base_point
        if obj_attack.spell_defense_base_point > 255:
            obj_attack.spell_defense_base_point = 255

    if obj_defense.can_get_base_point_type == 'speed':
        obj_attack.speed_base_point += obj_defense.can_get_base_point
        if obj_attack.speed_base_point > 255:
            obj_attack.speed_base_point = 255