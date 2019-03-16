import pets.propets
from battle import skill
import random

class Charmander(pets.propets.PropInit):
    health_basic = 39
    attack_basic = 52
    defense_basic = 43
    spell_power_basic = 60
    spell_defense_basic = 50
    speed_basic = 65

    name = '小火龙'
    style = '蜥蜴'
    talent = 'TA001' #天赋 eg：火属性技能伤害+10% 后续nnn版本 做一张map 天赋技能树 各种类型

    basic_exp_value = 62

    can_get_base_point = 1
    can_get_base_point_type = 'speed'

    # 精灵编号
    pet_no = '004'
    prop = ['fire']


class Charmeleon(Charmander):
    health_basic = 58
    attack_basic = 64
    defense_basic = 58
    spell_power_basic = 80
    spell_defense_basic = 65
    speed_basic = 80

    name = '火恐龙'
    kind = '火焰'
    basic_exp_value = 142

    # 精灵编号
    pet_no = '005'
    can_get_base_point_type = ['speed','spell_power']

class Charizard(Charmander):
    health_basic = 78
    attack_basic = 84
    defense_basic = 78
    spell_power_basic = 109
    spell_defense_basic = 85
    speed_basic = 100

    name = '喷火龙'
    kind = '火焰'
    basic_exp_value = 240

    # 精灵编号
    pet_no = '006'
    prop = ['fire','fly']
    can_get_base_point = 3
    can_get_base_point_type = 'spell_power'

