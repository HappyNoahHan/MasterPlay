import pets.propets

class aiOodish(pets.propets.Wood):
    name = '野生走路草'
    autoAi = True

    def __str__(self):
        return super().__str__() + ':' + self.name
