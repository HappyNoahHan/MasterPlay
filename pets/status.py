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
    status_show_name = '锁定'
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







