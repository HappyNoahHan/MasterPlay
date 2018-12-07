import pets.propets

class aiPidgey(pets.propets.Fly):
    name = '野生比比'
    autoAi = True
    basic_exp_value = 20
    level = 4

    def __str__(self):
        return super().__str__() + ':' + self.name
