from assist import rancom

class Status(object):
    status_show_name = '未知'
    rate = 25
    status_giver = None
    def __str__(self):
        return self.status_show_name


    def statusEffect(self):
        if rancom.statusRandom(self.rate):
            return True
        else:
            return False

class Cauma(Status):
    status_show_name = '灼伤'
    status_code = 'ST001'
    status_info = '每回合受到最大Hp值/16的伤害'

    def statusEffect(self,health):
        return round(health / 16)

class Paralysis(Status):
    '''
    麻痹状态只影响技能的会心等级计算时的速度 有1/4的几率使用技能失败
    '''
    status_show_name = '麻痹'
    status_code = 'ST002'
    status_info = '麻痹，有一定的几率无法使用技能'
    rate = 25


class Sleeping(Status):
    status_show_name = '睡眠'
    status_code = 'ST003'
    status_info = '睡眠，有一定的几率自我清醒'

class Shrink(Status):
    status_show_name = '畏缩'
    status_code = 'ST004'
    status_info = '精灵畏缩不前,没有做出任何动作'
    rate = 10

class BigPoisoning(Status):
    status_show_name = '剧毒'
    status_code = 'ST005'
    status_info = '陷入剧毒状态,每回合收到的伤害更重'

    def statusEffect(self,turns,health):
        if turns >= 16:
            turns = 15
        return round(health * turns / 16)

class Poisoning(Status):
    status_show_name = '中毒'
    status_code = 'ST007'
    status_info = '陷入中毒状态,每回合受到HP/8的伤害'

    def statusEffect(self,health):
        return round(health / 8)

class Lock(Status):
    status_show_name = '盯住'
    status_code = 'ST099'
    status_info = '被锁定,无法逃脱'

class NoTalent(Status):
    status_show_name = '无天赋'
    status_code = 'ST100'
    status_info = '天赋失效'

class Whirlwind(Status):
    status_show_name = '畏惧'
    status_code = 'ST101'
    status_info = '吹跑精灵'

class Chaos(Status):
    status_show_name = '混乱'
    status_code = 'ST006'
    status_info = '混乱,有一定的几率以威力40的无属性攻击自己,持续2~5回合'
    rate = 33

class Frozen(Status):
    status_show_name = '冰冻'
    status_code = 'ST008'
    status_info = '冰冻,有一定的几率自我清醒,无法使用技能'

class ArmorBreak(Status):
    status_show_name = '破甲'
    status_code = 'ST009'
    status_info = '破甲,使对方防御降低'

    def statusEffect(self,defense,turns):
        return round(defense *(1 - 0.1 * turns))

class Bound(Status):
    status_show_name = '束缚'
    status_code = 'ST010'
    status_info = '束缚状态持续4~5回合,处于束缚状态的宝可梦无法替换或逃走,' \
                  '处于束缚状态的宝可梦每回合结束时损失1⁄8的最大ＨＰ.'

    def statusEffect(self,health):
        return round(health / 8 )

class GuardBreak(Status):
    status_show_name = '破防'
    status_code = 'ST011'
    status_info = '破防,使对方特防降低'

    def statusEffect(self,spell_defense,turns):
        return round(spell_defense * (1 - 0.1 * turns))

class PowerSave(Status):
    status_show_name = '蓄力'
    status_code = 'ST012'
    status_info = '防御,特防提升一级'

    def statusEffect(self,defense,spell_defense):
        return round(defense * 1.1),round(spell_defense * 1.1)

class HitDown(Status):
    status_show_name = '命中降低'
    status_code = 'ST013'
    status_info = '技能命中降低'

    def statusEffect(self,hit_rate,turns):
        print("命中降低 %s 层" % turns)
        return round(hit_rate * (1 - 0.1 * turns))

class Satiate(Status):
    status_show_name = '吃饱'
    status_code = 'ST014'
    status_info = '吃饱状态,吃树果进入该状态'

class PropUp(Status):
    def __init__(self,status_show_name=None,status_info=None,status_code=None):
        self.status_show_name = status_show_name
        self.status_info = status_info
        self.status_code = status_code

    def statusEffect(self,value,turns):
        #print("命中提高 %s 层" % turns)
        return round(value * (1 + 0.1 * turns))

class PropDown(Status):
    def __init__(self,status_show_name=None,status_info=None,status_code=None):
        self.status_show_name = status_show_name
        self.status_info = status_info
        self.status_code = status_code

    def statusEffect(self,value,turns):
        #print("命中提高 %s 层" % turns)
        return round(value * (1 - 0.1 * turns))

class Fly(Status):
    status_show_name = '飞翔'
    status_info = '飞上天空'
    status_code = 'ST024'

class Vulnerability(Status):
    status_show_name = '易受伤'
    status_info = '容易伤害'
    status_code = 'ST025'

class LuckyUp(Status):
    status_show_name = '易击要害'
    status_info = '容易击中要害,lucky_level +2'
    status_code = 'ST026'

class DodgeUp(Status):
    status_show_name = '闪避提高'
    status_info = '使用者闪避能力提高'
    status_code = 'ST027'

    def statusEffect(self,value,turns):
        return value + turns


class DodgeDown(Status):
    status_show_name = '闪避降低'
    status_info = '使用者闪避能力降低'
    status_code = 'ST028'

    def statusEffect(self,value,turns):
        return value - turns

class HealBlock(Status):
    status_show_name = '回复封锁'
    status_info = '无法恢复生命值5回合'
    status_code = 'ST029'

class NoLucky(Status):
    status_show_name = '幸运咒语'
    status_info = '5回合内无法被击中要害'
    status_code = 'ST030'

class Place(Status):
    def __init__(self,status_code=None,status_show_name=None,status_info=None,place_property='normal',place_type = None):
        self.status_code = status_code
        self.status_show_name = status_show_name
        self.status_info = status_info
        self.place_property = place_property
        self.place_type = place_type

    def statusEffect(self,skill,power):
        '''
        技能属性与场地属性一致 威力加强50%
        :param skill:
        :param power:
        :return:
        '''
        if skill.property == self.place_property:
            return round(power * 1.5)
        return power

class PetalDance(Status):
    status_show_name = '花瓣舞'
    status_info = '花瓣舞状态里,2-3回合使用花瓣舞攻击'
    status_code = 'ST102'

    def statusEffect(self,turns):
        if turns == 1:
            if rancom.statusRandom(50):
                return True
            return False
        elif turns > 1:
            return True
        else:
            return False

class Rollout(Status):
    status_show_name = '滚动'
    status_info = '在５回合内连续滚动攻击对手,招式每次击中,威力就会提高'
    status_code = 'ST108'

    def statusEffect(self,turns):
        if turns > 3:
            return False
        return True

class SolarBeam(Status):
    status_show_name = '日光束'
    status_info = '蓄力攻击,第二回合攻击'
    status_code = 'ST103'

class KnockOff(Status):
    status_show_name = '拍落'
    status_info = '携带物视为不带'
    status_code = 'ST098'

class ChangePro(Status):
    status_show_name = '属性转变'
    status_info = '使用者属性变为对方属性'
    status_code = 'ST097'

class WaterSport(Place):
    def statusEffect(self,skill,power):
        if skill.property == 'fire':
            return round(power * 0.5)
        return power

class MudSport(Place):
    def statusEffect(self,skill,power):
        if skill.property == 'electric':
            return round(power * 0.5)
        return power

class AquaRing(Status):
    status_show_name = '水流环'
    status_info = '在自己身体的周围覆盖用水制造的幕,每回合回复ＨＰ'
    status_code = 'ST096'

class Lockon(Status):
    status_show_name = '锁定'
    status_info = '在锁定的下一回合,招式必定会击中'
    status_code = 'ST104'

class PropChangeTemp(Status):
    def __init__(self,status_show_name,status_info,status_code,change_prop):
        self.status_show_name = status_show_name
        self.status_info = status_info
        self.status_code = status_code
        self.change_prop = change_prop

class Minimize(Status):
    status_show_name = '变小'
    status_info = '状态变化~变小'
    status_code = 'ST105'

class LightScreen(Place):
    def statusEffect(self,skill):
        if skill.spell_skill == True:
            return True
        else:
            return False

class Disable(Status):
    status_show_name = '定身法'
    status_info = '定身法状态持续4个回合,处于定身法状态的宝可梦不能使用在进入定身法状态前最后使用的招式'
    status_code = 'ST106'

class MagnetRise(Status):
    status_show_name = '电磁飘浮'
    status_info = '电磁飘浮状态的宝可梦免疫地面属性招式'
    status_code = 'ST107'

class SmackDown(Status):
    status_show_name = '击落'
    status_info = '拍落到地面'
    status_code = 'ST109'

class DefenseCurl(Status):
    status_show_name = '变圆'
    status_info = '冰球和滚动进行攻击，威力将加倍'
    status_code = 'ST110'

class LeechSeed(Status):
    status_show_name = '寄生种子'
    status_code = 'ST111'
    status_info = '每回合结束时,会被寄生种子夺走ＨＰ,同时回复对手的ＨＰ'

    def statusEffect(self,health):
        return round(health / 8)

class WorrySeed(Status):
    status_show_name = '烦恼种子'
    status_code = 'ST112'
    status_info = '不会睡眠'

class SkullBash(Status):
    status_show_name = '火箭头锤'
    status_info = '蓄力攻击,第二回合攻击'
    status_code = 'ST113'

class RainDance(Place):
    def statusEffect(self,skill,power):
        if skill.property == 'fire':
            return round(power * 0.5)
        if skill.property == 'water':
            return round(power * 1.5)
        return power

class Safeguard(Status):
    status_show_name = '神秘守护'
    status_info = '在５回合内,不会陷入异常状态'
    status_code = 'ST114'

class FuryCutter(Status):
    status_show_name = '连斩'
    status_info = '连斩效果'
    status_code = 'ST115'

class Dig(Status):
    status_show_name = '挖洞'
    status_info = '第１回合钻入,第２回合攻击对手'
    status_code = 'ST116'

class Thrash(Status):
    status_show_name = '大闹一番'
    status_info = '在２～３回合内,乱打一气地攻击对手,大闹一番后自己会陷入混乱'
    status_code = 'ST117'

    def statusEffect(self,turns):
        if turns == 1:
            if rancom.statusRandom(50):
                return True
            return False
        elif turns > 1:
            return True
        else:
            return False

class Imprison(Status):
    status_show_name = '封印'
    status_info = '宝可梦使出封印后,其所学会的招式,对手的宝可梦将无法使出'
    status_code = 'ST118'

class Grudge(Status):
    status_show_name = '怨念'
    status_info = '因对手的招式而濒死时,该招式的ＰＰ会变为０'
    status_code = 'ST119'

class Tailwind(Status):
    status_show_name = '顺风'
    status_info = '速度加倍,持续时间为4回合'
    status_code = 'ST120'

class Identified(Status):
    status_show_name = '被识破'
    status_info = '躲避无效'
    status_code = 'ST121'

class Taunt(Status):
    status_show_name = '挑衅'
    status_info = '变得只能使出给予伤害的招式'
    status_code = 'ST122'