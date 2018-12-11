import pets.propets

class aiOodish(pets.propets.Wood):
    health_basic = 45
    attack_basic = 50
    defense_basic = 55
    spell_power_basic = 75
    spell_defense_basic = 65
    speed_basic = 30

    def __init__(self, level):
        super().__init__(level)
        self.name = '野生走路草'
        self.talent = 'TA002'
        self.basic_exp_value = 1000

    autoAi = True


    def __str__(self):
        return super().__str__() + ':' + self.name
