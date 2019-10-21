'''
    2.0 法强  法防  结算方式改变
    3.0 经验值
    3.1 pet init 改造 基础能力值
    3.2 升级属性提升  后续版本个体值
    3.21 随机1-31
    3.3 特性 eg：猛火
    3.4 状态 eg：灼伤
    4.0 基础点数 上限255
    5.0 从数据库读取信息
'''


from assist import cap,rancom
from database import petdata

class Pets(object):
    def __init__(self,petNo,level,skill_list=None):
        self.petNo = petNo
        self.level = level
        self.pet_detail_msg=petdata.get_pet(self.petNo)

        #随机数值 后续 随某个参数的提升 个体值更固定 ？
        [self.health_ini_value,
            self.attack_ini_value,
            self.defense_ini_value,
            self.special_attack_ini_value,
            self.special_defense_ini_value,
            self.speed_ini_value] = rancom.getIndiValue()

        self.hp = self.getHp()
        self._max_hp = self.hp
        self.attack = self.getAttack()
        self.defense = self.getDefense()
        self.special_attack = self.getSpecialAttack()
        self.special_defense = self.getSpecialDefense()
        self.speed = self.getSpeed()

        #base point 基础点 总和不得高于255
        self.hp_point = 0
        self.attack_point = 0
        self.defense_point = 0
        self.special_attack_point = 0
        self.special_defense_point = 0
        self.speed_point = 0

        #经验值
        self.exp = 0
        #技能树 从数据库读 后续
        self.skill_list = skill_list
        self.realize_skill_list = [] #已经领悟的技能表
        self.status = {} #状态表
        self.carry_prop = None
        self.berry = None #树果 只能保持一个
        #闪避
        self.dodge = 0
        #基础点数获得者，经验减半状态
        self.basic_point_getter = None
        #self.exp_status = []
        #遇见随机数
        #self.talent = 'TA002'
        #是否濒危?改为状态？如何
        self.is_alive = True
        #是否玩家所有
        self.owner = None #玩家名字
        #是否捕获
        self.has_captured = False
        #是否AI
        self.is_autoAi = True
        #最后使用过的技能
        self.last_used_skill = None
        #赏金
        self.reward_money = 0
        #基础经验值
        self.basic_exp_value = self.getBasicExpValue()

    def getName(self):
        return self.pet_detail_msg[1]

    def getAttr(self):
        return self.pet_detail_msg[2]

    def getTalent(self):
        return self.pet_detail_msg[3].split('/')

    def getHidTalent(self):
        return self.pet_detail_msg[4].split('/')

    def getBasicHp(self):
        return self.pet_detail_msg[8]

    def getBasicAttack(self):
        return self.pet_detail_msg[9]

    def getBasicDefense(self):
        return self.pet_detail_msg[10]

    def getBasicSpecialAttck(self):
        return self.pet_detail_msg[11]

    def getBasicSpecialDefense(self):
        return self.pet_detail_msg[12]

    def getBasicSpeed(self):
        return self.pet_detail_msg[13]

    def getAttrRelationShip(self):
        return self.pet_detail_msg[15]

    def getCaptureDegree(self):
        return self.pet_detail_msg[19]

    def getExpForFullLevel(self):
        return int(''.join(self.pet_detail_msg[21].split(',')))

    def getBasicPoint(self):
        return self.pet_detail_msg[22].split('、')

    def getHp(self):
        return cap.gethpCapValue(self.getBasicHp(),self.level,self.health_ini_value)

    def getAttack(self):
        return cap.getCapValue(self.getBasicAttack(),self.level,self.attack_ini_value)

    def getDefense(self):
        return cap.getCapValue(self.getBasicDefense(),self.level,self.defense_ini_value)

    def getSpecialAttack(self):
        return cap.getCapValue(self.getBasicSpecialAttck(),self.level,self.special_attack_ini_value)

    def getSpecialDefense(self):
        return cap.getCapValue(self.getBasicSpecialDefense(),self.level,self.special_defense_ini_value)

    def getSpeed(self):
        return cap.getCapValue(self.getBasicSpeed(),self.level,self.speed_ini_value)

    def getTotalPoint(self):
        return self.attack_point + self.hp_point + self.defense_point \
               + self.special_attack_point + self.special_defense_point + self.speed_point

    def getBasicExpValue(self):
        return  int((self.getExpForFullLevel()/100 * (self.pet_detail_msg[14] /1000  + 1) ) / self.getCaptureDegree())


    #for test
    def setautoAi(self,value):
        self.is_autoAi = value

    def setOwner(self,value):
        self.owner = value


    def setSkills(self,key,value):
        self.skill_list[key] = value

    def removeSkills(self,key):
        self.skill_list.pop(key)

    def setStatus(self,key,value=1):
        self.status[key] = value

    def removeStatus(self,key):
        self.status.pop(key)