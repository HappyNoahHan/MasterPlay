'''
#skill_code 技能代号  A  火系  N 普通系 B 木系 C 虫系 D 水系 S 超能=光 I 冰 T 恶=黑暗 E 地面 F 飞行 G 龙
                     R 岩石 P 毒 Q鬼魂 H 电     Y 妖精 fairy    X 钢 steel
#skill_mode 技能类型   0001 伤害技能 0002 防御临时提升 003 debuff 技能
                     0004 施加状态技能  0005 移除状态技能
                     0008 生命恢复 0009 属性亲和，同属性技能伤害加成
                     0010 伤害并恢复生命
                     0011 印记类技能 和印记多少有关 印记以状态显示
                     0012 增益状态技能
                     0013 特殊状态技能 eg.吹飞
                     0014 复制类技能
                     0015 延时类技能  eg. 挖地 飞天
                     0016 树果类技能  技能效果随树果的种类而变化
                     0017 改变场地的技能 eg 青草场地 玩水
                     0018 一击必杀  eg 角钻
                     0019 锁资源技能 eg 定身法
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

from assist import  rancom,petattr
from pets import statusmap,talentmap
from props import berrymap
import random

class skill(object):
    def __init__(self,pp=30,weather_condition=None):
        self._pp_value_max = pp
        self.pp_value = self._pp_value_max
        self.weather_condition = weather_condition

    skill_info = '使用技能'
    effect_turns = 1
    property = 'normal'
    hit_rate = 100
    skill_power = None
    use_condition = None  #使用条件
    multi_step = False #多段技能 默认False
    show_name = None
    skill_code = '0000'
    lock = False




    def __str__(self):
        return self.skill_info + ' || Power: ' + str(self.skill_power)

    def getProp(self):
        return self.property

class damageSkill(skill):
    def __init__(self,pp=30,hit_status=None,addition_status = None,
                 addition_status_rate = 5,spell_skill=True,lucky_level=1,
                 turns=1,power_changed=False,side_effect=None,
                 clean_status=None,fixed_damage=False):
        '''
        :param pp: pp value
        :param hit_status: 附加状态
        :param addition_status: 状态威力加强
        :param addition_status_rate: 状态几率
        :param spell_skill: 技能类型 物理or特殊
        :param lucky_level: 会心等级 默认=1
        :param truns: status层数
        :param side_effect: 副作用 默认None  数据形式(status turns)
        :param clean_status: 清除某些状态
        :param fixed_damage: 固定伤害值技能
        '''
        super().__init__(pp)
        self.skill_model = '0001'
        self.hit_status = hit_status #技能附加状态
        self.addition_status = addition_status #技能检查伤害加成状态
        self.addition_status_rate = addition_status_rate
        self.spell_skill = spell_skill #特殊攻击类型 True 默认 物理攻击类型 False
        self.lucky_level = lucky_level
        self.turns = turns
        self.power_changed = power_changed
        self.side_effect = side_effect
        self.clean_status = clean_status
        self.fixed_damage = fixed_damage


    def addStatus(self,obj,place):
        if self.hit_status != None:
            if rancom.statusRandom(self.addition_status_rate):
                if self.hit_status not in obj.status:
                    # 检查特性与obj 属性 某些pet不会中某技能
                    if talentmap.addStatusOrNot(obj,self.hit_status,place):
                        obj.setStatus(self.hit_status,self.turns)
                        print("%s 陷入了 %s 状态！" % (obj.name,statusmap.status_dict[self.hit_status].status_show_name))
                    else:
                        print("%s 免疫 %s 状态" % (obj.name,statusmap.status_dict[self.hit_status].status_show_name))

    def doublePowerOrNot(self,obj):
        '''
        改写成多种状态
        :param obj:
        :return:
        '''
        if self.addition_status != None:
            #ST999 弱点攻击
            for status in self.addition_status:
                if status in obj.status:
                #print("%s 受到了双倍伤害" % obj.name)
                    return True
        return False

    def getSideEffect(self,obj):
        '''
        为pet 加上技能的副作用
        :param obj:
        :return:
        '''
        obj.setStatus(self.side_effect[0],self.side_effect[1])

    def cleanStatus(self,obj):
        for status in self.clean_status:
            if status in obj.status:
                obj.removeStatus(status)

class MultipleDamageSkill(damageSkill):
    def addStatus(self,obj,place):
        if self.hit_status != None:
            for status in self.hit_status:
                if rancom.statusRandom(self.addition_status_rate):
                    if status not in obj.status:
                        # 检查特性与obj 属性 某些pet不会中某技能
                        if talentmap.addStatusOrNot(obj,status,place):
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
    def __init__(self,pp=30,status=None,turns = 1,side_effect=False,add_condition=None):
        super().__init__(pp)
        self.skill_model = '0004'
        self.status = status
        self.turns = turns
        self.side_effect = side_effect
        self.add_condition = add_condition #中状态条件

    def addStatus(self,obj,place):
        if self.status not in obj.status:
            if talentmap.addStatusOrNot(obj,self.status,place):
                obj.setStatus(self.status,self.turns)
                print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
            else:
                print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
        else:
            print("%s 已经陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))

class MutlipleStatusSkill(statusSkill):
    def addStatus(self,obj,place,double=1):
        if self.add_condition != None:
            if self.add_condition not in obj.status:
                print("没有任何效果~")
                return True
        for status in self.status:
            if status not in obj.status:
                if talentmap.addStatusOrNot(obj, status,place):
                    obj.setStatus(status,self.turns * double)
                    print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
                else:
                    print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
            else:
                print("%s 已经陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))



class GainStatusUpSkill(skill):
    '''
    多重加增益状态技能
    '''

    def __init__(self, pp=30, status=None, turns=1,weather_condition=None):
        super().__init__(pp,weather_condition)
        self.skill_model = '0012'
        self.status = status
        self.turns = turns
        #self.weather_condition = weather_condition

    def addStatus(self,obj,place,double=1):
        for status in self.status:
            if status not in obj.status:
                if talentmap.addStatusOrNot(obj, status,place):
                    obj.setStatus(status,self.turns * double)
                    print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
                else:
                    print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
            else:
                print("%s 已经陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))

    def doubleEffect(self,weather):
        if self.weather_condition != None and weather != None:
            if weather.code in self.weather_condition:
                return True
        return False


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
    def __init__(self,pp=30,index_per=0.5,weather_condition=None):
        super().__init__(pp,weather_condition)
        self.skill_model = '0008'
        self.index_per = index_per

    def getIndexPer(self):
        return self.index_per


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
            if obj.last_used_skill.skill_model != '0014' and obj.last_used_skill.multi_step == False:
                return obj.last_used_skill
        return None

class DelayedSkill(skill):
    def __init__(self,pp=30,add_status_begin=None,add_status_end=None,spell_skill=True,
                 lucky_level=1,delay_effect=True,power_change_by_hit=False,hit_count=0):
        super().__init__(pp)
        self.skill_model = '0015'
        self.add_status_begin = add_status_begin
        self.add_status_end = add_status_end
        self.spell_skill = spell_skill #特殊攻击类型 True 默认 物理攻击类型 False
        self.lucky_level = lucky_level
        self.delay_effect = delay_effect
        self.power_change_by_hit = power_change_by_hit
        self.hit_count = hit_count #击中次数

    def setDelayedSkill(self,pet):
        pet.setSkills('delay',self)

    def addStatus(self,pet):
        pet.setStatus(self.add_status_begin)
        pet.autoAi = 'lost'

    def removeStatus(self,pet):
        pet.removeStatus(self.add_status_begin)
        pet.removeSkills('delay')
        pet.autoAi = False
        if self.add_status_end != None:
            pet.setStatus(self.add_status_end)

    def useSkill(self,pet):
        if self.add_status_begin not in pet.status:
            self.setDelayedSkill(pet)
            self.addStatus(pet)


    def doublePowerOrNot(self,obj):
        return False

    def getPower(self):
        return self.skill_power

class BerryEffectSkill(skill):
    def __init__(self,pp=30,spell_skill=True,lucky_level=1):
        super().__init__(pp)
        self.skill_model = '0016'
        self.spell_skill = spell_skill
        self.lucky_level = lucky_level

    def doublePowerOrNot(self,obj):
        return False

class PlaceStatusSkill(skill):
    def __init__(self,pp=30,status=None,turns=5):
        super().__init__(pp)
        self.skill_model = '0017'
        self.status = status
        self.turns = turns

class OneHitKillSkill(skill):
    def __init__(self,pp=30,spell_skill=True):
        super().__init__(pp)
        self.skill_model = '0018'
        self.spell_skill = spell_skill

class LockSkill(skill):
    def __init__(self,pp=30,status=None,turns = 5):
        super(LockSkill, self).__init__(pp)
        self.status = status
        self.turns = turns
        self.skill_model = '0019'

    def addStatus(self,pet):
        if pet.last_used_skill:
            pet.setStatus(self.status, self.turns)
            pet.last_used_skill.lock = True
            print("%s 被限制使用 %s ！"%(pet.name,pet.last_used_skill.show_name))
        else:
            print("没有任何效果~")


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
    #index_per = 0.5
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

class Hurricane(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status='ST006',addition_status_rate=30)
    show_name = '暴风'
    skill_code = 'F009'
    hit_rate = 70
    skill_power = 110
    property = 'fly'
    skill_info = '攻击目标造成伤害,有30%的几率使目标陷入混乱状态'


class Peck(damageSkill):
    def __init__(self):
        super().__init__(pp=35,spell_skill=False)
    show_name = '啄'
    skill_code = 'F010'
    skill_power = 35
    skill_info = '啄对方,造成伤害'
    property = 'fly'

class AerialAce(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '燕返'
    skill_code = 'F011'
    skill_power = 60
    skill_info = '攻击目标造成伤害,一定会命中'
    hit_rate = 0
    property = 'fly'

class DrillPeck(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '啄钻'
    skill_code = 'F012'
    skill_power = 80
    skill_info = '攻击目标造成伤害'
    property = 'fly'

class Pluck(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '啄食'
    skill_code = 'F013'
    skill_power = 60
    skill_info = '攻击目标造成伤害。如果目标携带了树果，消耗掉目标的树果'#后续功能，暂时是个伤害技能
    property = 'fly'

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

class Growl(statusSkill):
    def __init__(self):
        super().__init__(pp=40,status='ST021')
    show_name = '叫声'
    skill_code = 'N015'
    skill_info = '令目标的攻击降低1级'

class FuryAttack(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '乱击'
    skill_info = '用角或喙刺向对手进行攻击，一回合内连续攻击2～5次'
    skill_power = 15
    hit_rate = 85
    skill_code = 'N016'
    multi_step = True

class FocusEnergy(GainStatusUpSkill):
    def __init__(self):
        super().__init__(status=['ST026'])
    show_name = '聚气'
    skill_code = 'N017'
    skill_info = '使自身进入易中要害状态'
    hit_rate = 0

class Growth(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST016','ST018'],weather_condition=['W001','W002'])
    show_name = '生长'
    skill_code = 'N018'
    skill_info = '令使用者的攻击提升1级,令使用者的特攻提升1级,在大晴天或大日照天气下等级提升数量翻倍'

class SweetScent(statusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST028')
    show_name = '甜甜香气'
    skill_code = 'N019'
    skill_info = '令目标的闪避率降低2级'

class LuckyChant(GainStatusUpSkill):
    def __init__(self):
        super().__init__(status=['ST030'],turns=5)
    show_name = '幸运咒语'
    skill_code = 'N020'
    skill_info = '会陷入幸运咒语状态，５回合内，变得不会被对手的招式击中要害'

class NaturalGift(BerryEffectSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False)

    show_name = '自然之恩'
    skill_code = 'N021'
    skill_info = '攻击目标造成伤害,威力和属性取决于这只宝可梦身上的树果,树果在使用后会消失'
    #use_condition = 'berry'

    def getPowerAndProperty(self,berry):
        return berrymap.berry_effect_for_NaturalGift[berry.code][0],berrymap.berry_effect_for_NaturalGift[berry.code][1]

class Slam(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '摔打'
    skill_code = 'N022'
    skill_power = 80
    hit_rate = 75
    skill_info = '摔打目标造成伤害'

class WringOut(damageSkill):
    def __init__(self):
        super().__init__(pp=5,power_changed=True)

    show_name = '绞紧'
    skill_code = 'N023'
    skill_info = '攻击目标造成伤害,威力与对手剩余HP有关，公式为 1 + 120 × 当前HP ÷ 满HP,最大为121'

    def getPower(self,obj_attack,obj_defense):
        power = 1 + 120 * obj_defense.health / obj_defense._max_health
        if power > 121:
            power = 121
        return round(power)

class Constrict(damageSkill):
    def __init__(self):
        super().__init__(pp=35,hit_status='ST023',addition_status_rate=10)
    show_name = '缠绕'
    skill_code = 'N024'
    skill_power = 10
    skill_info = '攻击目标造成伤害,10%几率令目标的速度降低1级'

class ReflectType(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=15,status=['ST097'])
    show_name = '镜面属性'
    skill_code = 'N025'
    skill_info = '反射对手的属性,让自己也变成一样的属性'
    hit_rate = 0

class Smokescreen(statusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST013')
    show_name = '烟幕'
    skill_code = 'N026'
    skill_info = '向对手喷出烟或墨汁等,从而降低对手的命中'

class TailWhip(statusSkill):
    def __init__(self):
        super().__init__(status='ST009')
    show_name = '摇尾巴'
    skill_code = 'N027'
    skill_info = '可爱地左右摇晃尾巴,诱使对手疏忽大意,会降低对手的防御'

class HornAttack(damageSkill):
    def __init__(self):
        super().__init__(pp=25,spell_skill=False)
    show_name = '角撞'
    skill_code = 'N028'
    skill_info = '用尖锐的角攻击对手'
    skill_power = 65

class Flail(damageSkill):
    def __init__(self):
        super().__init__(pp=15,power_changed=True,spell_skill=False)
    show_name = '抓狂'
    skill_code = 'N029'
    skill_info = '抓狂般乱打进行攻击,自己的ＨＰ越少.招式的威力越大'

    def getPower(self,obj_attack,obj_defense):
        health_per = round(obj_attack.health/obj_attack._max_health,4) * 100
        if 0 < health_per < 4.17:
            power = 200
        elif 4.17 <= health_per < 10.42:
            power = 150
        elif 10.42 <= health_per < 20.83:
            power = 100
        elif 20.83 <= health_per < 35.42:
            power = 80
        elif 35.42 <= health_per < 68.75:
            power = 40
        else:
            power = 20
        return power

class HornDrill(OneHitKillSkill):
    def __init__(self):
        super().__init__(pp=5,spell_skill=False)
    show_name = '角钻'
    skill_code = 'N030'
    hit_rate = 30
    skill_info = '用旋转的角刺入对手进行攻击,只要命中就会一击濒死'

class Harden(GainStatusUpSkill):
    def __init__(self):
        super().__init__(status=['ST017'])
    show_name = '变硬'
    skill_code = 'N031'
    hit_rate = 0
    skill_info = '全身使劲,让身体变硬,从而提高自己的防御'

class RapidSpin(damageSkill):
    def __init__(self):
        super().__init__(pp=40,spell_skill=False,clean_status=['ST025'])
    show_name = '高速旋转'
    skill_code = 'N032'
    skill_info = '通过旋转来攻击对手,还可以摆脱绑紧、紧束、寄生种子和撒菱等招式'
    skill_power = 20

class Recover(lifeRecoreSkill):
    def __init__(self):
        super().__init__(pp=10)
    show_name = '自我再生'
    skill_code = 'N033'
    skill_info = '让全身的细胞获得再生,回复一半HP'
    hit_rate = 0

class Camouflage(GainStatusUpSkill):
    def __init__(self):
        super(Camouflage, self).__init__(pp=20,status=['ST094'])

    show_name = '保护色'
    skill_code = 'N034'
    skill_info = '根据所在场所不同以改变自己的属性'
    hit_rate = 0

class Minimize(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=10,status=['ST105','ST027'],turns=2)

    show_name = '变小'
    skill_code = 'N035'
    skill_info = '蜷缩身体显得很小,从而大幅提高自己的闪避率'
    hit_rate = 0

class Pound(damageSkill):
    def __init__(self):
        super(Pound, self).__init__(pp=35,spell_skill=False)
    show_name = '拍击'
    skill_code = 'N036'
    skill_power = 40
    skill_info = '使用长长的尾巴或手等拍打对手进行攻击'

class Disable(LockSkill):
    def __init__(self):
        super(Disable, self).__init__(pp=20,status='ST106',turns=4)
    show_name = '定身法'
    skill_code = 'N037'
    skill_info = '使目标陷入定身法状态,在此期间目标不能使用陷入定身法状态前最后使用的招式'

class SonicBoom(damageSkill):
    def __init__(self):
        super(SonicBoom, self).__init__(pp=20,fixed_damage=True)
    show_name = '音爆'
    skill_code = 'N038'
    hit_rate = 90
    skill_info = '将冲击波撞向对手进行攻击,必定会给予２０的伤害'

    def getDamage(self):
        return  20

class Lockon(statusSkill):
    def __init__(self):
        super().__init__(pp=5,status='ST104',turns=2)
    show_name = '锁定'
    hit_rate = 0
    skill_code = 'N039'
    skill_info = '紧紧瞄准对手,下次攻击必定会打中'

class TriAttack(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status=random.choice(['ST001','ST002','ST008']),addition_status_rate=20)
    show_name = '三重攻击'
    skill_power = 80
    skill_code = 'N040'
    skill_info = '用３种光线进行攻击,有时会让对手陷入麻痹、灼伤或冰冻的状态'

class SelfDestruct(damageSkill):
    def __init__(self):
        super().__init__(pp=5,side_effect=True,spell_skill=False)
    show_name = '自爆'
    skill_power = 200
    skill_code = 'N041'
    skill_info = '引发爆炸,攻击自己周围所有的宝可梦,使用后陷入濒死'

    def getSideEffect(self,obj):
        obj.health = 0
        obj.alive = False


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

class StunSpore(statusSkill):
    def __init__(self):
        super().__init__(status = 'ST002')
    skill_info = '使目标陷入麻痹状态'
    skill_code = 'B001'
    show_name = '麻痹粉'
    property = 'wood'
    hit_rate = 75

class azorLeaf(damageSkill):
    def __init__(self):
        super().__init__(lucky_level=2,pp=25,spell_skill=False)
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
    def __init__(self,pp=25):
        super().__init__(pp)

    show_name = '吸取'
    skill_code = 'B006'
    property = 'wood'
    skill_info = "攻击目标造成伤害，自身的ＨＰ恢复“造成的伤害×50%"
    skill_power = 20

class SleepPowder(statusSkill):
    def __init__(self):
        super().__init__(status = 'ST003',pp=15)
    skill_info = '使目标陷入睡眠状态'
    skill_code = 'B007'
    show_name = '催眠粉'
    property = 'wood'
    hit_rate = 75

class MegaDrain(suckBloodSkill):
    def __init__(self,pp=15):
        super().__init__(pp)

    show_name = '超级吸取'
    skill_code = 'B008'
    property = 'wood'
    skill_info = "攻击目标造成伤害，自身的ＨＰ恢复“造成的伤害×50%"
    skill_power = 40

class GigaDrain(suckBloodSkill):
    def __init__(self,pp=10):
        super().__init__(pp)

    show_name = '终极吸取'
    skill_code = 'B009'
    property = 'wood'
    skill_info = "攻击目标造成伤害，自身的ＨＰ恢复“造成的伤害×50%"
    skill_power = 75

class GrassyTerrain(PlaceStatusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST031')
    show_name = '青草场地'
    skill_code = 'B010'
    property = 'wood'
    skill_info = '5回合内所有站地面上的宝可梦每回合回复少许体力。草属性招式的威力提升50%'
    hit_rate = 0

class PetalDance(DelayedSkill):
    def __init__(self):
        super().__init__(pp=10,add_status_begin='ST102',add_status_end='ST006',delay_effect=False)

    show_name = '花瓣舞'
    skill_code = 'B011'
    property = 'wood'
    skill_power = 120
    skill_info = '攻击目标造成伤害,陷入花瓣舞状态,在２～３回合内,乱打一气地进行攻,大闹一番后自己会陷入混乱'

class PetalBlizzard(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False)

    show_name = '落英缤纷'
    skill_code = 'B012'
    property = 'wood'
    skill_power = 90
    skill_info = '攻击目标造成伤害,全场攻击'

class Aromatherapy(removeStatusSkill):
    def __init__(self):
        super().__init__(status='abnormal',pp=5,effecters='attack')
    show_name = '芳香治疗'
    skill_info = '治愈己方队伍所有宝可梦的异常状态'
    skill_code = 'B013'
    property = 'wood'
    hit_rate = 0

class SolarBeam(DelayedSkill):
    def __init__(self):
        super().__init__(pp=10,add_status_begin='ST103')

    show_name = '日光束'
    skill_code = 'B014'
    skill_power = 200
    property = 'wood'
    skill_info = '使用日光束的宝可梦在第一回合进行蓄力,第二回合发动攻击'

class VineWhip(damageSkill):
    def __init__(self):
        super().__init__(pp=25,spell_skill=False)
    show_name = '藤鞭'
    skill_code = 'B015'
    skill_power = 45
    property = 'wood'
    skill_info = '攻击技能,造成伤害'

class LeafTornado(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status='ST013',addition_status_rate=50)
    show_name = '青草搅拌器'
    skill_code = 'B016'
    skill_power = 65
    hit_rate = 90
    property = 'wood'
    skill_info = '攻击目标造成伤害,50%几率令目标的命中率降低1级'

class LeafStorm(damageSkill):
    def __init__(self):
        super().__init__(pp=5,side_effect=('ST022',2))
    show_name = '飞叶风暴'
    skill_code = 'B017'
    skill_power = 130
    hit_rate = 90
    property = 'wood'
    skill_info = '攻击目标造成伤害,令使用者的特攻降低2级'

class LeafBlade(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False,lucky_level=2)
    show_name = '叶刃'
    skill_code = 'B018'
    skill_power = 90
    property = 'wood'
    skill_info = '攻击目标造成伤害,击中要害率比普通招式高1级'

class illuminatiom(removeDebuffSkill):
    def __init__(self,pp=20):
        super().__init__(pp)
    show_name = '光照'
    skill_info = "驱散一个debuff效果"
    skill_code = 'S001'
    property = 'psychic'

class Agility(GainStatusUpSkill):
    def __init__(self):
        super().__init__(status=['ST020'],turns=2)
    show_name = '高速移动'
    skill_info = '使用者的速度提升2级'
    skill_code = 'S002'
    property = 'psychic'
    hit_rate = 0

class Barrier(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST017'],turns=2)
    show_name = '屏障'
    skill_info = '制造坚固的壁障,从而大幅提高自己的防御'
    skill_code = 'S003'
    property = 'psychic'
    hit_rate = 0

class Psywave(damageSkill):
    def __init__(self):
        super().__init__(pp=15,fixed_damage=True)
    show_name = '精神波'
    skill_code = 'S004'
    skill_info = '向对手发射神奇的念波进行攻击,每次使用,伤害都会改变'
    property = 'psychic'

    def getDamage(self,level):
        return round(level * random.randint(5,15) / 10 )

class Psychic(damageSkill):
    def __init__(self):
        super(Psychic, self).__init__(pp=10,hit_status='ST011',addition_status_rate=10)
    show_name = '精神强念'
    skill_code = 'S005'
    skill_info = '向对手发送强大的念力进行攻击,有时会降低对手的特防'
    property = 'psychic'
    skill_power = 90

class LightScreen(PlaceStatusSkill):
    def __init__(self):
        super().__init__(status='ST033')
    show_name = '光墙'
    skill_code = 'S006'
    skill_info = '在５回合内使用神奇的墙,减弱从对手那受到的特殊攻击的伤害'
    property = 'psychic'
    hit_rate = 0

class CosmicPower(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST017','ST019'])
    show_name = '宇宙力量'
    skill_code = 'S007'
    skill_info = '汲取宇宙中神秘的力量,从而提高自己的防御和特防'
    property = 'psychic'
    hit_rate = 0

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

class Pursuit(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False,addition_status=['ST025'])
    skill_power = 40
    skill_code = 'T005'
    show_name = '追打'
    property = 'dark'
    skill_info = '攻击目标造成伤害,如果对方易受伤,威力加倍'

class Assurance(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False,addition_status=['ST025'])
    skill_power = 60
    skill_code = 'T006'
    show_name = '恶意追击'
    property = 'dark'
    skill_info = '攻击目标造成伤害,如果对方易受伤,威力加倍'

class KnockOff(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST098',addition_status_rate=100,spell_skill=False)
    skill_power = 65
    skill_code = 'T007'
    show_name = '拍落'
    property = 'dark'
    skill_info = '攻击目标造成伤害,使目标陷入拍落状态'

class Fling(damageSkill):
    def __init__(self):
        super(Fling, self).__init__(pp=10,power_changed=True)
    skill_code = 'T008'
    show_name = '投掷'
    skill_info = '快速投掷携带的道具进行攻击,根据道具不同,威力和效果会改变'
    property = 'dark'

    def getPower(self,obj_attack,obj_defense):
        return 60  #后续开发 暂时给一个定值

class Memento(MutlipleStatusSkill):
    def __init__(self):
        super().__init__(pp=10,side_effect=True,status=['ST021','ST022'],turns=2)
    show_name = '临别礼物'
    property = 'dark'
    skill_info = '虽然会使自己陷入濒死,但是能够大幅降低对手的攻击和特攻'
    skill_code = 'T009'

    def sideEffect(self,obj):
        obj.health = 0
        obj.alive = False

class Megahorn(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False)
    skill_code = 'C001'
    show_name = '超级角击'
    skill_info = '用坚硬且华丽的角狠狠地刺入对手进行攻击'
    skill_power = 120
    hit_rate = 85
    property = 'insect'

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

class Bubble(damageSkill):
    def __init__(self):
        super().__init__(hit_status='ST023',addition_status_rate=10)
    show_name = '泡沫'
    skill_code = 'D002'
    skill_power = 40
    property = 'water'
    skill_info = '向对手用力吹起无数泡泡进行攻击,有时会降低对手的速度'

class HydroPump(damageSkill):
    def __init__(self):
        super().__init__(pp=5)
    show_name = '水炮'
    skill_code = 'D003'
    skill_power = 110
    property = 'water'
    skill_info = '向对手猛烈地喷射大量水流进行攻击'
    hit_rate = 80

class WaterPulse(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST006',addition_status_rate=20)
    show_name = '水之波动'
    skill_code = 'D004'
    skill_power = 60
    property = 'water'
    skill_info = '用水的震动攻击对手,有时会使对手混乱'

class BubbleBeam(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST023',addition_status_rate=10)
    show_name = '泡沫光线'
    skill_code = 'D005'
    skill_power = 65
    property = 'water'
    skill_info = '向对手猛烈地喷射泡沫进行攻击,有时会降低对手的速度'

class Brine(damageSkill):
    def __init__(self):
        super().__init__(pp=10,power_changed=True)
    show_name = '盐水'
    skill_code = 'D006'
    skill_power = 65
    property = 'water'
    skill_info = '当对手的ＨＰ负伤到一半左右时,招式威力会变成２倍'

    def getPower(self,obj_attack,obj_defense):
        if (obj_defense.health / obj_defense._max_health) <= 0.5:
            return self.skill_power * 2
        else:
            return self.skill_power

class WaterGun(damageSkill):
    def __init__(self):
        super().__init__(pp=25)
    skill_code = 'D007'
    skill_power = 40
    skill_info = '向对手猛烈地喷射水流进行攻击'
    skill_name = '水枪'
    property = 'water'

class WaterSport(PlaceStatusSkill):
    def __init__(self):
        super().__init__(pp=15,status='ST032')
    show_name = '玩水'
    skill_info = '用水湿透周围,在５回合内减弱火属性的招式'
    property = 'water'
    hit_rate = 0
    skill_code = 'D008'

class AquaRing(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST096'])
    show_name = '水流环'
    skill_code = 'D009'
    property = 'water'
    hit_rate = 0
    skill_info = '在自己身体的周围覆盖用水制造的幕,每回合回复ＨＰ'

class Waterfall(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST004',addition_status_rate=20,spell_skill=False)
    show_name = '攀瀑'
    skill_code = 'D010'
    skill_power = 80
    skill_info = '以惊人的气势扑向对手,有时会使对手畏缩'
    property = 'water'

class Soak(statusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST095')
    show_name = '浸水'
    skill_info = '将大量的水泼向对手，从而使其变成水属性'
    property = 'water'
    skill_code = 'D011'

class RockThrow(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False)

    show_name = '落石'
    skill_code = 'R001'
    skill_power = 50
    property = 'rock'
    skill_info = '拿起小岩石,投掷对手进行攻击'
    hit_rate = 90


class RockSlide(damageSkill):
    def __init__(self):
        super().__init__(10,hit_status='ST004',addition_status_rate=30,spell_skill=False)

    show_name = '岩崩'
    skill_code = 'R002'
    skill_power = 75
    property = 'rock'
    skill_info = '将大岩石撞向对面,有一定的几率会使对方畏惧'
    hit_rate = 90

class PowerGem(damageSkill):
    def __init__(self):
        super().__init__(pp=20)
    show_name = '力量宝石'
    skill_code = 'R003'
    skill_power = 80
    property = 'rock'
    skill_info = '发射如宝石般闪耀的光芒攻击对手'

class RockPolish(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST020'],turns=2)
    show_name = '岩石打磨'
    skill_code = 'R004'
    skill_info = '打磨自己的身体,减少空气阻力,可以大幅提高自己的速度'
    property = 'rock'
    hit_rate = 0

class Rollout(DelayedSkill):
    def __init__(self):
        super(Rollout, self).__init__(pp=20,add_status_begin='ST108',spell_skill=False,
                                      delay_effect=False,power_change_by_hit=True)
    show_name = '滚动'
    skill_code = 'R005'
    skill_info = '在５回合内连续滚动攻击对手,招式每次击中,威力就会提高'
    property = 'rock'
    hit_rate = 90
    skill_power = 30

    def getPower(self):
        return 30 * pow(2,(self.hit_count - 1))

class SmackDown(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False,clean_status=['ST107'],hit_status='ST109',addition_status_rate=100)
    show_name = '击落'
    skill_code = 'R006'
    skill_info = '扔石头或炮弹攻击飞行的对手,对手会被击落,掉到地面'
    property = 'rock'
    skill_power = 50

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

class DrillRun(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False,lucky_level=2)
    show_name = '直冲钻'
    skill_code = 'E004'
    skill_info = '攻击目标造成伤害,击中要害率比普通招式高1级'
    property = 'ground'
    skill_power = 80
    hit_rate = 90

class MudSlap(damageSkill):
    def __init__(self):
        super(MudSlap, self).__init__(pp=10,hit_status='ST013',addition_status_rate=100)
    show_name = '掷泥'
    skill_code = 'E005'
    skill_power = 20
    property = 'ground'
    skill_info = '向对手的脸等投掷泥块进行攻击,会降低对手的命中率'

class MudSport(PlaceStatusSkill):
    def __init__(self):
        super(MudSport, self).__init__(pp=15,status='ST035')
    show_name = '玩泥巴'
    skill_code = 'E006'
    skill_info = '一旦使用此招式,周围就会弄得到处是泥,在５回合内减弱电属性的招式'
    property = 'ground'
    hit_rate = 0

class Magnitude(damageSkill):
    def __init__(self):
        super().__init__(power_changed=True,spell_skill=False)
    show_name = '震级'
    skill_code = 'E007'
    skill_info = '晃动地面,攻击自己周围所有的宝可梦,招式的威力会有各种变化'
    property = 'ground'

    def getPower(self,obj_attack,obj_defense):
        return random.choice([10,10,30,30,30,30,50,50,50,50,50,50,50,50,
                              70,70,70,70,70,70,70,70,70,70,70,70,
                              90,90,90,90,90,90,90,90,110,110,110,110,150,150])

class Bulldoze(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False,hit_status='ST023',addition_status_rate=100)
    show_name = '重踏'
    skill_code = 'E008'
    skill_power = 60
    property = 'ground'
    skill_info = '用力踩踏地面并攻击自己周围所有的宝可梦,降低对方的速度'


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

class Hex(damageSkill):
    def __init__(self):
        super().__init__(pp=10,addition_status=['ST001','ST002','ST003','ST005','ST007','ST008'])
    skill_info = '接二连三地进行攻击,对处于异常状态的对手给予较大的伤'
    skill_code = 'Q003'
    show_name = '祸不单行'
    property = 'ghost'
    skill_power = 65

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
        super().__init__(pp=10,addition_status=['ST005'])

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

class PoisonPowder(statusSkill):
    def __init__(self):
        super().__init__(status = 'ST007',pp=35)
    skill_info = '使目标陷入中毒状态'
    skill_code = 'P011'
    show_name = '毒粉'
    property = 'poison'
    hit_rate = 75

class PoisonJab(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST007',addition_status_rate=30,spell_skill=False)
    skill_code = 'P012'
    skill_power = 80
    show_name = '毒击'
    property = 'poison'
    skill_info = '攻击目标造成伤害,有30%的几率使目标陷入中毒状态'

class ToxicSpikes(statusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST025')
    show_name = '毒菱'
    property = 'poison'
    skill_info = '在对手的脚下撒毒菱,容易受伤'
    hit_rate = 0
    skill_code = 'P013'

class SludgeWave(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status='ST007',addition_status_rate=10)
    show_name = '污泥波'
    property = 'poison'
    skill_code = 'P014'
    skill_power = 95
    skill_info = '用污泥波攻击自己周围所有的宝可梦,有时会陷入中毒状'

class PoisonGas(statusSkill):
    def __init__(self):
        super(PoisonGas, self).__init__(pp=40,status='ST007')
    show_name = '毒瓦斯'
    property = 'poison'
    skill_code = 'P015'
    hit_rate = 90
    skill_info = '将毒瓦斯吹到对手的脸上,从而让对手陷入中毒状态'

class Sludge(damageSkill):
    def __init__(self):
        super(Sludge, self).__init__(pp=20,hit_status='ST007',addition_status_rate=30)
    show_name = '污泥攻击'
    property = 'poison'
    skill_code = 'P016'
    skill_power = 65
    skill_info = '用污泥投掷对手进行攻击,有时会让对手陷入中毒状态'

class SludgeBomb(damageSkill):
    def __init__(self):
        super(SludgeBomb, self).__init__(pp=10,hit_status='ST007',addition_status_rate=30)
    show_name = '污泥炸弹'
    property = 'poison'
    skill_code = 'P017'
    skill_power = 90
    skill_info = '用污泥投掷对手进行攻击,有时会让对手陷入中毒状态'

class AcidArmor(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST017'],turns=2)
    show_name = '溶化'
    property = 'poison'
    skill_code = 'P018'
    hit_rate = 0
    skill_info = '通过细胞的变化进行液化,从而大幅提高自己的防御'

class VenomDrench(MutlipleStatusSkill):
    def __init__(self):
        super(VenomDrench, self).__init__(pp=20,status=['ST011','ST021','ST023'],add_condition='ST007')
    show_name = '毒液陷阱'
    property = 'poison'
    skill_code = 'P019'
    skill_info = '将特殊的毒液泼向对手,对处于中毒状态的对手,其攻击、特攻和速度都会降低'

class ThunderFang(MultipleDamageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status=['ST002','ST004'],addition_status_rate=10,spell_skill=False)
    show_name = '雷电牙'
    skill_code = 'H001'
    property = 'electric'
    hit_rate = 95
    skill_power = 65
    skill_info = '攻击目标造成伤害,有10%的几率使目标陷入麻痹/畏缩状态'

class ThunderShock(damageSkill):
    def __init__(self):
        super(ThunderShock, self).__init__(hit_status='ST002',addition_status_rate=10)
    show_name = '电击'
    skill_code = 'H002'
    property = 'electric'
    skill_power = 40
    skill_info = '发出电流刺激对手进行攻击,有时会让对手陷入麻痹状态'

class ThunderWave(statusSkill):
    def __init__(self):
        super(ThunderWave, self).__init__(pp=20,status='ST002')
    show_name = '电磁波'
    skill_code = 'H003'
    property = 'electric'
    hit_rate = 90
    skill_info = '向对手发出微弱的电击,从而让对手陷入麻痹状态'

    def addStatus(self,obj,place):
        if self.status not in obj.status:
            if petattr.getAttrMap(self,obj) != 0:
                if talentmap.addStatusOrNot(obj, self.status,place):
                    obj.setStatus(self.status, self.turns)
                    print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
                    return True
            print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
        else:
            print("%s 已经陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))

class Spark(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False,hit_status='ST002',addition_status_rate=30)
    show_name = '电光'
    skill_code = 'H004'
    skill_power = 65
    skill_info = '让电流覆盖全身,猛撞向对手进行攻击,有时会让对手陷入麻痹状态'
    property = 'electric'

class ElectroBall(damageSkill):
    def __init__(self):
        super().__init__(pp=10,power_changed=True)
    show_name = '电球'
    skill_code = 'H005'
    skill_info = '用电气团撞向对手,自己比对手速度越快,威力越大'
    property = 'electric'

    def getPower(self,obj_attack,obj_defense):
        speed_ratio = obj_attack.getSpeed() / obj_defense.getSpeed()
        if  0 < speed_ratio < 1:
            power = 40
        elif  1 <= speed_ratio < 2:
            power = 60
        elif  2 <= speed_ratio < 3:
            power = 80
        elif 3 <= speed_ratio < 4:
            power = 120
        else:
            power = 150
        return power

class Discharge(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST002',addition_status_rate=30)
    show_name = '放电'
    skill_code = 'H006'
    skill_power = 80
    skill_info = '用耀眼的电击攻击自己周围所有的宝可梦,有时会陷入麻痹状态'
    property = 'electric'

class MagnetRise(statusSkill):
    def __init__(self):
        super().__init__(pp=10,status='ST107',turns=5)
    show_name = '电磁飘浮'
    skill_code = 'H007'
    skill_info = '利用电气产生的磁力浮在空中,在５回合内可以飘浮'
    property = 'electric'
    hit_rate = 0

class ZapCannon(damageSkill):
    def __init__(self):
        super().__init__(pp=5,hit_status='ST002',addition_status_rate=100)
    skill_code = 'H008'
    show_name = '电磁炮'
    skill_power = 120
    hit_rate = 50
    property = 'electric'
    skill_info = '发射大炮一样的电流进行攻击,让对手陷入麻痹状态'

class ElectricTerrain(PlaceStatusSkill):
    def __init__(self):
        super().__init__(pp=10,status='ST034')
    show_name = '电气场地'
    skill_code = 'H009'
    property = 'electric'
    hit_rate = 0
    skill_info = '在５回合内变成电气场地,地面上的宝可梦将无法入眠,电属性的招式威力还会提高'


class Twister(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST004',addition_status=['ST024'],addition_status_rate=20)

    show_name = '龙卷风'
    skill_code = 'G001'
    property = 'dragon'
    skill_power = 40
    skill_info = '攻击目标造成伤害,如果目标处于飞翔状态，威力翻倍,有20%的几率使目标陷入畏缩状态'

class DragonPulse(damageSkill):
    def __init__(self):
        super().__init__(pp=10)
    show_name = '龙之波动'
    skill_code = 'G002'
    property = 'dragon'
    skill_power = 85
    skill_info = '从大大的口中掀起冲击波攻击对手'

class DragonDance(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=20,status=['ST016','ST020'])
    show_name = '龙之舞'
    skill_code = 'G003'
    property = 'dragon'
    skill_info = '激烈地跳起神秘且强有力的舞蹈,从而提高自己的攻击和速度'
    hit_rate = 0

class Moonlight(lifeRecoreSkill):
    def __init__(self):
        super().__init__(pp=5,weather_condition=True)

    show_name = '月光'
    skill_code = 'Y001'
    property = 'fairy'
    skill_info = '月光恢复使用者的ＨＰ值。恢复量由当前天气决定'

    def getIndexPer(self,weather):
        if weather.code in ['W001','W002']:
            return 0.66
        if weather.code in ['W003']:
            return 0.5
        if weather.code in ['W004','W005','W006','W007','W008']:
            return 0.25

class Moonblast(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST021',addition_status_rate=30)

    show_name = '月亮之力'
    skill_code = 'Y002'
    property = 'fairy'
    skill_info = '攻击目标造成伤害,30%几率令目标的特攻降低1级'
    skill_power = 95

class GyroBall(damageSkill):
    def __init__(self):
        super().__init__(pp=5,spell_skill=False,power_changed=True)

    show_name = '陀螺球'
    skill_code = 'X001'
    property = 'steel'
    skill_info = '让身体高速旋转并撞击对手,速度比对手越慢威力越大'

    def getPower(self,obj_attack,obj_defense):
        power = round(25 * obj_defense.getSpeed() / obj_attack.getSpeed())

        if power > 150:
            power =150

        return power

class MagnetBomb(damageSkill):
    def __init__(self):
        super(MagnetBomb, self).__init__(pp=20,spell_skill=False)
    show_name = '磁铁炸弹'
    skill_code = 'X002'
    property = 'steel'
    skill_info = '发射吸住对手的钢铁炸弹,攻击必定会命中'
    hit_rate = 0
    skill_power = 60

class MirrorShot(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status='ST013',addition_status_rate=30)
    show_name = '镜光射击'
    skill_power = 65
    hit_rate = 85
    property = 'steel'
    skill_code = 'X003'
    skill_info = '抛光自己的身体,向对手释放出闪光之力,有时会降低对手的命中率'

class MetalSound(statusSkill):
    def __init__(self):
        super().__init__(pp=40,status='ST011',turns=2)
    show_name = '金属音'
    hit_rate = 85
    property = 'steel'
    skill_code = 'X004'
    skill_info = '让对手听摩擦金属般讨厌的声音,大幅降低对手的特防'

class FlashCannon(damageSkill):
    def __init__(self):
        super(FlashCannon, self).__init__(pp=10,hit_status='ST011',addition_status_rate=10)
    show_name = '加农光炮'
    skill_power = 80
    property = 'steel'
    skill_code = 'X005'
    skill_info = '将身体的光芒聚集在一点释放出去,有时会降低对手的特防'