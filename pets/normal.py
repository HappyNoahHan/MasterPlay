from pets import propets
class Rattata(propets.PropInit):
    health_basic = 30
    attack_basic = 56
    defense_basic = 35
    spell_power_basic = 25
    spell_defense_basic = 35
    speed_basic = 72

    name = '小拉达'
    kind = '鼠'
    basic_exp_value = 51

    can_get_base_point = 1
    can_get_base_point_type = 'speed'
    capture_rate = 255
    # 精灵编号
    pet_no = '019'
    prop = ['normal']


class Raticate(Rattata):
    health_basic = 55
    attack_basic = 81
    defense_basic = 60
    spell_power_basic = 50
    spell_defense_basic = 70
    speed_basic = 97

    name = '拉达'
    kind = '鼠'
    basic_exp_value = 145

    can_get_base_point = 2
    capture_rate = 127
    # 精灵编号
    pet_no = '020'