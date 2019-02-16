import pets.propets

class Pidgey(pets.propets.PropInit):
    health_basic = 40
    attack_basic = 45
    defense_basic = 40
    spell_power_basic = 35
    spell_defense_basic = 35
    speed_basic = 56

    name = '波波'
    kind = '鸟'
    basic_exp_value = 54

    can_get_base_point = 1
    can_get_base_point_type = 'speed'

    capture_rate = 255
    # 精灵编号
    pet_no = '026'
    prop = ['fly','normal']

class Pidgeotto(Pidgey):
    health_basic = 63
    attack_basic = 60
    defense_basic = 55
    spell_power_basic = 50
    spell_defense_basic = 50
    speed_basic = 71

    name = '比比鸟'
    basic_exp_value = 122

    can_get_base_point = 2

    capture_rate = 120
    # 精灵编号
    pet_no = '027'


class Pidgeot(Pidgey):
    health_basic = 83
    attack_basic = 80
    defense_basic = 75
    spell_power_basic = 70
    spell_defense_basic = 70
    speed_basic = 101

    name = '比雕'
    basic_exp_value = 216

    can_get_base_point = 3

    capture_rate = 45
    # 精灵编号
    pet_no = '028'
