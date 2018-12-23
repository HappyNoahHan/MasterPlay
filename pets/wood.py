import pets.propets
import random

class aiOodish(pets.propets.Wood):
    health_basic = 45
    attack_basic = 50
    defense_basic = 55
    spell_power_basic = 75
    spell_defense_basic = 65
    speed_basic = 30

    name = '走路草'
    talent = 'TA002'
    basic_exp_value = 1000

    autoAi = True

    can_get_base_point = 2
    can_get_base_point_type = 'attack'

    capture_rate = 255


    def __str__(self):
        return super().__str__() + ':' + self.name
