'''
#skill_code 技能代号  A  火系  N 普通系 B 木系
#skill_mode 技能类型  0001 伤害技能 0002 防御临时提升 003 debuff 行动后气血损伤
                    0008 生命恢复 0009 属性亲和，同属性技能伤害加成
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
    property = 'normal'

    def __str__(self):
        return self.skill_info

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
    skill_model = '0002'
    effect_turns = 3
    skill_info = "防御临时上升20%，持续3回合"

class strengthCre(skill):
    skill_show_name = '力量增幅'
    skill_code = 'N003'
    index_per = 0.3
    skill_model = '0004'
    effect_turns = 3
    skill_info = "力量增幅,持续3回合"

class fireBall(skill):
    skill_show_name = '火球'
    skill_code = 'A001'
    index_per = 1.1
    property = 'fire'
    skill_model = '0001'
    skill_info = '伤害加成10%'

class fireSpin(skill):
    skill_show_name = '火焰漩涡'
    skill_code = 'A002'
    index_per = 0.1
    property = 'fire'
    skill_model = '0003'
    effect_turns = 3
    skill_info = "持续性火焰伤害，每回合受到血量10%的伤害"

class flameAffinity(skill):
    skill_show_name = '火焰亲和'
    skill_code = 'A009'
    index_per = 0.5
    property = 'fire'
    skill_model = '0009'
    skill_info = "火焰亲和觉醒,接下来的一个回合，火属性技能伤害加成50%"

class  lifeRecovery(skill):
    skill_show_name = '生命复苏'
    skill_code = 'B003'
    index_per = 0.5
    property = 'wood'
    skill_model = '0008'
    skill_info = "生命恢复，恢复技能，恢复最大生命值50%"

class vinesTied(skill):
    skill_show_name = '蔓藤捆绑'
    skill_code = 'B004'
    index_per = 0.1
    property = 'wood'
    skill_model = '0003'
    effect_turns = 3
    skill_info = "捆绑，持续性收到10%气血的伤害"