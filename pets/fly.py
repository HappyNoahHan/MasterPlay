import pets.propets

class Pidgey(pets.propets.Fly):
    health_basic = 40
    attack_basic = 45
    defense_basic = 40
    spell_power_basic = 35
    spell_defense_basic = 35
    speed_basic = 56

    name = '比比'
    basic_exp_value = 54

    can_get_base_point = 1
    can_get_base_point_type = 'speed'

    capture_rate = 255

    canEvolve = False

    # 精灵编号
    pet_no = '026'



    def __str__(self):
        return super().__str__() + ':' + self.name