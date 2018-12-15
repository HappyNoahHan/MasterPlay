'''
#skill_code 技能代号  A  火系  N 普通系 B 木系
#skill_mode 技能类型   0001 伤害技能 0002 防御临时提升 003 debuff 技能
                     0004 施加状态技能  0005 移除状态技能
                     0008 生命恢复 0009 属性亲和，同属性技能伤害加成
                     --- 2.0
                     buff 类 与 debuff 类 集合
                     buff  标记attack denfense 法强 法防 提升 统一  0002 buff类技能

                     ---2.1
                     0007  debuff 移除技能
                     0006  buff 驱散技能

                     ---2.2
                     debuff 战前结算 属性临时降低
                            战后结算 气血损失

                     ---2.3
                     buff debuff 法强 法防

                     ---2.4
                     技能命中 威力

                     ---2.5
                     技能附带附加状态已经命中的概率


ready 睡眠粉 毒buff
#pp_value    技能次数（pp值）
#index_per   buff debuff 伤害
#skill_power 技能威力
#hit_rate    命中  100 = 100% 命中
'''

from assist import  rancom
from pets import statusmap,status

class skill(object):
    def __init__(self,pp=30):
        self._pp_value_max = pp
        self.pp_value = self._pp_value_max

    skill_info = '使用技能'
    effect_turns = 1
    property = 'normal'
    hit_rate = 100

    def __str__(self):
        return self.skill_info

    def getProp(self):
        return self.property

class damageSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0001'

    spell_skill = True #特殊攻击类型 物理攻击类型

    def addStatus(self,obj):
        pass

class buffSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0002'

class debuffSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0003'

    damage_debuff = False

class statusSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0004'

class removeStatusSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0005'

class removeBuffSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0006'

    remove_num = 1

class removeDebuffSkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0007'

    remove_num = 1

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
    skill_power = 40
    property = 'fly'
    skill_info = '伤害加成20%'
    spell_skill = False

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
    skill_power = 40
    property = 'fire'
    skill_info = '使用火球术攻击，威力一般,有5%的几率使对手进入灼伤状态'
    hit_rate = 80
    addition_status_rate = 5

    def addStatus(self,obj):
        if rancom.statusRandom(self.addition_status_rate):
            if 'ST001' not in obj.status:
                obj.status.append('ST001')
                print("%s 陷入了 %s 状态！" % (obj.name,statusmap.status_dict['ST001']))

class fireSpin(debuffSkill):
    skill_show_name = '火焰漩涡'
    skill_code = 'A004'
    index_per = 0.1
    property = 'fire'
    effect_turns = 3
    skill_info = "持续性火焰伤害，每回合受到血量10%的伤害"
    damage_debuff = True

class flameAffinity(propSkill):
    skill_show_name = '火焰亲和'
    skill_code = 'A009'
    index_per = 0.5
    property = 'fire'
    skill_info = "火焰亲和觉醒,接下来的一个回合，火属性技能伤害加成50%"

class azorLeaf(damageSkill):
    skill_show_name = '飞叶快刀'
    skill_code = 'B002'
    skill_power = 55
    spell_skill = False
    property = 'wood'
    hit_rate = 95
    skill_info = "飞叶攻击，片片不占身"

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

class illuminatiom(removeDebuffSkill):
    skill_show_name = '光照'
    skill_info = "驱散一个debuff效果"
    skill_code = 'S001'
    property = 'light'

class disperse(removeBuffSkill):
    skill_info = "驱散一个对方的增益效果"
    skill_code = 'T001'
    property = 'dark'
    skill_show_name = '驱散'

class threaten(debuffSkill):
    skill_info = "恐吓对方，迫使对方攻击下降10%，持续3回合"
    effect_turns = 3
    skill_code = 'T002'
    skill_show_name = '恐吓'
    property = 'dark'
    index_per = 0.1
    debuff_prop = 'SpellDefense'

class StunSpore(statusSkill):
    skill_info = '麻痹对手，使对手有一定的几率无法成功使用技能'
    skill_code = 'C001'
    skill_show_name = '麻痹粉'
    status = status.Paralysis()
    property = 'worm'
    hit_rate = 50

class SleepingPowder(statusSkill):
    skill_info = '是对手进入睡眠，无法行动，但有一定几率清醒'
    skill_code = 'C002'
    skill_show_name = '睡眠粉'
    status = status.Sleeping()
    property = 'worm'
    hit_rate = 85

class HolyLight(removeStatusSkill):
    skill_show_name = '圣光'
    skill_info = '移除所有状态'
    skill_code = 'S002'
    property = 'light'

    def useSkill(self,obj):
        statusmap.removeStatus(obj,status_code='all')
