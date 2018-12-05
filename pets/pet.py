import battle.skill

class Pet(object):
    def __init__(self,name,health,attack,defense,speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.max_health = self.health
        self.tmp_attack = 0
        self.tmp_defense = 0

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

    talent_skills = battle.skill.skill()

    skill_list = {
        '1':talent_skills
    }

    def setSkills(self,key,value):
        self.skill_list[key] = value


    debuff_dict={}
    buff_dict = {}

    def setDebuff(self,key,value):
        self.debuff_dict[key] = value

    def setBuff(self,key,value):
        self.buff_dict[key] = value






