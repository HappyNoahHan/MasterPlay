import pets.propets

class Clefairy(pets.propets.PropInit):
    health_basic = 70
    attack_basic = 45
    defense_basic = 48
    spell_power_basic = 60
    spell_defense_basic = 65
    speed_basic = 35

    name = '皮皮'
    kind = '妖精'
    basic_exp_value = 113

    can_get_base_point = 2
    can_get_base_point_type = 'health'

    capture_rate = 150
    # 精灵编号
    pet_no = '035'
    prop = ['fairy']

class Clefable(Clefairy):
    health_basic = 95
    attack_basic = 70
    defense_basic = 73
    spell_power_basic = 95
    spell_defense_basic = 90
    speed_basic = 60

    name = '皮可西'
    basic_exp_value = 217

    can_get_base_point = 3

    capture_rate = 25
    # 精灵编号
    pet_no = '036'

class Jigglypuff(pets.propets.PropInit):
    health_basic = 115
    attack_basic = 45
    defense_basic = 20
    spell_power_basic = 45
    spell_defense_basic = 25
    speed_basic = 20

    name = '胖丁'
    kind = '气球'
    basic_exp_value = 95

    can_get_base_point = 2
    can_get_base_point_type = 'health'

    capture_rate = 170
    # 精灵编号
    pet_no = '039'
    prop = ['fairy','normal']

class Wigglytuff(pets.propets.PropInit):
    health_basic = 140
    attack_basic = 70
    defense_basic = 45
    spell_power_basic = 85
    spell_defense_basic = 50
    speed_basic = 45

    name = '胖可丁'
    kind = '气球'
    basic_exp_value = 196

    can_get_base_point = 3
    can_get_base_point_type = 'health'

    capture_rate = 50
    # 精灵编号
    pet_no = '040'
    prop = ['fairy','normal']