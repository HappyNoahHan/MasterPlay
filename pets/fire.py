import pets.propets
from battle import skill

class Charmander(pets.propets.Fire):
    health_basic = 39
    attack_basic = 52
    defense_basic = 43
    spell_power_basic = 60
    spell_defense_basic = 50
    speed_basic = 65

    def __init__(self, level):
        super().__init__(level)
        self.name = '小火龙'
            #talent = 'a' #天赋 eg：火属性技能伤害+10% 后续nnn版本 做一张map 天赋技能树 各种类型
        self.basic_exp_value = 51

    def __str__(self):
        return super().__str__() + ':' + self.name

    evolve_level = 8

    #技能树
    skill_tree = {
        8 : 'A004',
        9 : 'S001',
    }

class Charmeleon(Charmander):
    health_basic = 58
    attack_basic = 64
    defense_basic = 58
    spell_power_basic = 80
    spell_defense_basic = 65
    speed_basic = 80

    def __init__(self, level):
        super().__init__(level)
        self.name = '火恐龙'
            #talent = 'a' #天赋 eg：火属性技能伤害+10% 后续nnn版本 做一张map 天赋技能树 各种类型
        self.basic_exp_value = 134

    evolve_level = 32

    skill_tree = {
        13: 'A004',
        16: 'S001',
    }
