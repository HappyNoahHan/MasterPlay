from pets import propets

class Magikarp(propets.PropInit):
    health_basic = 20
    attack_basic = 10
    defense_basic = 55
    spell_power_basic = 15
    spell_defense_basic = 20
    speed_basic = 80

    name = '鲤鱼王'
    basic_exp_value = 20

    can_get_base_point = 1
    can_get_base_point_type = 'speed'
    capture_rate = 255
    canEvolve = False
    # 精灵编号
    pet_no = '129'
    prop = ['water']

    def __str__(self):
        return super().__str__() + ':' + self.name

class Tentacool(propets.PropInit):
    health_basic = 40
    attack_basic = 40
    defense_basic = 35
    spell_power_basic = 50
    spell_defense_basic = 100
    speed_basic = 70

    name = '玛瑙水母'
    kind = '水母'
    basic_exp_value = 67

    can_get_base_point = 1
    can_get_base_point_type = 'spell_defense'
    capture_rate = 190
    # 精灵编号
    pet_no = '072'
    prop = ['water','poison']

class Tentacruel(Tentacool):
    health_basic = 80
    attack_basic = 70
    defense_basic = 65
    spell_power_basic = 80
    spell_defense_basic = 120
    speed_basic = 100

    name = '毒刺水母'
    basic_exp_value = 180

    can_get_base_point = 2
    capture_rate = 60
    # 精灵编号
    pet_no = '073'


class Horsea(propets.PropInit):
    health_basic = 30
    attack_basic = 40
    defense_basic = 70
    spell_power_basic = 70
    spell_defense_basic = 25
    speed_basic = 60

    name = '墨海马'
    kind = '龙'
    basic_exp_value = 59

    can_get_base_point = 1
    can_get_base_point_type = 'spell_power'
    capture_rate = 225
    # 精灵编号
    pet_no = '116'
    prop = ['water']

class Seadra(Horsea):
    health_basic = 55
    attack_basic = 65
    defense_basic = 95
    spell_power_basic = 95
    spell_defense_basic = 45
    speed_basic = 85

    name = '海刺龙'
    basic_exp_value = 154

    can_get_base_point = 1
    can_get_base_point_type = 'spell_power'
    capture_rate = 75
    # 精灵编号
    pet_no = '117'

class Goldeen(propets.PropInit):
    health_basic = 45
    attack_basic = 67
    defense_basic = 60
    spell_power_basic = 35
    spell_defense_basic = 50
    speed_basic = 63

    name = '角金鱼'
    basic_exp_value = 111

    can_get_base_point = 1
    can_get_base_point_type = 'attack'
    capture_rate = 225
    canEvolve = False
    # 精灵编号
    pet_no = '118'
    prop = ['water']

    def __str__(self):
        return super().__str__() + ':' + self.name

class Staryu(propets.PropInit):
    health_basic = 30
    attack_basic = 45
    defense_basic = 55
    spell_power_basic = 70
    spell_defense_basic = 55
    speed_basic = 80

    name = '海星星'
    basic_exp_value = 106

    can_get_base_point = 1
    can_get_base_point_type = 'speed'
    capture_rate = 225
    canEvolve = False
    # 精灵编号
    pet_no = '120'
    prop = ['water']

    def __str__(self):
        return super().__str__() + ':' + self.name

