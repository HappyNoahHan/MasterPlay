from pets import  propets

class Magnemite(propets.PropInit):
    health_basic = 25
    attack_basic = 35
    defense_basic = 70
    spell_power_basic = 90
    spell_defense_basic = 55
    speed_basic = 45

    name = '小磁怪'
    kind = '磁铁'
    basic_exp_value = 65

    can_get_base_point = 1
    can_get_base_point_type = 'spell_power'
    capture_rate = 190
    # 精灵编号
    pet_no = '081'
    prop = ['electric','steel']

class Magneton(Magnemite):
    health_basic = 50
    attack_basic = 60
    defense_basic = 95
    spell_power_basic = 120
    spell_defense_basic = 70
    speed_basic = 70

    name = '三合一磁怪'
    basic_exp_value = 163

    can_get_base_point = 2
    capture_rate = 60
    # 精灵编号
    pet_no = '082'