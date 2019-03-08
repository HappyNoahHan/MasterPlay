from assist import rancom

class Status(object):
    status_show_name = '未知'
    rate = 25
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
    status_show_name = '吹飞'
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
            return round(skill.skill_power * 0.5)
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

