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

    basic_exp_value = 51

    #技能树
    skill_tree = {
        6 : 'R001',
        12 : 'S001',
    }

    can_get_base_point = 2
    can_get_base_point_type = 'spell_power'

    # 精灵编号
    pet_no = '004'
    prop = 'fire'


class Charmeleon(Charmander):
    health_basic = 58
    attack_basic = 64
    defense_basic = 58
    spell_power_basic = 80
    spell_defense_basic = 65
    speed_basic = 80

    name = '火恐龙'
    basic_exp_value = 134

    # 精灵编号
    pet_no = '005'

    skill_tree = {
        14: 'A004',
        16: 'S001',
    }

    can_get_base_point = 3

