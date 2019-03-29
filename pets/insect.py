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


class Weedle(propets.PropInit):
    health_basic = 40
    attack_basic = 35
    defense_basic = 30
    spell_power_basic = 20
    spell_defense_basic = 20
    speed_basic = 50

    name = '独角虫'
    kind = '毛毛虫'
    basic_exp_value = 39

    can_get_base_point = 1
    can_get_base_point_type = 'speed'
    capture_rate = 255
    # 精灵编号
    pet_no = '013'
    prop = ['insect','poison']

class Kakuna(Weedle):
    health_basic = 45
    attack_basic = 25
    defense_basic = 50
    spell_power_basic = 25
    spell_defense_basic = 25
    speed_basic = 35

    name = '铁壳蛹'
    kind = '蛹'
    basic_exp_value = 72

    can_get_base_point = 2
    can_get_base_point_type = 'defense'
    capture_rate = 120
    # 精灵编号
    pet_no = '014'

class Beedrill(Weedle):
    health_basic = 65
    attack_basic = 90
    defense_basic = 40
    spell_power_basic = 45
    spell_defense_basic = 80
    speed_basic = 75

    name = '大针蜂'
    kind = '毒蜂'
    basic_exp_value = 178

    can_get_base_point = 3
    can_get_base_point_type = 'attack'
    capture_rate = 45
    # 精灵编号
    pet_no = '015'

class Paras(propets.PropInit):
    health_basic = 35
    attack_basic = 70
    defense_basic = 55
    spell_power_basic = 45
    spell_defense_basic = 55
    speed_basic = 25

    name = '派拉斯'
    kind = '蘑菇'
    basic_exp_value = 57

    can_get_base_point = 1
    can_get_base_point_type = 'attack'
    capture_rate = 190
    # 精灵编号
    pet_no = '046'
    prop = ['insect','wood']

class Parasect(propets.PropInit):
    health_basic = 60
    attack_basic = 95
    defense_basic = 80
    spell_power_basic = 60
    spell_defense_basic = 80
    speed_basic = 30

    name = '派拉斯特'
    kind = '蘑菇'
    basic_exp_value = 142

    can_get_base_point = 3
    can_get_base_point_type = 'attack'
    capture_rate = 75
    # 精灵编号
    pet_no = '047'
    prop = ['insect','wood']