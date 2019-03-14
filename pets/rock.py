from pets import propets

class Geodude(propets.PropInit):
    health_basic = 40
    attack_basic = 80
    defense_basic = 100
    spell_power_basic = 30
    spell_defense_basic = 30
    speed_basic = 20

    name = '小拳石'
    kind = '岩石'
    #talent = 'TA002'
    basic_exp_value = 60

    can_get_base_point = 1
    can_get_base_point_type = 'defense'
    capture_rate = 255
    # 精灵编号
    pet_no = '074'
    prop = ['rock','ground']

class Graveler(Geodude):
    health_basic = 55
    attack_basic = 95
    defense_basic = 115
    spell_power_basic = 45
    spell_defense_basic = 45
    speed_basic = 35

    name = '隆隆石'
    #talent = 'TA002'
    basic_exp_value = 137

    can_get_base_point = 2
    capture_rate = 120
    # 精灵编号
    pet_no = '075'

class Golem(Geodude):
    health_basic = 80
    attack_basic = 120
    defense_basic = 130
    spell_power_basic = 55
    spell_defense_basic = 65
    speed_basic = 45

    name = '隆隆岩'
    kind = '重量级'
    #talent = 'TA002'
    basic_exp_value = 223

    can_get_base_point = 3
    capture_rate = 45
    # 精灵编号
    pet_no = '076'

class Onix(propets.PropInit):
    health_basic = 35
    attack_basic = 40
    defense_basic = 160
    spell_power_basic = 30
    spell_defense_basic = 45
    speed_basic = 70

    name = '大岩蛇'
    #talent = 'TA002'
    basic_exp_value = 77

    can_get_base_point = 1
    can_get_base_point_type = 'defense'
    capture_rate = 45
    # 精灵编号
    pet_no = '095'
    prop = ['rock', 'ground']
