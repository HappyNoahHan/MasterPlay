'''
    天赋特性  --1.0    initial
             --1.1   生效时间
'''
from assist import life

class DamageTalent(object):
    def __init__(self):
        self.talent_type = '伤害类型'

    talent_property = 'normal'
    index_per = 1.1

    def talentEffect(self,skill,damage):
        if skill.property == self.talent_property:
            damage *= self.index_per
            print('触发猛火特性')
        return int(damage)

class RestoreTalent(object):
    def __init__(self):
        self.talent_type = '回复类型'

    talent_property = 'normal'
    index_per = 0.1

    def talentEffect(self,obj):
        life.healthRecoverByTalent(obj,self.index_per)
        print("生命回复10%")

class PropUpTalen(object):
    def __init__(self):
        self.talent_type = '属性增强类型'

    index_per = 0.1
    def talentEffect(self,value):
        return value * self.index_per



class Firaga(DamageTalent):
    talent_show_name = '猛火'
    talent_info = '火系伤害加成10%'
    talent_property = 'fire'
    index_per = 1.1
    talent_code = 'TA001'
    effect_time = ['middle']

class Growth(RestoreTalent):
    talent_show_name = '生长'
    talent_info = '战斗后回复滋生生命10%'
    talent_property = 'wood'
    index_per = 0.1
    talent_code = 'TA002'
    effect_time = ['after']

class SunShine(PropUpTalen):
    talent_show_name = '阳光'
    talent_info = '火系技能威力翻倍'
    talent_property = 'fire'
    talent_code = 'TA003'
    effect_time = ['before']
    effect_prop = 'skill_power'
    index_per = 2