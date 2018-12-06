'''
#skill_code 技能代号  A  火系  N 普通系 B 木系
#skill_mode 技能类型   0001 伤害技能 0002 防御临时提升 003 debuff 行动后气血损伤 0004 力量加成技能
                     0005 法强加成  0006 法防加成
                     0007 生命回复buff技能 0008 生命恢复 0009 属性亲和，同属性技能伤害加成
                     --- 2.0
                     buff 类 与 debuff 类 集合
                     buff  标记attack denfense 法强 法防 提升 统一  0002 buff类技能
#pp_value   技能次数（pp值）
'''



class skill(object):
    def __init__(self,pp=30):
        self._pp_value_max = pp
        self.pp_value = self._pp_value_max

    skill_info = '使用技能'
    effect_turns = 1
    property = 'normal'

    def __str__(self):
        return self.skill_info

    def getProp(self):
        return self.property

class damageSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0001'

class buffSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0002'

class debuffSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0003'

class lifeRecoreSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0008'

class propSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0009'


class scream(damageSkill):
    skill_show_name = '尖叫'
    skill_code = 'N001'
    index_per = 1.2
    property = 'fly'
    skill_info = '伤害加成20%'

class steadiness(buffSkill):
    skill_show_name = '稳固'
    skill_code = 'N002'
    index_per = 0.2
    effect_turns = 3
    skill_info = "防御临时上升20%，持续3回合"
    buff_prop = 'Defense'

class strengthCre(buffSkill):
    skill_show_name = '力量增幅'
    skill_code = 'N003'
    index_per = 0.3
    effect_turns = 3
    skill_info = "力量增幅,持续3回合"
    buff_prop = 'Attack'

class fireBall(damageSkill):
    skill_show_name = '火球'
    skill_code = 'A001'
    index_per = 1.1
    property = 'fire'
    skill_info = '伤害加成10%'

class fireSpin(debuffSkill):
    skill_show_name = '火焰漩涡'
    skill_code = 'A002'
    index_per = 0.1
    property = 'fire'
    effect_turns = 3
    skill_info = "持续性火焰伤害，每回合受到血量10%的伤害"

class flameAffinity(propSkill):
    skill_show_name = '火焰亲和'
    skill_code = 'A009'
    index_per = 0.5
    property = 'fire'
    skill_info = "火焰亲和觉醒,接下来的一个回合，火属性技能伤害加成50%"

class lifeRecovery(lifeRecoreSkill):
    skill_show_name = '生命复苏'
    skill_code = 'B003'
    index_per = 0.5
    property = 'wood'
    skill_info = "恢复技能，恢复最大生命值50%"

class lifeChains(buffSkill):
    skill_show_name = '生命锁链'
    skill_code = 'B004'
    index_per = 0.1
    property = 'wood'
    effect_turns = 3
    skill_info = "生命锁链，每回合恢复最大生命值10%的生命，持续3回合"
    buff_prop = 'Health'

class vinesTied(debuffSkill):
    skill_show_name = '蔓藤捆绑'
    skill_code = 'B005'
    index_per = 0.1
    property = 'wood'
    effect_turns = 3
    skill_info = "捆绑，持续性收到10%气血的伤害"