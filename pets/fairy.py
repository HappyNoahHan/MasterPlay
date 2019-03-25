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