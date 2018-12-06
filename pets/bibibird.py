import pets.pet
import battle.skill

class BBird(pets.pet.Pet):
    def __init__(self,name,health,attack,defense,speed):
        super().__init__(name,health,attack,defense,speed)
        self.init_skills = battle.skill.scream()

        self.skill_list = {
            '1': self.init_skills
        }

        self.property = ['wood','normal']

        self.can_learn_skills = ['A','N','F','B']

    def __str__(self):
        return print("鸟类神奇宝贝")

class WildBBird(BBird):
    autoAi = True