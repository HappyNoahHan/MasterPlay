from pets import propets
class Caterpie(propets.PropInit):
    health_basic = 45
    attack_basic = 30
    defense_basic = 35
    spell_power_basic = 20
    spell_defense_basic = 20
    speed_basic = 45

    name = '绿毛虫'
    kind = '虫宝宝'
    basic_exp_value = 39

    can_get_base_point = 1
    can_get_base_point_type = 'health'
    capture_rate = 255
    # 精灵编号
    pet_no = '010'
    prop = ['insect']

class Metapod(Caterpie):
    health_basic = 50
    attack_basic = 20
    defense_basic = 55
    spell_power_basic = 25
    spell_defense_basic = 25
    speed_basic = 30

    name = '铁甲蛹'
    kind = '蛹'
    basic_exp_value = 72

    can_get_base_point = 2
    can_get_base_point_type = 'defense'
    capture_rate = 120
    # 精灵编号
    pet_no = '011'

class Butterfree(Caterpie):
    health_basic = 60
    attack_basic = 45
    defense_basic = 50
    spell_power_basic = 90
    spell_defense_basic = 80
    speed_basic = 70

    name = '巴大蝶'
    kind = '蝴蝶'
    basic_exp_value = 178

    can_get_base_point = 3
    can_get_base_point_type = 'spell_power'
    capture_rate = 45
    # 精灵编号
    pet_no = '012'