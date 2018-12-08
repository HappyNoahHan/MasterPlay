import pets.propets

class FireFox(pets.propets.Fire):
    health_basic = 39
    attack_basic = 52
    defense_basic = 43
    spell_power_basic = 60
    spell_defense_basic = 50
    speed_basic = 65

    def __init__(self, level):
        super().__init__(level)
        self.name = '火狐狸'
            #talent = 'a' #天赋 eg：火属性技能伤害+10% 后续nnn版本 做一张map 天赋技能树 各种类型
        self.basic_exp_value = 51

    def __str__(self):
        return super().__str__() + ':' + self.name
