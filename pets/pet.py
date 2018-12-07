'''
    2.0 法强  法防  结算方式改变
'''

import battle.skill

class Pet(object):
    def __init__(self,health,attack,defense,spell_power,spell_defense,speed):

        self.health = health
        self.attack = attack
        self.defense = defense
        self.spell_power = spell_power
        self.spell_defense = spell_defense
        self.speed = speed
        self._max_health = self.health
        self.tmp_attack = 0
        self.tmp_defense = 0
        self.tmp_spell_power = 0
        self.tmp_spell_defense = 0
        self.debuff_dict = {}
        self.buff_dict = {}
        self.property_buff = {}
        self.skill_list = {}

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






