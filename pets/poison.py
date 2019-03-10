from pets import propets
class Ekans(propets.PropInit):
    health_basic = 35
    attack_basic = 60
    defense_basic = 44
    spell_power_basic = 40
    spell_defense_basic = 54
    speed_basic = 55

    name = '阿柏蛇'
    kind = '蛇'
    basic_exp_value = 58

    can_get_base_point = 1
    can_get_base_point_type = 'attack'

    capture_rate = 255
    # 精灵编号
    pet_no = '023'
    prop = ['poison']

class Arbok(Ekans):
    health_basic = 60
    attack_basic = 95
    defense_basic = 69
    spell_power_basic = 65
    spell_defense_basic = 79
    speed_basic = 80

    name = '阿柏怪'
    basic_exp_value = 157

    can_get_base_point = 2

    capture_rate = 90
    # 精灵编号
    pet_no = '024'



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

class Grimer(propets.PropInit):
    health_basic = 80
    attack_basic = 80
    defense_basic = 50
    spell_power_basic = 40
    spell_defense_basic = 50
    speed_basic = 25

    name = '臭泥'
    kind = '污泥'
    basic_exp_value = 65

    can_get_base_point = 1
    can_get_base_point_type = 'health'

    capture_rate = 190
    # 精灵编号
    pet_no = '088'
    prop = ['poison']

class Muk(propets.PropInit):
    health_basic = 105
    attack_basic = 105
    defense_basic = 75
    spell_power_basic = 65
    spell_defense_basic = 100
    speed_basic = 50

    name = '臭臭泥'
    basic_exp_value = 175

    can_get_base_point_type = ['health','attack']

    capture_rate = 75
    # 精灵编号
    pet_no = '089'