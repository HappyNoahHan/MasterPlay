'''
    天赋特性  --1.0    initial
             --1.1   生效时间  #战前类型 只有技能威力的提升 其他有buff 提供 或者后续版本
                              #战中类型 只有伤害增强类型
                              #战后类型 只有回复气血类型
                              #其他类型  后续nn个版本
            --2.0    与技能的配合
'''

class Talent(object):
    def __init__(self,name=None,talent_code=None,up_type=None):
        self.name = name
        self.talent_code = talent_code
        self.up_type = up_type

    def __str__(self):
        return self.name

class ProUpTalent(Talent):
    def __init__(self,match_property=None,up_cause = 0,up_number = 1.0,name=None,talent_code=None,up_type=None):
        super().__init__(name=name,talent_code=talent_code,up_type=up_type)
        self.match_property = match_property
        self.up_cause = up_cause
        self.up_number = up_number

    def checkTalent(self,power,health,max_health,skill_property):
        if (max_health / health) > self.up_cause:
            if skill_property == self.match_property:
                return round(power * self.up_number)
        return power
