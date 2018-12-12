'''
    prop_type   basci 基础能力 六维   skill 技能威力   restore 一次性救命道具
                debuff 闪避类
'''

import  assist.ppvalue
from assist import life
from pets import statusmap
from battle import buff


class Prop(object):
    prop_show_name = '道具'
    info = '可携带道具'

    def __str__(self):
        return self.info


class PropertyUpProp(Prop):
    def __init__(self,per = 1.1,up_type = 'attack'):
        self.info = '属性提升道具'
        self.per = per
        self.up_type = up_type
        self.prop_type = 'basic'

    def propCarry(self,value):
        return  int(value * self.per)
