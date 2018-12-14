'''
    prop_type   basci 基础能力 六维   skill 技能威力   restore 一次性救命道具
                debuff 闪避类  hit 命中类
'''

from props import propmap


class Prop(object):
    prop_show_name = '道具'
    info = '可携带道具'

    def __str__(self):
        return self.info

    def removeProp(self,obj):
        print("%s 卸下了 %s " % (obj.name,self.prop_show_name))
        obj.carry_prop = None
    def equipProp(self,obj):
        print("%s 装备了 %s " % (obj.name,self.prop_show_name))
        obj.carry_prop = propmap.prop_dict[self.prop_show_name]


class PropertyUpProp(Prop):
    def __init__(self,per = 0.3,up_type = 'attack',prop_show_name = ''):
        self.info = '属性提升道具'
        self.per = per
        self.up_type = up_type
        self.prop_type = 'basic'
        self.prop_show_name = prop_show_name

    def propCarry(self,value):
        #print(value * self.per)
        return  int(value * self.per)

class SkillPowerUpProp(Prop):
    def __init__(self,pety='normal',power = 20,prop_show_name = ''):
        self.info = '技能威力提高道具'
        self.prop_type = 'skill'
        self.pety = pety #属性
        self.power = power
        self.prop_show_name = prop_show_name

    def propCarry(self,skill):
        if self.pety == 'all':
            return self.power
        if self.pety == skill.property:
            return self.power
        else:
            return 0

class SkillHitUpProp(Prop):
    def __init__(self,hit_up=10,prop_show_name = ''):
        self.info = '技能命中提高道具'
        self.prop_type = 'hit'
        self.hit_up = hit_up
        self.prop_show_name = prop_show_name

    def propCarry(self):
        return self.hit_up
