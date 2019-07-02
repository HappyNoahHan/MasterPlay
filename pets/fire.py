import pets.propets

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
    capture_rate = 45

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

class Vulpix(pets.propets.PropInit):
    health_basic = 48
    attack_basic = 41
    defense_basic = 40
    spell_power_basic = 50
    spell_defense_basic = 65
    speed_basic = 65

    name = '六尾'
    style = '狐狸'

    basic_exp_value = 60

    can_get_base_point = 1
    can_get_base_point_type = 'speed'
    capture_rate = 190

    # 精灵编号
    pet_no = '037'
    prop = ['fire']

class Ninetales(pets.propets.PropInit):
    health_basic = 73
    attack_basic = 76
    defense_basic = 75
    spell_power_basic = 81
    spell_defense_basic = 100
    speed_basic = 100

    name = '九尾'
    style = '狐狸'

    basic_exp_value = 177

    can_get_base_point = 1
    can_get_base_point_type = ['speed','spell_defense']
    capture_rate = 75

    # 精灵编号
    pet_no = '038'
    prop = ['fire']