'''
    2.0 法强  法防  结算方式改变
    3.0 经验值
    3.1 pet init 改造 基础能力值
    3.2 升级属性提升  后续版本个体值 随机1-31 基础点数
    3.3 ready 需要一个函数random 几率
'''

import battle.skill
from assist import cap

class Pet(object):
    health_basic = 1
    attack_basic = 1
    defense_basic = 1
    spell_power_basic = 1
    spell_defense_basic = 1
    speed_basic = 1



    def __init__(self,level):
        self.level = level

        self.health = cap.gethpCapValue(self.health_basic,self.level)
        self.attack = cap.getCapValue(self.attack_basic,self.level)
        self.defense = cap.getCapValue(self.defense_basic,self.level)
        self.spell_power = cap.getCapValue(self.spell_power_basic,self.level)
        self.spell_defense = cap.getCapValue(self.spell_defense_basic,self.level)
        self.speed = cap.getCapValue(self.speed_basic,self.level)
        self._max_health = self.health
        self.tmp_attack = 0
        self.tmp_defense = 0
        self.tmp_spell_power = 0
        self.tmp_spell_defense = 0
        self.debuff_dict = {}
        self.buff_dict = {}
        self.property_buff = {}
        self.skill_list = {}
        self.exp_for_current = 0



    autoAi = False


    def getDefense(self):
        return self.defense + self.tmp_defense

    def getAttack(self):
        return self.attack + self.tmp_attack

    def getSpellPower(self):
        return self.spell_power + self.tmp_spell_power

    def getSpellDefense(self):
        return self.spell_defense + self.tmp_spell_defense

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






