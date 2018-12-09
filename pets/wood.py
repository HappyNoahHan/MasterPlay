import pets.propets

class aiOodish(pets.propets.Wood):
    health_basic = 45
    attack_basic = 50
    defense_basic = 55
    spell_power_basic = 75
    spell_defense_basic = 65
    speed_basic = 30

    name = '野生走路草'
    autoAi = True
   #basic_exp_value = 56
    basic_exp_value = 10000
    level = 3

    def __str__(self):
        return super().__str__() + ':' + self.name
