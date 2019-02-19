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