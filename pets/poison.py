from pets import propets
class Nidoran(propets.PropInit):
    health_basic = 55
    attack_basic = 47
    defense_basic = 52
    spell_power_basic = 40
    spell_defense_basic = 40
    speed_basic = 41

    name = '尼多兰'
    kind = '毒针'
    basic_exp_value = 55

    can_get_base_point = 1
    can_get_base_point_type = 'health'

    capture_rate = 235
    # 精灵编号
    pet_no = '029'
    prop = ['poison']

class Nidorina(Nidoran):
    health_basic = 70
    attack_basic = 62
    defense_basic = 67
    spell_power_basic = 55
    spell_defense_basic = 55
    speed_basic = 56

    name = '尼多娜'
    basic_exp_value = 128

    can_get_base_point = 2

    capture_rate = 120
    # 精灵编号
    pet_no = '030'

class Nidoqueen(Nidoran):
    health_basic = 90
    attack_basic = 92
    defense_basic = 87
    spell_power_basic = 75
    spell_defense_basic = 85
    speed_basic = 76

    name = '尼多后'
    kind = '钻锥'
    basic_exp_value = 227

    can_get_base_point = 3

    capture_rate = 45
    # 精灵编号
    pet_no = '031'
    prop = ['poison', 'ground']

class NidoranX(propets.PropInit):
    health_basic = 46
    attack_basic = 57
    defense_basic = 40
    spell_power_basic = 40
    spell_defense_basic = 40
    speed_basic = 50

    name = '尼多朗'
    kind = '毒针'
    basic_exp_value = 55

    can_get_base_point = 1
    can_get_base_point_type = 'attack'

    capture_rate = 235
    # 精灵编号
    pet_no = '032'
    prop = ['poison']

class Nidorino(NidoranX):
    health_basic = 61
    attack_basic = 72
    defense_basic = 57
    spell_power_basic = 55
    spell_defense_basic = 55
    speed_basic = 65

    name = '尼多力诺'
    basic_exp_value = 128

    can_get_base_point = 2

    capture_rate = 120
    # 精灵编号
    pet_no = '033'

class Nidoking(NidoranX):
    health_basic = 81
    attack_basic = 102
    defense_basic = 77
    spell_power_basic = 85
    spell_defense_basic = 75
    speed_basic = 85

    name = '尼多王'
    kind = '钻锥'
    basic_exp_value = 227

    can_get_base_point = 3

    capture_rate = 45
    # 精灵编号
    pet_no = '034'
    prop = ['poison','ground']

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