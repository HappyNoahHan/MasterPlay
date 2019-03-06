import pets.propets
import random

class Oodish(pets.propets.PropInit):
    health_basic = 45
    attack_basic = 50
    defense_basic = 55
    spell_power_basic = 75
    spell_defense_basic = 65
    speed_basic = 30

    name = '走路草'
    kind = '杂草'
    basic_exp_value = 64

    can_get_base_point = 1
    can_get_base_point_type = 'spell_power'
    capture_rate = 255
    # 精灵编号
    pet_no = '043'
    prop = ['wood','poison']

class Gloom(Oodish):
    health_basic = 60
    attack_basic = 65
    defense_basic = 70
    spell_power_basic = 85
    spell_defense_basic = 75
    speed_basic = 40

    name = '臭臭花'
    basic_exp_value = 138

    can_get_base_point = 2
    capture_rate = 120
    # 精灵编号
    pet_no = '044'

class Vileplume(Oodish):
    health_basic = 75
    attack_basic = 80
    defense_basic = 85
    spell_power_basic = 110
    spell_defense_basic = 90
    speed_basic = 50

    name = '霸王花'
    basic_exp_value = 221

    can_get_base_point = 3
    capture_rate = 45
    # 精灵编号
    pet_no = '045'

class Bellsprout(pets.propets.PropInit):
    health_basic = 50
    attack_basic = 75
    defense_basic = 35
    spell_power_basic = 40
    spell_defense_basic = 30
    speed_basic = 40

    name = '喇叭芽'
    kind = '花'
    #talent = 'TA002'
    basic_exp_value = 60

    can_get_base_point = 1
    can_get_base_point_type = 'attack'
    capture_rate = 255
    # 精灵编号
    pet_no = '069'
    prop = [ 'wood','poison']

class Weepinbell(Bellsprout):
    health_basic = 65
    attack_basic = 90
    defense_basic = 50
    spell_power_basic = 85
    spell_defense_basic = 45
    speed_basic = 55

    name = '口呆花'
    kind = '捕蝇'
    #talent = 'TA002'
    basic_exp_value = 137

    can_get_base_point = 2
    capture_rate = 120
    # 精灵编号
    pet_no = '070'

class Victreebel(Bellsprout):
    health_basic = 80
    attack_basic = 105
    defense_basic = 65
    spell_power_basic = 100
    spell_defense_basic = 70
    speed_basic = 70

    name = '大食花'
    #talent = 'TA002'
    basic_exp_value = 221

    can_get_base_point = 3
    capture_rate = 45
    # 精灵编号
    pet_no = '071'