'''
    2.0 法强  法防  结算方式改变
    3.0 经验值
    3.1 pet init 改造 基础能力值
    3.2 升级属性提升  后续版本个体值
    3.21 随机1-31 基础点数
    3.3 特性 eg：猛火
    3.4 状态 eg：灼伤
'''

import battle.skill
from assist import cap,rancom

import random

class Pet(object):
    #能力值 每个精灵属性皆不同
    health_basic = 1
    attack_basic = 1
    defense_basic = 1
    spell_power_basic = 1
    spell_defense_basic = 1
    speed_basic = 1

    #初始化函数
    def __init__(self,level=1,skill_list={},exp_for_current=0,realize_skill_list=[],
                 status=[],carry_prop=None,indi_list=rancom.getIndiValue()):
        self.level = level
        [self.health_indi,
            self.attack_indi,
            self.defense_indi,
            self.spell_power_indi,
            self.spell_defense_indi,
            self.speed_indi] = indi_list
        self.health = cap.gethpCapValue(self.health_basic,self.level,self.health_indi)
        self.attack = cap.getCapValue(self.attack_basic,self.level,self.attack_indi)
        self.defense = cap.getCapValue(self.defense_basic,self.level,self.defense_indi)
        self.spell_power = cap.getCapValue(self.spell_power_basic,self.level,self.spell_power_indi)
        self.spell_defense = cap.getCapValue(self.spell_defense_basic,self.level,self.spell_defense_indi)
        self.speed = cap.getCapValue(self.speed_basic,self.level,self.speed_indi)
        self._max_health = self.health
        #buff提升的能力属性
        self.tmp_attack = 0
        self.tmp_defense = 0
        self.tmp_spell_power = 0
        self.tmp_spell_defense = 0
        self.tmp_speed = 0
        #属性道具提升的能力属性
        self.prop_attack_up = 0
        self.prop_defense_up = 0
        self.prop_spell_power_up = 0
        self.prop_spell_defense_up = 0
        self.prop_speed_up = 0
        self.debuff_dict = {}
        self.buff_dict = {}
        self.property_buff = {}
        #以下是进化时需要继承的选线
        self.skill_list = skill_list
        self.exp_for_current = exp_for_current
        self.realize_skill_list = realize_skill_list #已经领悟的技能表
        self.status = status #状态表
        self.carry_prop = carry_prop

    autoAi = False
    canEvolve = True


    def getDefense(self):
        return self.defense + self.tmp_defense + self.prop_defense_up

    def getAttack(self):
        return self.attack + self.tmp_attack + self.prop_attack_up

    def getSpellPower(self):
        return self.spell_power + self.tmp_spell_power + self.prop_spell_power_up

    def getSpellDefense(self):
        return self.spell_defense + self.tmp_spell_defense + self.prop_spell_defense_up

    def getSpeed(self):
        return self.speed + self.tmp_speed + self.prop_speed_up

    def setSkills(self,key,value):
        self.skill_list[key] = value

    def setDebuff(self,key,value):
        self.debuff_dict[key] = value

    def setBuff(self,key,value):
        self.buff_dict[key] = value

    def removeBuff(self,key):
        self.buff_dict.pop(key)

    def removeDebuff(self,key):
        self.debuff_dict.pop(key)

    def setProBuff(self,key,value):
        self.property_buff[key] = value






