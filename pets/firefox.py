import pets.pet
import battle.skill

class Fire(pets.pet.Pet):
    def __init__(self, name, health, attack, defense, speed):
        super().__init__(name, health, attack, defense, speed)
        self.init_skills = battle.skill.fireBall()

        self.skill_list = {
            '1': self.init_skills
        }

        self.property = ['fire', 'normal']

        self.can_learn_skills = ['A', 'N']
    def __str__(self):
        return print("火属性神奇宝贝")

class FireFox(Fire):

    talent = 'a' #天赋 eg：火属性技能伤害+10% 后续nnn版本 做一张map 天赋技能树 各种类型

    def __str__(self):
        return print("火狐狸神奇宝贝")