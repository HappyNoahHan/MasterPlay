'''
    ready 2.0 法强  法防
'''

import battle.skill

class Pet(object):
    def __init__(self,name,health,attack,defense,speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self._max_health = self.health
        self.tmp_attack = 0
        self.tmp_defense = 0
        self.debuff_dict = {}
        self.buff_dict = {}
        self.property_buff = {}
        self.skill_list = {}

    autoAi = False

    def showStatus(self):
        print("%s： 攻击 %s 防御 %s 速递 %s 生命 %s " %(
            self.name,
            self.attack + self.tmp_attack,
            self.defense + self.tmp_defense,
            self.speed,
            self.health )
              )

    def getDefense(self):
        return self.defense + self.tmp_defense

    def getAttack(self):
        return self.attack + self.tmp_attack

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






