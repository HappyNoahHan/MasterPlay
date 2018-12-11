from assist import rancom

class Status(object):
    status_show_name = '未知'
    def __str__(self):
        return self.status_show_name


class Cauma(Status):
    status_show_name = '灼烧'
    status_code = 'ST001'
    status_info = '受到火属性伤害加成20%'
    index_per = 1.2

    def statusEffect(self,skill,damage):
        if skill.property == 'fire':
            return int(damage * self.index_per)

class Paralysis(Status):
    status_show_name = '麻痹'
    status_code = 'ST002'
    status_info = '麻痹，有一定的几率无法使用技能'
    rate = 30

    def statusEffect(self):
        if rancom.statusRandom(self.rate):
            return True
        else:
            return False
