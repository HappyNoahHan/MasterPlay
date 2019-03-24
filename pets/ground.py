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