from assist import rancom

class Status(object):
    status_show_name = '未知'
    rate = 30
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
    status_info = '受到火属性伤害加成20%'
    index_per = 1.2

    def statusEffect(self,skill,damage):
        if skill.property == 'fire':
            return int(damage * self.index_per)
        return damage

class Paralysis(Status):
    status_show_name = '麻痹'
    status_code = 'ST002'
    status_info = '麻痹，有一定的几率无法使用技能'


class Sleeping(Status):
    status_show_name = '睡眠'
    status_code = 'ST003'
    status_info = '睡眠，有一定的几率自我清醒'

class Shrink(Status):
    status_show_name = '畏缩'
    status_code = 'ST004'
    status_info = '精灵畏缩不前,没有做出任何动作'
    rate = 10


