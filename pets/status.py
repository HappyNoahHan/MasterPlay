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
