import pets.propets

class aiPidgey(pets.propets.Fly):
    health_basic = 40
    attack_basic = 45
    defense_basic = 40
    spell_power_basic = 35
    spell_defense_basic = 35
    speed_basic = 56
    name = '野生比比'
    autoAi = True
    basic_exp_value = 54
    level = 4

    def __str__(self):
        return super().__str__() + ':' + self.name
