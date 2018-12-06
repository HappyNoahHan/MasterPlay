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

    init_skills = battle.skill.skill()

    skill_list = {
        '1':init_skills
    }

    def setSkills(self,key,value):
        self.skill_list[key] = value

    def setDebuff(self,key,value):
        self.debuff_dict[key] = value

    def setBuff(self,key,value):
        self.buff_dict[key] = value

    def setProBuff(self,key,value):
        self.property_buff[key] = value






