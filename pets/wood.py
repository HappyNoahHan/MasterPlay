import pets.propets
import random

class Oodish(pets.propets.Wood):
    health_basic = 45
    attack_basic = 50
    defense_basic = 55
    spell_power_basic = 75
    spell_defense_basic = 65
    speed_basic = 30

    name = '走路草'
    talent = 'TA002'
    basic_exp_value = 1000

    can_get_base_point = 2
    can_get_base_point_type = 'attack'
    capture_rate = 255
    # 精灵编号
    pet_no = '043'


    def __str__(self):
        return super().__str__() + ':' + self.name

class Bellsprout(pets.propets.Wood):
    health_basic = 50
    attack_basic = 75
    defense_basic = 35
    spell_power_basic = 40
    spell_defense_basic = 30
    speed_basic = 40

    name = '喇叭芽'
    #talent = 'TA002'
    basic_exp_value = 84

    can_get_base_point = 1
    can_get_base_point_type = 'attack'
    capture_rate = 255
    # 精灵编号
    pet_no = '069'


    def __str__(self):
        return super().__str__() + ':' + self.name
