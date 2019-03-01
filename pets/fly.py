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
    talent = 'TA001'

    can_get_base_point = 1
    can_get_base_point_type = 'speed'

    capture_rate = 255
    # 精灵编号
    pet_no = '016'
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
    pet_no = '017'


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
    pet_no = '018'

class Spearow(pets.propets.PropInit):
    health_basic = 40
    attack_basic = 60
    defense_basic = 30
    spell_power_basic = 31
    spell_defense_basic = 31
    speed_basic = 70

    name = '烈雀'
    kind = '鸟'
    basic_exp_value = 52
    #talent = 'TA001'

    can_get_base_point = 1
    can_get_base_point_type = 'speed'

    capture_rate = 255
    # 精灵编号
    pet_no = '021'
    prop = ['fly','normal']

class Fearow(Spearow):
    health_basic = 65
    attack_basic = 90
    defense_basic = 65
    spell_power_basic = 61
    spell_defense_basic = 61
    speed_basic = 100

    name = '大嘴雀'
    kind = '鸟'
    basic_exp_value = 155
    #talent = 'TA001'

    can_get_base_point = 2

    capture_rate = 90
    # 精灵编号
    pet_no = '022'