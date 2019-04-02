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

class Meowth(propets.PropInit):
    health_basic = 40
    attack_basic = 45
    defense_basic = 35
    spell_power_basic = 40
    spell_defense_basic = 40
    speed_basic = 90

    name = '喵喵'
    kind = '妖怪猫'
    basic_exp_value = 58

    can_get_base_point = 1
    can_get_base_point_type = 'speed'
    capture_rate = 255
    # 精灵编号
    pet_no = '052'
    prop = ['normal']

class Persian(propets.PropInit):
    health_basic = 65
    attack_basic = 70
    defense_basic = 60
    spell_power_basic = 65
    spell_defense_basic = 65
    speed_basic = 115

    name = '猫老大'
    kind = '暹罗猫'
    basic_exp_value = 154

    can_get_base_point = 2
    can_get_base_point_type = 'speed'
    capture_rate = 90
    # 精灵编号
    pet_no = '053'
    prop = ['normal']
