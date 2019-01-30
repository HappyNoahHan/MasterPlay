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