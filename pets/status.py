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

class Chaos(Status):
    status_show_name = '混乱'
    status_code = 'ST006'
    status_info = '混乱,有一定的几率以威力40的无属性攻击自己,持续2~5回合'
    rate = 33




