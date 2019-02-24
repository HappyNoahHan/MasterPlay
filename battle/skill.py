'''
#skill_code 技能代号  A  火系  N 普通系 B 木系 C 虫系 D 水系 S 超能=光 I 冰 T 恶=黑暗 E 地面 F 飞行 G 龙  R 岩石 P 毒 Q鬼魂
#skill_mode 技能类型   0001 伤害技能 0002 防御临时提升 003 debuff 技能
                     0004 施加状态技能  0005 移除状态技能
                     0008 生命恢复 0009 属性亲和，同属性技能伤害加成
                     0010 伤害并恢复生命
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
from pets import statusmap,talentmap

class skill(object):
    def __init__(self,pp=30):
        self._pp_value_max = pp
        self.pp_value = self._pp_value_max

    skill_info = '使用技能'
    effect_turns = 1
    property = 'normal'
    hit_rate = 100
    skill_power = None


    def __str__(self):
        return self.skill_info + ' || Power: ' + str(self.skill_power)

    def getProp(self):
        return self.property

class damageSkill(skill):
    def __init__(self,pp=30,hit_status=None,addition_status = None,addition_status_rate = 100,spell_skill=True,lucky_level=1):
        '''
        :param pp: pp value
        :param hit_status: 附加状态
        :param addition_status: 状态威力加强
        :param addition_status_rate: 状态几率
        :param spell_skill: 技能类型 物理or特殊
        :param lucky_level: 会心等级 默认=1
        '''
        super().__init__(pp)
        self.skill_model = '0001'
        self.hit_status = hit_status #技能附加状态
        self.addition_status = addition_status #技能检查伤害加成状态
        self.addition_status_rate = addition_status_rate
        self.spell_skill = spell_skill #特殊攻击类型 True 默认 物理攻击类型 False
        self.lucky_level = lucky_level

    def addStatus(self,obj):
        if self.hit_status != None:
            if rancom.statusRandom(self.addition_status_rate):
                if self.hit_status not in obj.status:
                    # 检查特性与obj 属性 某些pet不会中某技能
                    if talentmap.addStatusOrNot(obj,self.hit_status):
                        obj.setStatus(self.hit_status)
                        print("%s 陷入了 %s 状态！" % (obj.name,statusmap.status_dict[self.hit_status].status_show_name))
                    else:
                        print("%s 免疫 %s 状态" % (obj.name,statusmap.status_dict[self.hit_status].status_show_name))

    def doublePowerOrNot(self,obj):
        if self.addition_status != None:
            #ST999 弱点攻击
            if self.addition_status in obj.status:
                #print("%s 受到了双倍伤害" % obj.name)
                return True
        return False

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
    def __init__(self,pp=30,status=None):
        super().__init__(pp)
        self.skill_model = '0004'
        self.status = status

    def addStatus(self,obj):
        if talentmap.addStatusOrNot(obj,self.status):
            obj.setStatus(self.status)
            print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
        else:
            print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))

class removeStatusSkill(skill):
    def __init__(self,pp=30,effecters='both',status=None):
        super().__init__(pp)
        self.skill_model = '0005'
        self.effecters = effecters
        self.status = status

    def useSkill(self,obj_attack,obj_defense):
        if self.effecters == 'attack':
            statusmap.removeStatus(obj_attack, status_code=self.status)
        elif self.effecters == 'defense':
            statusmap.removeStatus(obj_defense,status_code=self.status)
        else:
            statusmap.removeStatus(obj_attack, status_code=self.status)
            statusmap.removeStatus(obj_defense, status_code=self.status)

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

class suckBloodSkill(skill):
    def __init__(self,pp=15,spell_skill=True,suck_per = 0.5,lucky_level = 1):
        super().__init__(pp)
        self.skill_model = '0010'
        self.spell_skill = spell_skill
        self.suck_per = suck_per
        self.lucky_level = lucky_level

    def doublePowerOrNot(self,obj):
        return False


class StartWind(damageSkill):
    def __init__(self):
        super().__init__(35,spell_skill=False)
    show_name = '起风'
    skill_code = 'F001'
    skill_power = 40
    property = 'fly'
    skill_info = '用翅膀刮起风攻击对方'

class WingAttack(StartWind):
    show_name = '翅膀攻击'
    skill_code = 'F002'
    skill_power = 60
    skill_info = '用翅膀攻击对方'

class AirCut(damageSkill):
    def __init__(self):
        super().__init__(15)
    show_name = '空气斩'
    skill_code = 'F003'
    property = 'fly'
    skill_power = 75
    hit_rate = 95
    skill_info = "将空气压缩成刀再攻击对面,威力强大"

class AirSword(damageSkill):
    def __init__(self):
        super().__init__(25,lucky_level=99)
    show_name = '空气利刃'
    skill_code = 'F004'
    property = 'fly'
    skill_power = 60
    hit_rate = 95
    skill_info = "用锐利的风切攻击,更容易会心一击~"

class Strike(damageSkill):
    def __init__(self):
        super().__init__(pp=35,spell_skill=False)
    show_name = '撞击'
    skill_code = 'N001'
    skill_power = 40
    skill_info = '用身体撞击对方'

class Grab(damageSkill):
    def __init__(self):
        super().__init__(pp=35,spell_skill=False)
    show_name = '抓'
    skill_code = 'N002'
    skill_power = 40
    skill_info = '用爪子攻击对方'

class Supersonic(statusSkill):
    def __init__(self):
        super().__init__(20,status = 'ST002')
    skill_info = '使对方混乱，一定的几率无法成功使用技能'
    skill_code = 'N003'
    show_name = '超音波'
    hit_rate = 55

class HighSpeedStar(damageSkill):
    def __init__(self):
        super().__init__(pp=20)
    skill_info = "发射星星光线,攻击必定命中"
    skill_code = 'N004'
    show_name = '高速星星'
    skill_power = 60

class BlackEye(statusSkill):
    def __init__(self):
        super().__init__(pp=5,status = 'ST099')
    skill_info = '用目光紧紧盯住对方,使其无法逃脱'
    skill_code = 'N005'
    show_name = '黑色目光'


class steadiness(buffSkill):
    show_name = '稳固'
    skill_code = 'N099'
    index_per = 0.2
    effect_turns = 3
    skill_info = "防御临时上升20%，持续3回合"
    buff_prop = 'Defense'

class strengthCre(buffSkill):
    show_name = '力量增幅'
    skill_code = 'N100'
    index_per = 0.3
    effect_turns = 3
    skill_info = "力量增幅,持续3回合"
    buff_prop = 'Attack'

class fireBall(damageSkill):
    def __init__(self,pp=25):
        super().__init__(pp,hit_status='ST001')
    show_name = '火球'
    skill_code = 'A001'
    skill_power = 40
    property = 'fire'
    skill_info = '使用火球术攻击，威力一般,有5%的几率使对手进入灼伤状态'
    hit_rate = 80

class JetFlame(fireBall):
    def __init__(self):
        super().__init__(pp=15)
    show_name = '喷射火焰'
    skill_code = 'A005'
    skill_power = 90
    skill_info = '火焰喷射，威力超绝,有5%的几率使对手进入灼伤状态'
    hit_rate = 100

class fireSpin(debuffSkill):
    def __init__(self,pp=15):
        super().__init__(pp)
    show_name = '火焰漩涡'
    skill_code = 'A004'
    index_per = 0.1
    property = 'fire'
    effect_turns = 3
    skill_info = "持续性火焰伤害，每回合受到血量10%的伤害"
    damage_debuff = True

class flameAffinity(propSkill):
    def __init__(self,pp=10):
        super().__init__(pp)
    show_name = '火焰亲和'
    skill_code = 'A009'
    index_per = 0.5
    property = 'fire'
    skill_info = "火焰亲和觉醒,接下来的一个回合，火属性技能伤害加成50%"

class azorLeaf(damageSkill):
    def __init__(self):
        super().__init__(lucky_level=2)
    show_name = '飞叶快刀'
    skill_code = 'B002'
    skill_power = 55
    spell_skill = False
    property = 'wood'
    hit_rate = 95
    skill_info = "飞叶攻击，片片不占身"

class lifeRecovery(lifeRecoreSkill):
    def __init__(self,pp=15):
        super().__init__(pp)
    show_name = '生命复苏'
    skill_code = 'B003'
    index_per = 0.5
    property = 'wood'
    skill_info = "恢复技能，恢复最大生命值50%"

class lifeChains(buffSkill):
    def __init__(self,pp=15):
        super().__init__(pp)
    show_name = '生命锁链'
    skill_code = 'B004'
    index_per = 0.1
    property = 'wood'
    effect_turns = 3
    skill_info = "生命锁链，每回合恢复最大生命值10%的生命，持续3回合"
    buff_prop = 'Health'

class vinesTied(debuffSkill):
    show_name = '蔓藤捆绑'
    skill_code = 'B005'
    index_per = 0.1
    property = 'wood'
    effect_turns = 3
    skill_info = "捆绑，持续性收到10%气血的伤害"

class Assimilate(suckBloodSkill):
    def __init__(self,pp=15):
        super().__init__(pp)

    show_name = '吸取'
    skill_code = 'B006'
    property = 'wood'
    skill_info = "吸取对方回复自己的生命"
    skill_power = 40

class illuminatiom(removeDebuffSkill):
    def __init__(self,pp=20):
        super().__init__(pp)
    show_name = '光照'
    skill_info = "驱散一个debuff效果"
    skill_code = 'S001'
    property = 'light'

class disperse(removeBuffSkill):
    def __init__(self,pp=20):
        super().__init__(pp)
    skill_info = "驱散一个对方的增益效果"
    skill_code = 'T001'
    property = 'dark'
    show_name = '驱散'

class threaten(debuffSkill):
    skill_info = "恐吓对方，迫使对方攻击下降10%，持续3回合"
    effect_turns = 3
    skill_code = 'T002'
    show_name = '恐吓'
    property = 'dark'
    index_per = 0.1
    debuff_prop = 'SpellDefense'

class Bite(damageSkill):
    def __init__(self):
        super().__init__(pp=25,hit_status='ST004',spell_skill=False)

    skill_info = "咬住对方,有一定的几率使对面畏缩"
    skill_code = 'T003'
    show_name = '咬住'
    property = 'dark'
    skill_power = 60

class StunSpore(statusSkill):
    def __init__(self):
        super().__init__(status = 'ST002')
    skill_info = '麻痹对手，使对手有一定的几率无法成功使用技能'
    skill_code = 'C001'
    show_name = '麻痹粉'
    property = 'insect'
    hit_rate = 50

class SleepingPowder(statusSkill):
    def __init__(self):
        super().__init__(status = 'ST003')
    skill_info = '使对手进入睡眠，无法行动，但有一定几率清醒'
    skill_code = 'C002'
    show_name = '睡眠粉'
    property = 'insect'
    hit_rate = 85

class StukBlood(suckBloodSkill):
    def __init__(self,pp=20):
        super().__init__(pp,spell_skill=False)
    skill_code = 'C003'
    show_name = '吸血'
    skill_power = 80
    skill_info = "吸取对方,回复生命"
    property = 'insect'

class BlackFog(removeStatusSkill):
    def __init__(self):
        super().__init__(status='all')
    show_name = '黑雾'
    skill_info = '移除所有状态'
    skill_code = 'I001'
    property = 'ice'

class WaterJump(buffSkill):
    show_name = '水溅跃'
    skill_code = 'D001'
    index_per = 0.1
    effect_turns = 2
    skill_info = "防御临时上升10%，持续2回合"
    buff_prop = 'Defense'

class WaterBall(damageSkill):
    show_name = '水球'
    skill_code = 'D002'
    skill_power = 40
    property = 'water'
    skill_info = '使用水球术攻击，威力一般'
    hit_rate = 100

class WaterCannon(damageSkill):
    show_name = '水炮'
    skill_code = 'D003'
    skill_power = 80
    property = 'water'
    skill_info = '使用水炮术攻击，威力不一般'
    hit_rate = 95

class DownRock(damageSkill):
    def __init__(self,pp=35):
        super().__init__(pp,spell_skill=False)

    show_name = '落岩'
    skill_code = 'R001'
    skill_power = 40
    property = 'rock'
    skill_info = '使用落岩攻击，威力一般'


class RockFall(damageSkill):
    def __init__(self):
        super().__init__(10,hit_status='ST004',addition_status_rate=5,spell_skill=False)

    show_name = '岩崩'
    skill_code = 'R002'
    skill_power = 75
    property = 'rock'
    skill_info = '将大岩石撞向对面,有一定的几率会使对方畏惧'
    hit_rate = 90

class Earthquake(damageSkill):
    def __init__(self):
        super().__init__(10,spell_skill=False)

    show_name = '地震'
    skill_code = 'E001'
    skill_power = 100
    property = 'ground'
    skill_info = '引发地震攻击对面,威力超绝'

class SingularLight(statusSkill):
    def __init__(self):
        super().__init__(20,status = 'ST002')
    skill_code = 'Q001'
    show_name = '奇异之光'
    property = 'ghost'
    skill_info = '显示奇怪的光,使对面混乱'

class Scare(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST004',spell_skill=False)

    skill_info = "惊吓,有一定的几率使对面畏缩"
    skill_code = 'Q002'
    show_name = '惊吓'
    property = 'ghost'
    skill_power = 30

class Toxic(statusSkill):
    def __init__(self):
        super().__init__(10,status = 'ST005')
    skill_code = 'P001'
    show_name = '剧毒'
    property = 'poison'
    skill_info = "释放剧毒,使对方中毒"
    hit_rate = 90

class ToxicFang(damageSkill):
    def __init__(self):
        super().__init__(hit_status='ST005',pp=15,spell_skill=False)
    skill_info = "使用有毒的牙齿攻击,有几率使对面中毒"
    show_name = '剧毒牙'
    property = 'poison'
    skill_power = 50
    skill_code = 'P002'

class VenomImpact(damageSkill):
    def __init__(self):
        super().__init__(pp=10,addition_status='ST005')

    show_name = '毒液冲击'
    property = 'poison'
    skill_power = 65
    skill_info = '用特殊的毒液攻击,目标在中毒状态下威力加倍'
    skill_code = 'P003'
