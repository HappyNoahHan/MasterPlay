import pets.propets

class Sandshrew(pets.propets.PropInit):
    health_basic = 50
    attack_basic = 75
    defense_basic = 85
    spell_power_basic = 20
    spell_defense_basic = 30
    speed_basic = 40

    name = '穿山鼠'
    kind = '鼠'
    basic_exp_value = 60

    can_get_base_point = 1
    can_get_base_point_type = 'defense'

    capture_rate = 255
    # 精灵编号
    pet_no = '027'
    prop = ['ground']

class Sandslash(Sandshrew):
    health_basic = 75
    attack_basic = 100
    defense_basic = 110
    spell_power_basic = 45
    spell_defense_basic = 55
    speed_basic = 65

    name = '穿山王'
    kind = '鼠'
    basic_exp_value = 158

    can_get_base_point = 2

    capture_rate = 90
    # 精灵编号
    pet_no = '028'

class Diglett(pets.propets.PropInit):
    health_basic = 10
    attack_basic = 55
    defense_basic = 25
    spell_power_basic = 35
    spell_defense_basic = 45
    speed_basic = 95

    name = '地鼠'
    kind = '鼹鼠'
    basic_exp_value = 53

    can_get_base_point = 1
    can_get_base_point_type = 'speed'

    capture_rate = 255
    # 精灵编号
    pet_no = '050'
    prop = ['ground']

class Dugtrio(pets.propets.PropInit):
    health_basic = 35
    attack_basic = 100
    defense_basic = 50
    spell_power_basic = 50
    spell_defense_basic = 70
    speed_basic = 120

    name = '三地鼠'
    kind = '鼹鼠'
    basic_exp_value = 149

    can_get_base_point = 2
    can_get_base_point_type = 'speed'

    capture_rate = 50
    # 精灵编号
    pet_no = '051'
    prop = ['ground']