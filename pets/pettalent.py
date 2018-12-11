'''
    天赋特性
'''

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
    index_per = 1.1


class Firaga(DamageTalent):
    talent_show_name = '猛火'
    talent_info = '火系伤害加成10%'
    talent_property = 'fire'
    index_per = 1.1
    talent_code = 'TA001'

class Growth(RestoreTalent):
    talent_show_name = '生长'
    talent_info = '每回合回复生命10%'
    talent_property = 'wood'
    index_per = 1.1
    talent_code = 'TA002'