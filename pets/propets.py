import pets.pet
import battle.skill

class Fire(pets.pet.Pet):
    def __init__(self, level):
        super().__init__(level)
        self.init_skills = battle.skill.fireBall()
        super().setSkills('1',self.init_skills)
        self.property = ['fire', 'normal']
        self.can_learn_skills = ['A','B','N','T','S']
        self.info = '火系神奇宝贝'

    def __str__(self):
        return self.info

class Wood(pets.pet.Pet):
    def __init__(self, level):
        super().__init__(level)
        self.init_skills = battle.skill.lifeChains()
        super().setSkills('1',self.init_skills)
        self.property = ['wood', 'normal']
        self.can_learn_skills = ['A','B','N','T','S']
        self.info = '木系神奇宝贝'

    def __str__(self):
        return self.info

class Fly(pets.pet.Pet):
    def __init__(self,level):
        super().__init__(level)
        self.init_skills = battle.skill.strengthCre()
        super().setSkills('1',self.init_skills)
        self.property = ['fly','normal']
        self.can_learn_skills = ['A','N','F','B','T','S']
        self.info = '飞行神奇宝贝'

    def __str__(self):
        return self.info