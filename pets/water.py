from pets import propets

class Magikarp(propets.Water):
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

    def __str__(self):
        return super().__str__() + ':' + self.name

class Tentacool(propets.Water):
    health_basic = 40
    attack_basic = 40
    defense_basic = 35
    spell_power_basic = 50
    spell_defense_basic = 100
    speed_basic = 70

    name = '毒刺水母'
    basic_exp_value = 105

    can_get_base_point = 1
    can_get_base_point_type = 'spell_defense'
    capture_rate = 190
    canEvolve = False
    # 精灵编号
    pet_no = '072'

    def __str__(self):
        return super().__str__() + ':' + self.name

class Horsea(propets.Water):
    health_basic = 30
    attack_basic = 40
    defense_basic = 70
    spell_power_basic = 70
    spell_defense_basic = 25
    speed_basic = 60

    name = '墨海马'
    basic_exp_value = 83

    can_get_base_point = 1
    can_get_base_point_type = 'spell_power'
    capture_rate = 225
    canEvolve = False
    # 精灵编号
    pet_no = '115'

    def __str__(self):
        return super().__str__() + ':' + self.name

class Goldeen(propets.Water):
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

    def __str__(self):
        return super().__str__() + ':' + self.name

class Staryu(propets.Water):
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

    def __str__(self):
        return super().__str__() + ':' + self.name

