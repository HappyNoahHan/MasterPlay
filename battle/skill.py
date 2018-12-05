'''
#skill_code 技能代号  A  火系  N 普通系
#skill_mode 技能类型  0001 伤害加成 0002 防御临时提升 003 debuff 行动后气血损伤
#pp_value   技能次数（pp值）
'''



class skill(object):
    def __init__(self,pp=30):
        self._pp_value_max = pp
        self.pp_value = self._pp_value_max

    skill_show_name = '普攻'
    skill_code = '0000'
    skill_model = '0000'
    index_per = 0.0
    effect_turns = 1
    skill_info = '使用技能'

    def __str__(self):
        return self.skill_info


class fireBall(skill):
    skill_show_name = '火球'
    skill_code = 'A001'
    index_per = 1.5
    property = 'fire'
    skill_model = '0001'
    skill_info = '伤害加成50%'


class scream(skill):
    skill_show_name = '尖叫'
    skill_code = 'N001'
    index_per = 1.2
    property = 'bird'
    skill_model = '0001'
    skill_info = '伤害加成20%'

class steadiness(skill):
    skill_show_name = '稳固'
    skill_code = 'N002'
    index_per = 0.2
    property = 'normal'
    skill_model = '0002'
    effect_turns = 3
    skill_info = "防御临时上升20%，持续3回合"

class fireSpin(skill):
    skill_show_name = '火焰漩涡'
    skill_code = 'A002'
    index_per = 0.1
    property = 'fire'
    skill_model = '0003'
    effect_turns = 3
    skill_info = "持续性火焰伤害，每回合受到血量10%的伤害"

class vinesTied(skill):
    skill_show_name = '蔓藤捆绑'
    skill_code = 'B004'
    index_per = 0.1
    property = 'wood'
    skill_model = '0003'
    effect_turns = 3
    skill_info = "捆绑，持续性收到10%气血的伤害"