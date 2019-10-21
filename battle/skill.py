'''
#skill_code 技能代号  A  火系  N 普通系 B 木系 C 虫系 D 水系 S 超能=光 I 冰 T 恶=黑暗 E 地面 F 飞行 G 龙
                     R 岩石 P 毒 Q鬼魂 H 电     Y 妖精 fairy    X 钢 steel   Z combat 格斗
#skill_mode 技能类型   0001 伤害技能
                     0004 施加状态技能
                     0008 生命恢复
                     #0010 伤害并恢复生命 合并入0001
                     0011 印记类技能 和印记多少有关 印记以状态显示
                     0012 增益状态技能
                     0013 特殊状态技能 eg.吹飞
                     0014 复制类技能
                     0015 延时类技能  eg. 挖地 飞天
                     0016 树果类技能  技能效果随树果的种类而变化
                     0017 改变场地的技能 eg 青草场地 玩水
                     #0018 一击必杀  eg 角钻  合并0001
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
#hit_rate    命中  0 = 100% 命中
'''

from assist import  rancom,petattr,weathermap,life
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
    limit_skill = False  #限制第一回合使用
    use_condition = None  #使用条件
    multi_step = False #多段技能 默认False
    show_name = None
    skill_code = '0000'
    lock = False
    priority = 5 #释放优先度

    def __str__(self):
        return self.skill_info + ' || Power: ' + str(self.skill_power)

    def getProp(self):
        return self.property

    def getPower(self):
        return self.skill_power

class damageSkill(skill):
    def __init__(self,pp=30,hit_status=None,addition_status = None,
                 addition_status_rate = 5,spell_skill=True,lucky_level=1,
                 turns=1,power_changed=False,side_effect=False,self_effect=None,
                 clean_status=None,fixed_damage=False,berry_effect=False,
                 remove_status=None,recover_by_damage = False,recover_per = 0.0,
                 one_hit_kill=False,prize_efect = False):
        '''
        :param pp: pp value
        :param hit_status: 附加状态
        :param addition_status: 状态威力加强
        :param addition_status_rate: 状态几率
        :param spell_skill: 技能类型 物理or特殊
        :param lucky_level: 会心等级 默认=1
        :param truns: status层数
        :param side_effect: 副作用
        :param clean_status: 清除某些状态
        :param fixed_damage: 固定伤害值技能
        :param berry_effect: 树果效果
        :param self_effect: 自生属性提升 默认None  数据形式([status], turns, per)
        :param remove_status: 移除对方的状态
        :param recover_by_damage: 伤害回复 默认False
        :param recover_per: 回复比例 默认0
        :param one_hit_kill: 一击必杀 默认False
        :param prize_efect: 赏金增加
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
        self.berry_effect = berry_effect
        self.self_effect = self_effect
        self.remove_status = remove_status
        self.recover_by_damage = recover_by_damage
        self.recover_per = recover_per
        self.one_hit_kill = one_hit_kill
        self.prize_effect = prize_efect


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

    def getSideEffect(self,obj,damage):
        return True

    def selfSideEffect(self,obj_attack,obj_defense,damage):
        if rancom.statusRandom(self.self_effect[2]):
            for status in self.self_effect[0]:
                obj_attack.setStatus(status,self.self_effect[1])

    def cleanStatus(self,obj):
        for status in self.clean_status:
            if status in obj.status:
                obj.removeStatus(status)

    def removeStatus(self,obj):
        for status in self.remove_status:
            if status in obj.status:
                obj.removeStatus(status)

    def recover(self,obj,damage):
        life.healthRecoverFromDamage(obj,damage,self.recover_per)

    # 多段技能触发几段
    def getStepOfSkill(self):
        num = random.randint(1, 100)

        if num < 34:
            return 2
        elif 33 < num < 67:
            return 3
        elif 66 < num < 84:
            return 4
        else:
            return 5

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

class statusSkill(skill):
    def __init__(self,pp=30,status=None,turns = 1,side_effect=False,add_condition=None,need_user=False,spell_skill=None):
        super().__init__(pp)
        self.skill_model = '0004'
        self.status = status
        self.turns = turns
        self.side_effect = side_effect
        self.add_condition = add_condition #中状态条件
        self.need_user = need_user #是否需要记录使用者
        self.spell_skill = spell_skill #技能类型 None 变化型

    def addStatus(self,obj,place):
        if talentmap.addStatusOrNot(obj,self.status,place):
            obj.setStatus(self.status,self.turns)
            print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))
        else:
            print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[self.status].status_show_name))

    def setStatusGiver(self,pet):
        statusmap.status_dict[self.status].status_giver = (pet,self)

class MutlipleStatusSkill(statusSkill):
    def addStatus(self,obj,place,double=1):
        if self.add_condition != None:
            if self.add_condition not in obj.status:
                print("没有任何效果~")
                return True
        for status in self.status:
            if talentmap.addStatusOrNot(obj, status,place):
                obj.setStatus(status,self.turns * double)
                print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
            else:
                print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))

class GainStatusUpSkill(skill):
    '''
    多重加增益状态技能
    '''

    def __init__(self, pp=30, status=None, turns=1,weather_condition=None,spell_skill=None):
        super().__init__(pp,weather_condition)
        self.skill_model = '0012'
        self.status = status
        self.turns = turns
        self.spell_skill = spell_skill  # 技能类型 None 变化型
        #self.weather_condition = weather_condition

    def addStatus(self,obj,place,double=1):
        for status in self.status:
            if talentmap.addStatusOrNot(obj, status,place):
                obj.setStatus(status,self.turns * double)
                print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
            else:
                print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))

    def doubleEffect(self,weather):
        if self.weather_condition != None and weather != None:
            if weather in self.weather_condition:
                return True
        return False

class RecoverSkill(skill):
    def __init__(self,pp=30,weather_condition=None,recover_per=0.0
                 ,recover_health = False,recover_status = False,
                 clean_status=None,remove_status=None,hit_status=None,turns=0,
                 max_recover_allowable = True,spell_skill=None):
        super().__init__(pp,weather_condition)
        self.skill_model = '0008'
        self.recover_per = recover_per
        self.recover_health = recover_health
        self.recover_status = recover_status
        self.clean_status = clean_status #清除自身状态
        self.remove_status = remove_status #清除对面状态
        self.hit_status = hit_status #附加状态
        self.turns = turns #层数
        self.max_recover_allowable = max_recover_allowable #满状态治疗允许
        self.spell_skill = spell_skill

    def getIndexPer(self):
        return self.recover_per

    def cleanStatus(self,pet):
        for status in self.clean_status:
            if status in pet.status:
                statusmap.removeStatus(pet,status_code=status)

    def removeStatus(self,pet):
        for status in self.remove_status:
            if status in pet.status:
                statusmap.removeStatus(pet,status_code=status)

    def setStatus(self,pet,place):
        for status in self.hit_status:
            if talentmap.addStatusOrNot(pet, status, place):
                pet.setStatus(status, self.turns)
                print("%s 陷入 %s 状态 ！" % (pet.name, statusmap.status_dict[status].status_show_name))
            else:
                print("%s 免疫 %s 状态 ！" % (pet.name, statusmap.status_dict[status].status_show_name))
            statusmap.status_dict[status].status_giver = (pet,self)

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


class SpecialStatusSkill(skill):
    def __init__(self,pp=30,status=None,turns =1 ,spell_skill=None):
        super().__init__(pp)
        self.skill_model = '0013'
        self.status = status
        self.turns = turns
        self.spell_skill = spell_skill

    def addStatus(self,obj_attack,obj_defense):
        if obj_attack.level >= obj_defense.level:
            if obj_defense.has_trainer == False:
                obj_defense.setStatus(self.status)
                print("%s 陷入 %s 状态 ！" % (obj_defense.name, statusmap.status_dict[self.status].status_show_name))
                return True
        return False

class CopySkill(skill):
    def __init__(self,pp=30,spell_skill=None,copy_skill_or_not=True):
        super().__init__(pp)
        self.skill_model = '0014'
        self.spell_skill = spell_skill
        self.copy_skill_or_not = copy_skill_or_not

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
        if isinstance(self.add_status_begin,list):
            for status in self.add_status_begin:
                pet.setStatus(status)
        else:
            pet.setStatus(self.add_status_begin)
        pet.is_autoAi = 'lost'

    def removeStatus(self,pet):
        if isinstance(self.add_status_begin,list):
            for status in self.add_status_begin:
                pet.removeStatus(status)
        else:
            pet.removeStatus(self.add_status_begin)
        pet.removeSkills('delay')
        pet.is_autoAi = False
        if self.add_status_end != None:
            pet.setStatus(self.add_status_end)

    def useSkill(self,pet):
        if isinstance(self.add_status_begin,list):
            if self.add_status_begin[0] not in pet.status:
                self.setDelayedSkill(pet)
                self.addStatus(pet)
        else:
            if self.add_status_begin not in pet.status:
                self.setDelayedSkill(pet)
                self.addStatus(pet)

class BerryEffectSkill(skill):
    def __init__(self,pp=30,spell_skill=True,lucky_level=1):
        super().__init__(pp)
        self.skill_model = '0016'
        self.spell_skill = spell_skill
        self.lucky_level = lucky_level

class PlaceStatusSkill(skill):
    def __init__(self,pp=30,status=None,turns=5,weather_change=False,weather=None,spell_skill=None):
        super().__init__(pp)
        self.skill_model = '0017'
        self.status = status
        self.turns = turns
        self.weather_change = weather_change
        self.weather = weather
        self.spell_skill = spell_skill

class LockSkill(skill):
    def __init__(self,pp=30,status=None,turns = 5,spell_skill=None):
        super(LockSkill, self).__init__(pp)
        self.status = status
        self.turns = turns
        self.skill_model = '0019'
        self.spell_skill = spell_skill

    def addStatus(self,pet,attack_pet):
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

class Roost(RecoverSkill):
    def __init__(self,pp=10):
        super().__init__(pp,recover_per=0.5,recover_health=True)
    show_name = '羽栖'
    skill_code = 'F006'
    #index_per = 0.5
    property = 'fly'
    skill_info = "恢复使用者的1⁄2的ＨＰ值"

class Tailwind(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=15,status=['ST120'],turns=4)
    show_name = '顺风'
    skill_code = 'F007'
    skill_info = "己方场地上全部的宝可梦的速度加倍,持续时间为4回合,包括使用的当回合"
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
        super().__init__(pp=20,spell_skill=False,berry_effect=True)
    show_name = '啄食'
    skill_code = 'F013'
    skill_power = 60
    skill_info = '攻击目标造成伤害。如果目标携带了树果，消耗掉目标的树果'
    property = 'fly'

    def eatBerry(self,obj_attack,obj_defense):
        if obj_defense.berry:
            obj_defense.berry.berryEffect(obj_attack)
            obj_defense.berry = None

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

class Roar(Whirlwind):
    skill_code = 'N069'
    skill_info = '吓唬对面使其逃跑'
    show_name = '吼叫'

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

class HornDrill(damageSkill):
    def __init__(self):
        super().__init__(pp=5,spell_skill=False,one_hit_kill=True)
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

class Recover(RecoverSkill):
    def __init__(self):
        super().__init__(pp=10,recover_health=True,recover_per=0.5)
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

    def getDamage(self,obj_attack,obj_defense):
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

    def getSideEffect(self,obj,damage):
        obj.health = 0
        #obj.alive = False

class DoubleEdge(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False,side_effect=True)
    show_name = '舍身冲撞'
    skill_power = 120
    skill_code = 'N042'
    skill_info = '拼命地猛撞向对手进行攻击,自己也会受到不小的伤害'

    def getSideEffect(self,obj,damage):
        obj.health -= round(damage / 3)
        print("%s 受到了 %s 反弹伤害" % (obj.name,round(damage / 3)))

class Explosion(damageSkill):
    def __init__(self):
        super().__init__(pp=5,spell_skill=False,side_effect=True)
    show_name = '大爆炸'
    skill_power = 250
    skill_code = 'N043'
    skill_info = '引发大爆炸,攻击自己周围所有的宝可梦,使用后自己会陷入濒死'

    def getSideEffect(self,obj,damage):
        obj.health = 0

class DefenseCurl(GainStatusUpSkill):
    def __init__(self):
        super(DefenseCurl, self).__init__(pp=40,status=['ST017','ST110'])
    skill_code = 'N044'
    hit_rate = 0
    show_name = '变圆'
    skill_info = '将身体蜷曲变圆,从而提高自己的防御'

class ScaryFace(statusSkill):
    def __init__(self):
        super().__init__(pp=10,status='ST023',turns=2)
    skill_code = 'N045'
    show_name = '鬼面'
    skill_info = '用恐怖的脸瞪着对手,使其害怕,从而大幅降低对手的速度'

class Slash(damageSkill):
    def __init__(self):
        super(Slash, self).__init__(pp=20,spell_skill=False,lucky_level=2)
    show_name = '劈开'
    skill_code = 'N046'
    skill_power = 70
    skill_info = '用爪子或镰刀等劈开对手进行攻击,容易击中要害'

class TakeDown(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False,side_effect=True)
    show_name = '猛撞'
    skill_code = 'N047'
    skill_power = 90
    hit_rate = 85
    skill_info = '以惊人的气势撞向对手进行攻击,自己也会受到少许伤害'

    def getSideEffect(self,obj,damage):
        obj.health -= round(damage / 4)
        print('%s 受到了 %s 的反弹伤害' % (obj.name,round(damage / 4 )))

class Protect(GainStatusUpSkill):
    def __init__(self):
        super(Protect, self).__init__(pp=10,status=['ST017','ST019'],turns=2)
    show_name = '守住'
    skill_code = 'N048'
    hit_rate = 0
    skill_info = '守住,大幅提高防御'

class SkullBash(DelayedSkill):
    def __init__(self):
        super(SkullBash, self).__init__(pp=10,add_status_begin=['ST113','ST017'],spell_skill=False)
    show_name = '火箭头锤'
    skill_code = 'N049'
    skill_power = 130
    skill_info = '第１回合把头缩进去,从而提高防御,第２回合攻击对手'

class FakeOut(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False,hit_status='ST004',addition_status_rate=100)
    show_name = '击掌奇袭'
    skill_code = 'N050'
    skill_power = 40
    skill_info = '进行先制攻击,使对手畏缩,要在出场后立刻使出才能成功'
    limit_skill = True

class Safeguard(statusSkill):
    def __init__(self):
        super().__init__(pp=5,status='ST114')
    show_name = '神秘守护'
    skill_code = 'N051'
    skill_info = '在５回合内被神奇的力量守护,从而不会陷入异常状态'
    hit_rate = 0

class Captivate(statusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST022',turns=2)
    show_name = '诱惑'
    skill_code = 'N052'
    skill_info = '♂诱惑♀或♀诱惑♂,从而大幅降低对手的特攻'

class Endeavor(damageSkill):
    def __init__(self):
        super(Endeavor, self).__init__(pp=5,fixed_damage=True,spell_skill=False)
    show_name = '蛮干'
    skill_code = 'N053'
    skill_info = '给予伤害,使对手的ＨＰ变得和自己的ＨＰ一样'

    def getDamage(self,obj_attack,obj_defense):
        if obj_attack.health >= obj_defense.health:
            return 0
        else:
            return obj_defense.health - obj_attack.health

class Rage(damageSkill):
    def __init__(self):
        super(Rage, self).__init__(pp=20,spell_skill=False)
    show_name = '愤怒'
    skill_code = 'N054'
    skill_power = 20
    skill_info = '如果在使出招式后受到攻击的话,会因愤怒的力量而提高攻击'

class HyperFang(damageSkill):
    def __init__(self):
        super(HyperFang, self).__init__(pp=15,hit_status='ST004',addition_status_rate=20,spell_skill=False)
    show_name = '必杀门牙'
    skill_code = 'N055'
    skill_power = 80
    hit_rate = 90
    skill_info = '用锋利的门牙牢牢地咬住对手进行攻击,有时会使对手畏缩'

class PayDay(damageSkill):
    def __init__(self):
        super(PayDay, self).__init__(pp=20,spell_skill=False,prize_efect=True)
    show_name = '聚宝盆'
    skill_code = 'N056'
    skill_power = 40
    skill_info = '向对手的身体投掷小金币进行攻击,战斗后可以拿到钱'

    def setPrize(self,pet):
        pet.reward_money = pet.level * 5

class SuperFang(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False,fixed_damage=True)
    show_name = '愤怒门牙'
    skill_code = 'N057'
    hit_rate = 90
    skill_info = '用锋利的门牙猛烈地咬住对手进行攻击,对手的ＨＰ减半'

    def getDamage(self,obj_attack,obj_defense):
        return round(obj_defense.health / 2)

class SwordsDance(GainStatusUpSkill):
    def __init__(self):
        super(SwordsDance, self).__init__(pp=20,status=['ST016'],turns=2)
    show_name = '剑舞'
    skill_code = 'N058'
    hit_rate = 0
    skill_info = '激烈地跳起战舞提高气势,大幅提高自己的攻击'

class PlayNice(statusSkill):
    def __init__(self):
        super(PlayNice, self).__init__(pp=20,status='ST021')
    show_name = '和睦相处'
    skill_code = 'N059'
    hit_rate = 0
    skill_info = '和对手和睦相处,使其失去战斗的气力,从而降低对手的攻击'

class Feint(damageSkill):
    def __init__(self):
        super(Feint, self).__init__(pp=20,spell_skill=False)
    show_name = '佯攻'
    skill_code = 'N060'
    skill_power = 30
    priority = 2
    skill_info = '能够攻击正在使用守住或看穿等招式的对手,解除其守护效果'#后续

class DoubleTeam(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=15,status=['ST027'])
    show_name = '影子分身'
    skill_code = 'N061'
    skill_info = '通过快速移动来制造分身,扰乱对手,从而提高闪避率'
    hit_rate = 0

class FurySwipes(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False)
    show_name = '乱抓'
    skill_code = 'N062'
    skill_power = 18
    hit_rate = 80
    skill_info = '用爪子或镰刀等抓对手进行攻击,连续攻击２～５次'
    multi_step = True

class CrushClaw(damageSkill):
    def __init__(self):
        super(CrushClaw, self).__init__(pp=10,hit_status='ST009',addition_status_rate=50,spell_skill=False)
    show_name = '撕裂爪'
    skill_code = 'N063'
    skill_power = 75
    hit_rate = 95
    skill_info = '用坚硬的锐爪劈开对手进行攻击,有时会降低对手的防御'

class ChipAway(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '逐步击破'
    skill_code = 'N064'
    skill_power = 70
    skill_info = '看准机会稳步攻击,无视对手的能力变化,直接给予伤害'

class BodySlam(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False,hit_status='ST002',addition_status_rate=30,addition_status='ST105')
    show_name = '泰山压顶'
    skill_code = 'N065'
    skill_power = 85
    skill_info = '用整个身体压住对手进行攻击,有时会让对手陷入麻痹状态'

class Thrash(DelayedSkill):
    def __init__(self):
        super(Thrash, self).__init__(pp=10,spell_skill=False,add_status_begin='ST117',
                                     add_status_end='ST006',delay_effect=False)
    show_name = '大闹一番'
    skill_code = 'N066'
    skill_power = 120
    skill_info = '在２～３回合内,乱打一气地攻击对手,大闹一番后自己会陷入混乱'

class DoubleSlap(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False)
    show_name = '连环巴掌'
    skill_code = 'N067'
    skill_power = 15
    hit_rate = 85
    multi_step = True
    skill_info = '用连环巴掌拍打对手进行攻击,连续攻击２～５次'

class Sing(statusSkill):
    def __init__(self):
        super().__init__(pp=15,status='ST003')
    show_name = '唱歌'
    skill_code = 'N068'
    hit_rate = 55
    skill_info = '让对手听舒适,美妙的歌声,从而陷入睡眠状态'

class Mimic(CopySkill):
    def __init__(self):
        super().__init__(pp=10)

    show_name = '模仿'
    skill_code = 'N070'
    hit_rate = 0
    skill_info = '可以将对手最后使用的招式,在战斗内变成自己的招式'

class Round(damageSkill):
    def __init__(self):
        super(Round, self).__init__(pp=15)
    show_name = '轮唱'
    skill_code = 'N071'
    skill_power = 60
    skill_info = '用歌声攻击对手,同伴还可以接着使出轮唱招式,威力也会提高' #后续

class HyperVoice(damageSkill):
    def __init__(self):
        super(HyperVoice, self).__init__(pp=10)
    show_name = '巨声'
    skill_code = 'N072'
    skill_power = 90
    skill_info = '给予对手又吵又响的巨大震动进行攻击'

class Foresight(statusSkill):
    def __init__(self):
        super(Foresight, self).__init__(pp=40,status='ST121')
    show_name = '识破'
    skill_code = 'N073'
    skill_info = '对幽灵属性宝可梦没有效果的招式以及闪避率高的对手,使用后变得能够打中'

class PsychUp(CopySkill):
    def __init__(self):
        super(PsychUp, self).__init__(pp=10,copy_skill_or_not=False)
    show_name = '自我暗示'
    skill_code = 'N074'
    skill_info = '取消自身能力的变化,并复制对手的能力变化'
    hit_rate = 0

class Ember(damageSkill):
    def __init__(self,pp=25):
        super().__init__(pp,hit_status='ST001',addition_status_rate=10)
    show_name = '火花'
    skill_code = 'A001'
    skill_power = 40
    property = 'fire'
    skill_info = '向对手发射小型火焰进行攻击,有时会让对手陷入灼伤状态'

class FireFang(MultipleDamageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status=['ST001','ST004'],addition_status_rate=10,spell_skill=False)
    show_name = '火焰牙'
    skill_code = 'A002'
    property = 'fire'
    hit_rate = 95
    skill_power = 65
    skill_info = '攻击目标造成伤害,有10%的几率使目标陷入灼伤/畏缩状态'

class FlameBurst(damageSkill):
    def __init__(self):
        super(FlameBurst, self).__init__(pp=15)
    show_name = '火焰溅射'
    skill_code = 'A003'
    property = 'fire'
    skill_power = 70
    skill_info = '爆裂的火焰会攻击到对手'

class Flamethrower(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST001',addition_status_rate=10)
    show_name = '喷射火焰'
    skill_code = 'A005'
    skill_power = 90
    skill_info = '火焰喷射，威力超绝,有10%的几率使对手进入灼伤状态'
    property = 'fire'

class fireSpin(damageSkill):
    def __init__(self,pp=15):
        super().__init__(pp,hit_status='ST010',addition_status_rate=100)
    show_name = '火焰漩涡'
    skill_code = 'A004'
    property = 'fire'
    skill_info = "持续性火焰伤害，每回合受到血量10%的伤害"
    skill_power = 35
    hit_rate = 85

class Inferno(damageSkill):
    def __init__(self):
        super().__init__(pp=5,hit_status='ST001',addition_status_rate=100)
    show_name = '炼狱'
    skill_code = 'A006'
    property = 'fire'
    skill_power = 100
    hit_rate = 50
    skill_info = '用烈焰包裹住对手进行攻击,让对手陷入灼伤状态'

class FlareBlitz(damageSkill):
    def __init__(self):
        super(FlareBlitz, self).__init__(pp=15,spell_skill=False,side_effect=True,
                                         hit_status='ST001',addition_status_rate=10,
                                         clean_status=['ST008'])
    show_name = '闪焰冲锋'
    skill_code = 'A007'
    property = 'fire'
    skill_power = 120
    skill_info = '让火焰覆盖全身猛撞向对手,自己也会受到不小的伤害,有时会让对手陷入灼伤状态'

    def getSideEffect(self,obj,damage):
        obj.health -= round(damage /3)
        print('%s 受到了 %s 的反弹伤害' % (obj.name,round(damage / 3 )))

class HeatWave(damageSkill):
    def __init__(self):
        super(HeatWave, self).__init__(pp=10,hit_status='ST001',addition_status_rate=10)
    show_name = '热风'
    skill_code = 'A008'
    skill_power = 95
    hit_rate = 90
    property = 'fire'
    skill_info = '将炎热的气息吹向对手进行攻击,有时会让对手陷入灼伤状态'

class WillOWisp(statusSkill):
    def __init__(self):
        super(WillOWisp, self).__init__(pp=15,status='ST001')
    show_name = '鬼火'
    skill_code = 'A009'
    property = 'fire'
    skill_info = '放出怪异的火焰,从而让对手陷入灼伤状态'
    hit_rate = 85

    def addStatus(self,obj,place):
        for prop in obj.prop:
            if prop in ['fire']:
                print("火属性pet 免疫")
                return True
        print("%s 陷入 灼伤状态"% obj.name)
        obj.setStatus(self.status)

class FireBlast(damageSkill):
    def __init__(self):
        super().__init__(pp=5,hit_status='ST001',addition_status_rate=10)
    show_name = '大字爆炎'
    skill_code = 'A010'
    skill_power = 110
    hit_rate = 85
    property = 'fire'
    skill_info = '大字形状的火焰烧尽对手,有时会让对手陷入灼伤状态'

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

class Absorb(damageSkill):
    def __init__(self,pp=25):
        super().__init__(pp,recover_by_damage=True,recover_per=0.5)

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

class MegaDrain(damageSkill):
    def __init__(self,pp=15):
        super().__init__(pp,recover_by_damage=True,recover_per=0.5)

    show_name = '超级吸取'
    skill_code = 'B008'
    property = 'wood'
    skill_info = "攻击目标造成伤害，自身的ＨＰ恢复“造成的伤害×50%"
    skill_power = 40

class GigaDrain(damageSkill):
    def __init__(self,pp=10):
        super().__init__(pp,recover_by_damage=True,recover_per=0.5)

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

class Aromatherapy(RecoverSkill):
    def __init__(self):
        super().__init__(pp=5,clean_status=statusmap.abnormal_list,recover_status=True)
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
        super().__init__(pp=5,self_effect=(['ST022'],2,100))
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

class LeechSeed(statusSkill):
    def __init__(self):
        super(LeechSeed, self).__init__(pp=10,status='ST111',need_user=True)
    show_name = '寄生种子'
    skill_info = '植入寄生种子后,将在每回合一点一点吸取对手的ＨＰ,从而用来回复自己的ＨＰ'
    property = 'wood'
    hit_rate = 90
    skill_code = 'B019'

class WorrySeed(statusSkill):
    def __init__(self):
        super(WorrySeed, self).__init__(pp=10,status='ST112')
    show_name = '烦恼种子'
    property = 'wood'
    skill_code = 'B020'
    skill_info = '种植心神不宁的种子,使对手不能入眠,并将特性变成不眠'

class Synthesis(RecoverSkill):
    def __init__(self):
        super().__init__(pp=5,weather_condition=True,recover_health=True)
    show_name = '光合作用'
    skill_code = 'B021'
    property = 'wood'
    hit_rate = 0
    skill_info = '回复自己的ＨＰ,根据天气的不同,回复量也会有所变化'

    def getIndexPer(self,weather):
        if weather in ['W001','W002']:
            return 0.66
        if weather in ['W003']:
            return 0.5
        if weather in ['W004','W005','W006','W007','W008']:
            return 0.25

class SeedBomb(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False)
    skill_code = 'B022'
    property = 'wood'
    skill_power = 80
    skill_name = '种子炸弹'
    skill_info = '将外壳坚硬的大种子,从上方砸下攻击对手'

class Spore(statusSkill):
    def __init__(self):
        super().__init__(pp=15,status='ST003')
    skill_code = 'B023'
    property = 'wood'
    skill_info = '沙沙沙地撒满具有催眠效果的孢子,从而让对手陷入睡眠状态'
    show_name = '蘑菇孢子'

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

    def getDamage(self,obj_attack,obj_defense):
        return round(obj_attack.level * random.randint(5,15) / 10 )

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

class Confusion(damageSkill):
    def __init__(self):
        super().__init__(pp=25,hit_status='ST006',addition_status_rate=10)
    show_name = '念力'
    skill_code = 'S008'
    skill_power = 50
    property = 'psychic'
    skill_info = '向对手发送微弱的念力进行攻击,有时会使对手混乱'

class Psybeam(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST006',addition_status_rate=10)
    show_name = '幻象光线'
    skill_code = 'S009'
    skill_power = 65
    property = 'psychic'
    skill_info = '向对手发射神奇的光线进行攻击,有时会使对手混乱'

class StoredPower(damageSkill):
    def __init__(self):
        super(StoredPower, self).__init__(pp=10,power_changed=True)
    show_name = '辅助力量'
    skill_code = 'S010'
    skill_power = 20
    property = 'psychic'
    skill_info = '用蓄积起来的力量攻击对手,自己的能力提高得越多,威力就越大'

    def getPower(self,obj_attack,obj_defense):
        sum = 1
        for status in ['ST016','ST017','ST018','ST019','ST020']:
            if status in obj_attack.status:
                sum += obj_attack.status[status]

        return self.skill_power * sum

class Extrasensory(damageSkill):
    def __init__(self):
        super(Extrasensory, self).__init__(pp=20,hit_status='ST004',addition_status_rate=10)
    show_name = '神通力'
    skill_code = 'S011'
    skill_power = 80
    property = 'psychic'
    skill_info = '发出看不见的神奇力量进行攻击,有时会使对手畏缩'

class Imprison(LockSkill):
    def __init__(self):
        super().__init__(pp=10,status='ST118',turns=1)
    show_name = '封印'
    skill_code = 'S012'
    property = 'psychic'
    skill_info = '如果对手有和自己相同的招式,那么只有对手无法使用该招式'
    hit_rate = 0

    def addStatus(self,pet,attack_pet):
        pet.setStatus(self.status)
        attack_pet_skilllist = []
        for key,skill in attack_pet.skill_list.items():
            attack_pet_skilllist.append(skill.skill_code)

        for key,skill in pet.skill_list.items():
            if skill.skill_code in attack_pet_skilllist:
                skill.lock = True

class Rest(RecoverSkill):
    def __init__(self):
        super(Rest, self).__init__(pp=10,recover_health=True,recover_status=True,
                                   clean_status=statusmap.abnormal_list,hit_status=['ST003'],
                                   turns=1,recover_per=1.0,max_recover_allowable=False)
    show_name = '睡觉'
    skill_code = 'S013'
    property = 'psychic'
    hit_rate = 0
    skill_info = '连续睡上２回合,回复自己的全部ＨＰ以及治愈所有异常状态'

class ZenHeadbut(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False,hit_status='ST004',addition_status_rate=20)
    show_name = '意念头锤'
    skill_code = 'S014'
    property = 'psychic'
    hit_rate = 90
    skill_power = 80
    skill_info = '将思念的力量集中在前额进行攻击,有时会使对手畏缩'

class Amnesia(GainStatusUpSkill):
    def __int__(self):
        super(Amnesia, self).__int__(pp=20,status=['ST019'],turns=2)
    show_name = '瞬间失忆'
    skill_code = 'S015'
    property = 'psychic'
    hit_rate = 0
    skill_info = '将头脑清空,瞬间忘记某事,从而大幅提高自己的特防'

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
        #obj.alive = False
    
class Flatter(MutlipleStatusSkill):
    def __init__(self):
        super(Flatter, self).__init__(pp=15,status=['ST006','ST018'])
    show_name = '吹捧'
    property = 'dark'
    skill_code = 'T010'
    skill_info = '吹捧对手,使其混乱,同时还会提高对手的特攻'

class Payback(damageSkill):
    def __init__(self):
        super(Payback, self).__init__(pp=10,spell_skill=False,addition_status='ST025')
    show_name = '以牙还牙'
    property = 'dark'
    skill_code = 'T011'
    skill_power = 50
    skill_info = '蓄力攻击,如果能在对手之后攻击,招式的威力会变成２倍' #后续功能能

class FeintAttack(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '出奇一击'
    property = 'dark'
    skill_code = 'T012'
    skill_power = 60
    hit_rate = 0
    skill_info = '悄悄地靠近对手,趁其不备进行殴打,攻击必定会命中'

class NastyPlot(GainStatusUpSkill):
    def __init__(self):
        super(NastyPlot, self).__init__(pp=20,status=['ST018'],turns=2)
    show_name = '诡计'
    property = 'dark'
    skill_code = 'T013'
    skill_info = '谋划诡计,激活头脑,大幅提高自己的特攻'
    hit_rate = 0

class SuckerPunch(damageSkill):
    def __init__(self):
        super(SuckerPunch, self).__init__(pp=5,spell_skill=False)
    show_name = '突袭'
    skill_code = 'T014'
    skill_power = 70
    skill_info = '可以比对手先攻击'
    property = 'dark'
    priority = 1

class NightSlash(damageSkill):
    def __init__(self):
        super(NightSlash, self).__init__(pp=15,lucky_level=2,spell_skill=False)
    show_name = '暗袭要害'
    skill_power = 70
    skill_code = 'T015'
    skill_info = '抓住瞬间的空隙切斩对手,容易击中要害'
    property = 'dark'

class Taunt(statusSkill):
    def __init__(self):
        super(Taunt, self).__init__(pp=20,status='ST122',turns=3)
    show_name = '挑衅'
    skill_code = 'T016'
    skill_info = '使对手愤怒,在３回合内让对手只能使出给予伤害的招式'
    property = 'dark'

class Megahorn(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False)
    skill_code = 'C001'
    show_name = '超级角击'
    skill_info = '用坚硬且华丽的角狠狠地刺入对手进行攻击'
    skill_power = 120
    hit_rate = 85
    property = 'insect'

class LeechLife(damageSkill):
    def __init__(self,pp=20):
        super().__init__(pp,spell_skill=False,recover_by_damage=True,recover_per=0.5)
    skill_code = 'C003'
    show_name = '吸血'
    skill_power = 80
    skill_info = "吸取对方,回复生命"
    property = 'insect'

class Steamroller(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST004',addition_status_rate=30,
                         addition_status='ST105',spell_skill=False)
    skill_code = 'C004'
    show_name = '疯狂滚压'
    skill_power = 65
    skill_info = '旋转揉成团的身体压扁对手,有时会使对手畏缩'
    property = 'insect'

class StringShot(statusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST023',turns=2)
    show_name = '吐丝'
    skill_code = 'C002'
    hit_rate = 95
    property = 'insect'
    skill_info = '用口中吐出的丝缠绕对手,从而大幅降低对手的速度'

class BugBite(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False,berry_effect=True)
    show_name = '虫咬'
    skill_code = 'C005'
    skill_power = 60
    property = 'insect'
    skill_info = '咬住进行攻击,当对手携带树果时,可以食用并获得其效'

    def eatBerry(self,obj_attack,obj_defense):
        if obj_defense.berry:
            obj_defense.berry.berryEffect(obj_attack)
            obj_defense.berry = None

class SilverWind(damageSkill):
    def __init__(self):
        super().__init__(pp=5,self_effect=(['ST016','ST017','ST018','ST019','ST020'],1,10))
    show_name = '银色旋风'
    skill_code = 'C006'
    skill_power = 60
    property = 'insect'
    skill_info = '在风中掺入鳞粉攻击对手,有时会提高自己的全部能力'

class BugBuzz(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status='ST011',addition_status_rate=10)
    show_name = '虫鸣'
    skill_code = 'C007'
    skill_power = 90
    property = 'insect'
    skill_info = '利用振动发出音波进行攻击,有时会降低对手的特防'

class QuiverDance(GainStatusUpSkill):
    def __init__(self):
        super(QuiverDance, self).__init__(pp=20,status=['ST018','ST019','ST020'])
    show_name = '蝶舞'
    skill_code = 'C008'
    hit_rate = 0
    property = 'insect'
    skill_info = '轻巧地跳起神秘而又美丽的舞蹈,提高自己的特攻,特防和速度'

class Twineedle(damageSkill):
    def __init__(self):
        super().__init__(pp=20,hit_status='ST007',addition_status_rate=20,spell_skill=False)
    show_name = '双针'
    skill_code = 'C009'
    property = 'insect'
    skill_power = 25
    skill_info = '将２根针刺入对手,连续２次给予伤害,有时会让对手陷入中毒状态'
    multi_step = True

    def getStepOfSkill(self):
        return 2

class PinMissile(damageSkill):
    def __init__(self):
        super(PinMissile, self).__init__(pp=20,spell_skill=False)
    show_name = '飞弹针'
    skill_code = 'C010'
    property = 'insect'
    skill_power = 25
    hit_rate = 95
    multi_step = True
    skill_info = '向对手发射锐针进行攻击,连续攻击２～５次'

class FellStinger(damageSkill):
    def __init__(self):
        super().__init__(pp=25,spell_skill=False,self_effect=('ST016',3,100))
    show_name = '致命针刺'
    skill_power = 50
    property = 'insect'
    skill_code = 'C011'
    skill_info = '如果使用此招式打倒对手,攻击会巨幅提高'

    def selfSideEffect(self,obj_attack,obj_defense,damage):
        if obj_defense.health - damage <= 0:
            if rancom.statusRandom(self.self_effect[2]):
                obj_attack.setStatus(self.self_effect[0], self.self_effect[1])

class FuryCutter(damageSkill):
    def __init__(self):
        super().__init__(pp=20,side_effect=True,spell_skill=False,power_changed=True)
    show_name = '连斩'
    skill_power = 40
    property = 'insect'
    skill_code = 'C012'
    skill_info = '用镰刀或爪子等切斩对手进行攻击,连续击中,威力就会提高'
    hit_rate = 95

    def getPower(self,obj_attack,obj_defense):
        if 'ST115' in obj_attack.status:
            power = self.skill_power + self.skill_power * obj_attack.status['ST115']
            if power > 160:
                power = 160
            return power
        else:
            return self.skill_power

    def getSideEffect(self,obj,damage):
        if 'ST115' not in obj.status:
            obj.setStatus('ST115')
        else:
            obj.status['ST115'] += 1

class XScissor(damageSkill):
    def __init__(self):
        super(XScissor, self).__init__(pp=15,spell_skill=False)
    show_name = '十字剪'
    skill_code = 'C013'
    skill_power = 80
    skill_info = '将镰刀或爪子像剪刀般地交叉,顺势劈开对手'
    property = 'insect'

class SignalBeam(damageSkill):
    def __init__(self):
        super(SignalBeam, self).__init__(pp=15,hit_status='ST006',addition_status_rate=10)
    show_name = '信号光束'
    skill_code = 'C014'
    skill_power = 75
    property = 'insect'
    skill_info = '发射神奇的光线进行攻击,有时会使对手混乱'

class Haze(RecoverSkill):
    def __init__(self):
        super().__init__(pp=5,recover_status=True,clean_status=statusmap.all_status_list,
                         remove_status=statusmap.all_status_list)
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

class Withdraw(GainStatusUpSkill):
    def __init__(self):
        super(Withdraw, self).__init__(pp=40,status=['ST017'])
    show_name = '缩入壳中'
    skill_info = '缩入壳里保护身体,从而提高自己的防御'
    property = 'water'
    skill_code = 'D012'
    hit_rate = 0

class AquaTail(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False)
    skill_code = 'D013'
    skill_power = 90
    hit_rate = 90
    show_name = '水流尾'
    property = 'water'
    skill_info = '如惊涛骇浪般挥动大尾巴攻击对手'

class RainDance(PlaceStatusSkill):
    def __init__(self):
        super().__init__(pp=5,status='ST036')
    skill_code = 'D014'
    hit_rate = 0
    show_name = '求雨'
    property = 'water'
    skill_info = '在５回合内一直降雨,从而提高水属性的招式威力,火属性的招式威力则降低'

class AquaJet(damageSkill):
    def __init__(self):
        super(AquaJet, self).__init__(pp=20)
    skill_code = 'D015'
    show_name = '水流喷射'
    property = 'water'
    skill_power = 40
    skill_info = '以迅雷不及掩耳之势扑向对手,必定能够先制攻击'

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

    def getPower(self,pet):
        power = 30 * pow(2,(self.hit_count - 1))
        if 'ST110' in pet.status:
            power *= 2
        return power

class SmackDown(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False,clean_status=['ST107'],hit_status='ST109',addition_status_rate=100)
    show_name = '击落'
    skill_code = 'R006'
    skill_info = '扔石头或炮弹攻击飞行的对手,对手会被击落,掉到地面'
    property = 'rock'
    skill_power = 50

class StoneEdge(damageSkill):
    def __init__(self):
        super(StoneEdge, self).__init__(pp=5,spell_skill=False,lucky_level=2)
    show_name = '尖石攻击'
    skill_code = 'R007'
    property = 'rock'
    skill_power = 100
    hit_rate = 80
    skill_info = '用尖尖的岩石刺入对手进行攻击,容易击中要'

class RockBlast(damageSkill):
    def __init__(self):
        super().__init__(pp=20,spell_skill=False)
    show_name = '岩石爆击'
    skill_info = '向对手发射坚硬的岩石进行攻击,连续攻击２～５次'
    skill_power = 25
    hit_rate = 90
    skill_code = 'R008'
    multi_step = True
    property = 'rock'

class StealthRock(statusSkill):
    def __init__(self):
        super().__init__(pp=20,status='ST025')
    show_name = '隐形岩'
    hit_rate = 0
    skill_code = 'R009'
    skill_info = '将无数岩石悬浮在对手的周围,易受伤'
    property = 'rock'

class Sandstorm(PlaceStatusSkill):
    def __init__(self):
        super().__init__(pp=10,weather='W004',weather_change=True)
    show_name = '沙暴'
    hit_rate = 0
    skill_code = 'R010'
    property = 'rock'
    skill_info = '在５回合内扬起沙暴'

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

class SandTomb(damageSkill):
    def __init__(self):
        super(SandTomb, self).__init__(pp=15,spell_skill=False,hit_status='ST010',addition_status_rate=100)
    show_name = '流沙地狱'
    skill_code = 'E009'
    skill_power = 35
    hit_rate = 85
    property = 'ground'
    skill_info = '将对手困在铺天盖地的沙暴中,在４～５回合内进行攻击'

class Dig(DelayedSkill):
    def __init__(self):
        super(Dig, self).__init__(pp=10,spell_skill=True,add_status_begin='ST116')
    show_name = '挖洞'
    skill_power = 80
    skill_code = 'E010'
    property = 'ground'
    skill_info = '第１回合钻入,第２回合攻击对手'

class EarthPower(damageSkill):
    def __init__(self):
        super(EarthPower, self).__init__(pp=10,hit_status='ST011',addition_status_rate=10)
    show_name = '大地之力'
    skill_power = 90
    skill_code = 'E011'
    property = 'ground'
    skill_info = '向对手脚下释放出大地之力,有时会降低对手的特防'

class Fissure(damageSkill):
    def __init__(self):
        super().__init__(pp=5,spell_skill=False,one_hit_kill=True)
    show_name = '地裂'
    skill_code = 'E012'
    property = 'ground'
    skill_info = '让对手掉落于地裂的裂缝中进行攻击,只要命中就会一击濒死'

class Rototiller(GainStatusUpSkill):
    def __init__(self):
        super(Rototiller, self).__init__(pp=10,status=['ST016','ST018'])
    show_name = '耕地'
    skill_code = 'E013'
    property = 'ground'
    skill_info = '翻耕土地,使草木更容易成长,会提高草属性宝可梦的攻击和特攻'

    def addStatus(self, obj, place, double=1):
        for status in self.status:
            if 'wood' in obj.prop and 'ST116' not in obj.status and 'ST024' not in obj.status:
                if talentmap.addStatusOrNot(obj, status, place):
                    obj.setStatus(status, self.turns * double)
                    print("%s 陷入 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))
                else:
                    print("%s 免疫 %s 状态 ！" % (obj.name, statusmap.status_dict[status].status_show_name))


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

class ShadowClaw(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False,lucky_level=2)
    show_name = '暗影爪'
    skill_code = 'Q004'
    skill_power = 70
    skill_info = '以影子做成的锐爪,劈开对手,容易击中要害'
    property = 'ghost'

class Grudge(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=5,status=['ST119'],turns=2)
    show_name = '怨念'
    skill_code = 'Q005'
    skill_info = '因对手的招式而陷入濒死时给对手施加怨念,让该招式的ＰＰ变成０'
    property = 'ghost'
    hit_rate = 0

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

class CrossPoison(damageSkill):
    def __init__(self):
        super(CrossPoison, self).__init__(pp=20,hit_status='ST007',addition_status_rate=10,spell_skill=False,lucky_level=2)
    property = 'poison'
    show_name = '十字毒刃'
    skill_power = 70
    skill_code = 'P020'
    skill_info = '用毒刃劈开对手,有时会让对手陷入中毒状态,也容易击中要害'

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

class Nuzzle(damageSkill):
    def __init__(self):
        super(Nuzzle, self).__init__(pp=20,hit_status='ST002',addition_status_rate=100,spell_skill=False)
    show_name = '蹭蹭脸颊'
    skill_power = 20
    property = 'electric'
    skill_code = 'H010'
    skill_info = '将带电的脸颊蹭蹭对手进行攻击,让对手陷入麻痹状态'

class Thunderbolt(damageSkill):
    def __init__(self):
        super(Thunderbolt, self).__init__(pp=15,hit_status='ST002',addition_status_rate=10)
    show_name = '十万伏特'
    skill_power = 90
    property = 'electric'
    skill_code = 'H011'
    skill_info = '向对手发出强力电击进行攻击,有时会让对手陷入麻痹状态'

class WildCharge(damageSkill):
    def __init__(self):
        super().__init__(pp=15,side_effect=True,spell_skill=False)
    show_name = '疯狂伏特'
    skill_power = 90
    skill_code = 'H012'
    property = 'electric'
    skill_info = '让电流覆盖全身撞向对手进行攻击,自己也会受到少许伤害'

    def getSideEffect(self,obj,damage):
        obj.health -= round(damage / 4)
        print("%s 受到了 %s 反弹伤害" % (obj.name, round(damage / 3)))

class Thunder(damageSkill):
    def __init__(self):
        super().__init__(pp=10,hit_status='ST002',addition_status_rate=30)
    show_name = '打雷'
    skill_power = 110
    skill_code = 'H013'
    hit_rate = 70
    property = 'electric'
    skill_info = '向对手劈下暴雷进行攻击,有时会让对手陷入麻痹状'

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

class DragonRage(damageSkill):
    def __init__(self):
        super(DragonRage, self).__init__(pp=10,fixed_damage=True)
    show_name = '龙之怒'
    skill_code = 'G004'
    property = 'dragon'
    skill_info = '将愤怒的冲击波撞向对手进行攻击,必定会给予４０的伤害'

    def getDamage(self,obj_attack,obj_defense):
        return 40

class DragonClaw(damageSkill):
    def __init__(self):
        super().__init__(pp=15,spell_skill=False)
    show_name = '龙爪'
    skill_code = 'G005'
    property = 'dragon'
    skill_power = 80
    skill_info = '用尖锐的巨爪劈开对手进行攻击'

class Moonlight(RecoverSkill):
    def __init__(self):
        super().__init__(pp=5,weather_condition=True,recover_health=True)

    show_name = '月光'
    skill_code = 'Y001'
    property = 'fairy'
    skill_info = '月光恢复使用者的ＨＰ值。恢复量由当前天气决定'

    def getIndexPer(self,weather):
        if weather in ['W001','W002']:
            return 0.66
        if weather in ['W003']:
            return 0.5
        if weather in ['W004','W005','W006','W007','W008']:
            return 0.25

class Moonblast(damageSkill):
    def __init__(self):
        super().__init__(pp=15,hit_status='ST021',addition_status_rate=30)

    show_name = '月亮之力'
    skill_code = 'Y002'
    property = 'fairy'
    skill_info = '攻击目标造成伤害,30%几率令目标的特攻降低1级'
    skill_power = 95
    
class DisarmingVoice(damageSkill):
    def __init__(self):
        super(DisarmingVoice, self).__init__(pp=15)
    show_name = '魅惑之声'
    skill_power = 40
    property = 'fairy'
    skill_code = 'Y003'
    skill_info = '发出魅惑的叫声,给予对手精神上的伤害,攻击必定会命中'
    hit_rate = 0

class BabyDollEyes(statusSkill):
    def __init__(self):
        super(BabyDollEyes, self).__init__(status='ST021')
    show_name = '圆瞳'
    skill_code = 'Y004'
    property = 'fairy'
    priority = 1
    skill_info = '用圆瞳凝视对手,从而降低其攻击,必定能够先制攻击。'

class PlayRough(damageSkill):
    def __init__(self):
        super(PlayRough, self).__init__(pp=10,spell_skill=False,hit_status='ST021',addition_status_rate=10)
    show_name = '嬉闹'
    skill_code = 'Y005'
    property = 'fairy'
    skill_power = 90
    hit_rate = 90
    skill_info = '与对手嬉闹并攻击,有时会降低对手的攻击'

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

class IronDefense(GainStatusUpSkill):
    def __init__(self):
        super().__init__(pp=15,status=['ST017'],turns=2)
    show_name = '铁壁'
    skill_code = 'X006'
    skill_info = '将皮肤变得坚硬如铁,从而大幅提高自己的防御'
    property = 'steel'

class MeteorMash(damageSkill):
    def __init__(self):
        super(MeteorMash, self).__init__(pp=10,self_effect=(['ST016'],1,20),spell_skill=False)
    show_name = '彗星拳'
    skill_power = 90
    hit_rate = 90
    skill_code = 'X007'
    property = 'steel'
    skill_info = '使出彗星般的拳头攻击对手,有时会提高自己的攻击'

class DoubleKick(damageSkill):
    def __init__(self):
        super(DoubleKick, self).__init__(spell_skill=False)
    show_name = '二连踢'
    skill_code = 'Z001'
    property = 'combat'
    skill_power = 30
    skill_info = '用２只脚踢飞对手进行攻击,连续２次给予伤害'
    multi_step = True

    def getStepOfSkill(self):
        return 2

class Superpower(damageSkill):
    def __init__(self):
        super(Superpower, self).__init__(pp=5,side_effect=True,spell_skill=False)
    show_name = '蛮力'
    skill_code = 'Z002'
    property = 'combat'
    skill_power = 120
    skill_info = '发挥惊人的力量攻击对手,自己的攻击和防御会降低'

    def getSideEffect(self,obj,damage):
        if 'ST021' not in obj.status:
            obj.setStatus('ST021')
        if 'ST009' not in obj.status:
            obj.setStatus('ST009')

class WakeUpSlap(damageSkill):
    def __init__(self):
        super().__init__(pp=10,spell_skill=False,remove_status=['ST003'],addition_status='ST003')
    show_name = '唤醒巴掌'
    skill_code = 'Z003'
    property = 'combat'
    skill_power = 70
    skill_info = '给予睡眠状态下的对手较大的伤害,但相反对手会从睡眠中醒过来'