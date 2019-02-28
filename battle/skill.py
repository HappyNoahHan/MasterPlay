'''
#skill_code 技能代号  A  火系  N 普通系 B 木系 C 虫系 D 水系 S 超能=光 I 冰 T 恶=黑暗 E 地面 F 飞行 G 龙
                     R 岩石 P 毒 Q鬼魂 H 电
#skill_mode 技能类型   0001 伤害技能 0002 防御临时提升 003 debuff 技能
                     0004 施加状态技能  0005 移除状态技能
                     0008 生命恢复 0009 属性亲和，同属性技能伤害加成
                     0010 伤害并恢复生命
                     0011 印记类技能 和印记多少有关 印记以状态显示
                     0012 增益状态技能
                     0013 特殊状态技能 eg.吹飞
                     0014 复制类技能
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
    use_condition = None  #使用条件



    def __str__(self):
        return self.skill_info + ' || Power: ' + str(self.skill_power)

    def getProp(self):
        return self.property

class damageSkill(skill):
    def __init__(self,pp=30,hit_status=None,addition_status = None,
                 addition_status_rate = 5,spell_skill=True,lucky_level=1,
                 turns=1):
        '''
        :param pp: pp value
        :param hit_status: 附加状态
        :param addition_status: 状态威力加强
        :param addition_status_rate: 状态几率
        :param spell_skill: 技能类型 物理or特殊
        :param lucky_level: 会心等级 默认=1
        :param truns: status层数
        '''
        super().__init__(pp)
        self.skill_model = '0001'
        self.hit_status = hit_status #技能附加状态
        self.addition_status = addition_status #技能检查伤害加成状态
        self.addition_status_rate = addition_status_rate
        self.spell_skill = spell_skill #特殊攻击类型 True 默认 物理攻击类型 False
        self.lucky_level = lucky_level
        self.turns = turns


    def addStatus(self,obj):
        if self.hit_status != None:
            if rancom.statusRandom(self.addition_status_rate):
                if self.hit_status not in obj.status:
                    # 检查特性与obj 属性 某些pet不会中某技能
                    if talentmap.addStatusOrNot(obj,self.hit_status):
                        obj.setStatus(self.hit_status,self.turns)
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

class MultipleDamageSkill(damageSkill):
    def addStatus(self,obj):
        if self.hit_status != None:
            for status in self.hit_status:
                if rancom.statusRandom(self.addition_status_rate):
                    if status not in obj.status:
                        # 检查特性与obj 属性 某些pet不会中某技能
                        if talentmap.addStatusOrNot(obj,status):
                            obj.setStatus(status,self.turns)
                            print("%s 陷入了 %s 状态！" % (obj.name,statusmap.status_dict[status].status_show_name))
                        else:
                            print("%s 免疫 %s 状态" % (obj.name,statusmap.status_dict[status].status_show_name))

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
    def __init__(self,pp=30,status=None,turns = 1):
        super().__init__(pp)
        self.skill_model = '0004'
        self.status = status
        self.turns = turns

    def addStatus(self,obj):
        if self.status not in obj.status:
            if talentmap.addStatusOrNot(obj,self.status):
                obj.setStatus(self.status,self.turns)
                print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
            else:
                print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
        else:
            print("%s 已经陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))

class GainStatusUpSkill(skill):
    '''
    多重加增益状态技能
    '''

    def __init__(self, pp=30, status=None, turns=1):
        super().__init__(pp)
        self.skill_model = '0012'
        self.status = status
        self.turns = turns

    def addStatus(self,obj):
        for status in self.status:
            if status not in obj.status:
                if talentmap.addStatusOrNot(obj, status):
                    obj.setStatus(status,self.turns)
                    print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
                else:
                    print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
            else:
                print("%s 已经陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))


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

class ImprintSkill(skill):
    def __init__(self,pp=30,lucky_level= 1,status=None,imprint_level = 1,imprint_type = None,spell_skill = None):
        '''
        印记技能
        :param pp:
        :param lucky_level:
        :param status:
        :param imprint_level: 印记收集 1 还是使用 2
        :param imprint_type: 使用模式 输出 治疗
        :param spell_skill: 技能类型 None 变化 True 特殊 False 物理
        '''
        super().__init__(pp)
        self.skill_model = '0011'
        self.lucky_level = lucky_level
        self.status = status
        #self.turns = turns
        self.imprint_level = imprint_level
        self.imprint_type = imprint_type
        self.spell_skill = spell_skill

    def addStatus(self,obj):
        if self.status in obj.status:
            obj.status[self.status] += 1
            if obj.status[self.status] > 3:
                obj.status[self.status] = 3
            print("%s %s 状态 %s 层" % (obj.name, statusmap.status_dict[self.status].status_show_name,obj.status[self.status]))
        else:
            obj.setStatus(self.status)
            print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))

    def doublePowerOrNot(self,obj):
        return False

class SpecialStatusSkill(skill):
    def __init__(self,pp=30,status=None,turns =1 ):
        super().__init__(pp)
        self.skill_model = '0013'
        self.status = status
        self.turns = turns

    def addStatus(self,obj_attack,obj_defense):
        if obj_attack.level >= obj_defense.level:
            if obj_defense.has_trainer == False:
                obj_defense.setStatus(self.status)
                print("%s 陷入 %s 状态 ！" % (obj_defense.name, statusmap.status_dict[self.status].status_show_name))
                return True
        return False

class CopySkill(skill):
    def __init__(self,pp=30):
        super().__init__(pp)
        self.skill_model = '0014'

    def useOrNot(self,obj):
        if obj.last_used_skill != None:
            if obj.last_used_skill.skill_model != '0014':
                return obj.last_used_skill
        return None


class Gust(damageSkill):
    def __init__(self):
        super().__init__(35,spell_skill=False)
    show_name = '起风'
    skill_code = 'F001'
    skill_power = 40
    property = 'fly'
    skill_info = '用翅膀刮起风攻击对方'

class WingAttack(Gust):
    show_name = '翅膀攻击'
    skill_code = 'F002'
    skill_power = 60
    skill_info = '用翅膀攻击对方'

class AirSlash(damageSkill):
    def __init__(self):
        super().__init__(15,hit_status='ST004',addition_status_rate=30)
    show_name = '空气斩'
    skill_code = 'F003'
    property = 'fly'
    skill_power = 75
    hit_rate = 95
    skill_info = "攻击目标造成伤害,有30%的几率使目标陷入畏缩状态"

class AirCutter(damageSkill):
    def __init__(self):
        super().__init__(25,lucky_level=2)
    show_name = '空气利刃'
    skill_code = 'F004'
    property = 'fly'
    skill_power = 60
    hit_rate = 95
    skill_info = "用锐利的风切攻击,更容易会心一击~"

class FeatherDance(statusSkill):
    def __init__(self):
        super().__init__(pp=15,status='ST021',turns=2)

    show_name = '羽毛舞'
    skill_info = '令目标的攻击降低2级'
    property = 'fly'
    skill_code = 'F005'

class Roost(lifeRecoreSkill):
    def __init__(self,pp=10):
        super().__init__(pp)
    show_name = '羽栖'
    skill_code = 'F006'
    index_per = 0.5
    property = 'fly'
    skill_info = "恢复使用者的1⁄2的ＨＰ值"

class Tailwind(buffSkill):
    def __init__(self):
        super().__init__(15)
    show_name = '顺风'
    skill_code = 'F007'
    index_per = 1
    effect_turns = 4
    skill_info = "己方场地上全部的宝可梦的速度加倍。持续时间为4回合，包括使用的当回合"
    buff_prop = 'Speed'
    property = 'fly'

class MirrorMove(CopySkill):
    def __init__(self):
        super().__init__(pp=20)

    show_name = '鹦鹉学舌'
    skill_code = 'F008'
    hit_rate = 0
    property = 'fly'
    skill_info = '使用目标最后使用过的招式'

class Tackle(damageSkill):
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

class Swift(damageSkill):
    def __init__(self):
        super().__init__(pp=20)
    skill_info = "发射星星光线,攻击必定命中"
    skill_code = 'N004'
    show_name = '高速星星'
    skill_power = 60
    hit_rate = 0

class MeanLook(statusSkill):
    def __init__(self):
        super().__init__(pp=5,status = 'ST099')
    skill_info = '用目光紧紧盯住对方,使其无法逃脱'
    skill_code = 'N005'
    show_name = '黑色目光'
    hit_rate = 0

class Screech(statusSkill):
    def __init__(self):
        super().__init__(40,status='ST009',turns=2)
    skill_info = "令目标的防御降低2级"
    skill_code = 'N006'
    show_name = '刺耳声'
    hit_rate = 85

class Wrap(damageSkill):
    def __init__(self):
        super().__init__(20,hit_status='ST010',addition_status_rate=100,spell_skill=False)
    skill_info = '攻击目标造成伤害。使目标陷入束缚状态'
    skill_code = 'N007'
    show_name = '紧束'
    skill_power = 15
    hit_rate = 90

class Leer(statusSkill):
    def __init__(self):
        super().__init__(status='ST009')
    skill_info = '令目标的防御降低1级'
    skill_code = 'N008'
    show_name = '瞪眼'

class Glare(statusSkill):
    def __init__(self):
        super().__init__(status='ST002')
    skill_info = '使目标陷入麻痹状态'
    skill_code = 'N009'
    show_name = '大蛇瞪眼'

class Stockpile(ImprintSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST012')

    skill_info = '陷入蓄力状态,在蓄力的时候，防御和特防会提高'
    skill_code = 'N010'
    show_name = '蓄力'
    hit_rate = 0

class Swallow(ImprintSkill):
    def __init__(self):
        super().__init__(pp=10,imprint_level=2,imprint_type='restore',status='ST012')
    skill_info = '将储存的力量吞入,恢复HP'
    skill_code = 'N011'
    show_name = '吞下'
    hit_rate = 0

class SpitUp(ImprintSkill):
    def __init__(self):
        super().__init__(pp=10,imprint_level=2,imprint_type='damage',status='ST012',lucky_level=2,spell_skill=True)
    skill_info = '将储存的力量喷出,造成伤害,威力为次数×100'
    skill_code = 'N012'
    show_name = '喷出'
    hit_rate = 0

class QuickAttack(damageSkill):
    def __init__(self):
        super().__init__(spell_skill=False)
    skill_info = '攻击目标造成伤害'
    show_name = '电光一闪'
    skill_code = 'N013'
    skill_power = 40

class Whirlwind(SpecialStatusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST101')
    show_name = '吹飞'
    skill_code = 'N014'
    hit_rate = 0
    skill_info = '吹飞对手'

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

class FireFang(MultipleDamageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status=['ST001','ST004'],addition_status_rate=10,spell_skill=False)
    show_name = '火焰牙'
    skill_code = 'A002'
    property = 'fire'
    hit_rate = 95
    skill_power = 65
    skill_info = '攻击目标造成伤害,有10%的几率使目标陷入灼伤/畏缩状态'

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

class Absorb(suckBloodSkill):
    def __init__(self,pp=15):
        super().__init__(pp)

    show_name = '吸取'
    skill_code = 'B006'
    property = 'wood'
    skill_info = "攻击目标造成伤害，自身的ＨＰ恢复“造成的伤害×50%"
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
        super().__init__(pp=25,hit_status='ST004',spell_skill=False,addition_status_rate=30)

    skill_info = "攻击目标造成伤害,有30%的几率使目标陷入畏缩状态"
    skill_code = 'T003'
    show_name = '咬住'
    property = 'dark'
    skill_power = 60

class Crunch(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST009',spell_skill=False,addition_status_rate=20)
    skill_info = "攻击目标造成伤害20%几率令目标的防御降低1级"
    skill_code = 'T004',
    show_name = '咬碎'
    property = 'dark'
    skill_power = 80

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

class LeechLife(suckBloodSkill):
    def __init__(self,pp=20):
        super().__init__(pp,spell_skill=False)
    skill_code = 'C003'
    show_name = '吸血'
    skill_power = 80
    skill_info = "吸取对方,回复生命"
    property = 'insect'

class Haze(removeStatusSkill):
    def __init__(self):
        super().__init__(status='all')
    show_name = '黑雾'
    skill_info = '移除所有状态'
    skill_code = 'I001'
    property = 'ice'
    hit_rate = 0

class IceFang(MultipleDamageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status=['ST004','ST008'],addition_status_rate=10,spell_skill=False)
    show_name = '冰冻牙'
    skill_code = 'I002'
    property = 'ice'
    hit_rate = 95
    skill_power = 65
    skill_info = '攻击目标造成伤害,有10%的几率使目标陷入冰冻/畏缩状态'

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

class MudBomb(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status='ST013',addition_status_rate=30)
    show_name = '泥巴炸弹'
    skill_code = 'E002'
    skill_power = 65
    property = 'ground'
    skill_info = '攻击目标造成伤害,30%几率令目标的命中率降低1级'
    hit_rate = 85

class SandAttack(statusSkill):
    def __init__(self):
        super().__init__(pp=15,status='ST013')
    show_name = '泼沙'
    skill_code = 'E003'
    skill_info = '令目标的命中率降低1级'
    property = 'ground'

class ConfuseRay(statusSkill):
    def __init__(self):
        super().__init__(20,status = 'ST002')
    skill_code = 'Q001'
    show_name = '奇异之光'
    property = 'ghost'
    skill_info = '显示奇怪的光,使对面混乱'

class Astonish(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST004',spell_skill=False,addition_status_rate=30)

    skill_info = "惊吓,有30%几率使对面畏缩"
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

class PoisonFang(damageSkill):
    def __init__(self):
        super().__init__(hit_status='ST005',pp=15,spell_skill=False,addition_status_rate=50)
    skill_info = "使用有毒的牙齿攻击,有50几率使对面中毒"
    show_name = '剧毒牙'
    property = 'poison'
    skill_power = 50
    skill_code = 'P002'

class Venoshock(damageSkill):
    def __init__(self):
        super().__init__(pp=10,addition_status='ST005')

    show_name = '毒液冲击'
    property = 'poison'
    skill_power = 65
    skill_info = '用特殊的毒液攻击,目标在中毒状态下威力加倍'
    skill_code = 'P003'

class PoisonSting(damageSkill):
    def __init__(self):
        super().__init__(pp=35,addition_status_rate=30,spell_skill=False,hit_status='ST007')

    show_name = '毒针'
    property = 'poison'
    skill_power = 15
    skill_code = 'P004'
    skill_info = '攻击目标造成伤害,有30%的几率使目标陷入中毒状态'

class Acid(damageSkill):
    def __init__(self):
        super().__init__(hit_status='ST011',addition_status_rate=10)

    show_name = '溶解液'
    property = 'poison'
    skill_power = 40
    skill_code = 'P005'
    skill_info = '攻击目标造成伤害,10%几率令目标的特防降低1级'

class AcidSpray(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST011',addition_status_rate=100,turns=2)
    show_name = '酸液炸弹'
    property = 'poison'
    skill_power = 40
    skill_code = 'P006'
    skill_info = '攻击目标造成伤害,100%几率令目标的特防降低2级'

class GastroAcid(statusSkill):
    def __init__(self):
        super().__init__(pp=10,status='ST100')

    show_name = '胃液'
    property = 'poison'
    skill_code = 'P007'
    skill_info = '使目标陷入无特性状态'

class Belch(damageSkill):
    def __init__(self):
        super().__init__(pp=10)

    show_name = '打嗝'
    property = 'poison'
    skill_code = 'P008'
    skill_power = 120
    hit_rate = 90
    skill_info = '攻击目标造成伤害,如果自身没有处于吃饱状态则招式无法选择'
    use_condition = 'ST014'

class Coil(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST015','ST016','ST017'])

    show_name = '盘蜷'
    property = 'poison'
    skill_code = 'P009'
    hit_rate = 0
    skill_info = '攻击者命中,攻击,防御提升1级'

class GunkShot(damageSkill):
    def __init__(self):
        super().__init__(pp=5,hit_status='ST007',addition_status_rate=30,spell_skill=False)
    show_name = '垃圾射击'
    property = 'poison'
    skill_code = 'P010'
    hit_rate = 80
    skill_power = 120
    skill_info = '攻击目标造成伤害,有30%的几率使目标陷入中毒状态'

class ThunderFang(MultipleDamageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status=['ST002','ST004'],addition_status_rate=10,spell_skill=False)
    show_name = '雷电牙'
    skill_code = 'H001'
    property = 'electric'
    hit_rate = 95
    skill_power = 65
    skill_info = '攻击目标造成伤害,有10%的几率使目标陷入麻痹/畏缩状态'

class Twister(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST004',addition_status='ST024',addition_status_rate=20)

    show_name = '龙卷风'
    skill_code = 'G001'
    property = 'dragon'
    skill_power = 40
    skill_info = '攻击目标造成伤害,如果目标处于飞翔状态，威力翻倍,有20%的几率使目标陷入畏缩状态'
