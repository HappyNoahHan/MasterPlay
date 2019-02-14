from pets import propets

class Geodude(propets.Rock):
    health_basic = 40
    attack_basic = 80
    defense_basic = 100
    spell_power_basic = 30
    spell_defense_basic = 30
    speed_basic = 20

    name = '小拳石'
    #talent = 'TA002'
    basic_exp_value = 60

    can_get_base_point = 1
    can_get_base_point_type = 'defense'
    capture_rate = 255
    # 精灵编号
    pet_no = '074'


    def __str__(self):
        return super().__str__() + ':' + self.name

class Onix(propets.Rock):
    health_basic = 35
    attack_basic = 40
    defense_basic = 160
    spell_power_basic = 30
    spell_defense_basic = 45
    speed_basic = 70

    name = '大岩蛇'
    #talent = 'TA002'
    basic_exp_value = 77

    can_get_base_point = 1
    can_get_base_point_type = 'defense'
    capture_rate = 45
    # 精灵编号
    pet_no = '095'


    def __str__(self):
        return super().__str__() + ':' + self.name