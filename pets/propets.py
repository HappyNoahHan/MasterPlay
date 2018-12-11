import pets.pet
import battle.skill

class Fire(pets.pet.Pet):
    def __init__(self, level):
        super().__init__(level)
        self.init_skills = battle.skill.fireBall()
        super().setSkills('1',self.init_skills)
        self.property = ['fire']
        self.can_learn_skills = ['A','B','N','T','S','C']
        self.info = '火系神奇宝贝'

    def __str__(self):
        return self.info

class Wood(pets.pet.Pet):
    def __init__(self, level):
        super().__init__(level)
        self.init_skills = battle.skill.scream()
        super().setSkills('1',self.init_skills)
        self.property = ['wood']
        self.can_learn_skills = ['A','B','N','T','S','C']
        self.info = '木系神奇宝贝'

    def __str__(self):
        return self.info

class Fly(pets.pet.Pet):
    def __init__(self,level):
        super().__init__(level)
        self.init_skills = battle.skill.strengthCre()
        super().setSkills('1',self.init_skills)
        self.property = ['fly']
        self.can_learn_skills = ['A','N','F','B','T','S']
        self.info = '飞行神奇宝贝'

    def __str__(self):
        return self.info