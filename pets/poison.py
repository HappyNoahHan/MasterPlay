from pets import propets

class Zubat(propets.PropInit):
    health_basic = 40
    attack_basic = 45
    defense_basic = 35
    spell_power_basic = 30
    spell_defense_basic = 40
    speed_basic = 55

    name = '超音蝠'
    kind = '蝙蝠'
    basic_exp_value = 49

    can_get_base_point = 1
    can_get_base_point_type = 'speed'

    capture_rate = 255
    # 精灵编号
    pet_no = '041'
    prop = ['poison','fly']

class Golbat(Zubat):
    health_basic = 75
    attack_basic = 80
    defense_basic = 70
    spell_power_basic = 65
    spell_defense_basic = 75
    speed_basic = 90

    name = '大嘴蝠'
    kind = '蝙蝠'
    basic_exp_value = 159

    can_get_base_point = 2

    capture_rate = 90
    # 精灵编号
    pet_no = '042'