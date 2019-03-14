'''
    2.0 法强  法防  结算方式改变
    3.0 经验值
    3.1 pet init 改造 基础能力值
    3.2 升级属性提升  后续版本个体值
    3.21 随机1-31
    3.3 特性 eg：猛火
    3.4 状态 eg：灼伤
    4.0 基础点数 上限255
'''


from assist import cap,rancom

class Pet(object):
    #天赋
    talent = None
    #能力值 每个精灵属性皆不同
    health_basic = 1
    attack_basic = 1
    defense_basic = 1
    spell_power_basic = 1
    spell_defense_basic = 1
    speed_basic = 1
    #基础点数

    #初始化函数
    #初始化的时候 需要将技能 基础点数传输进去，不然每一个类是固定的
    def __init__(self,level=1,skill_list={},exp_for_current=0,carry_prop=None,base_points_list=[],has_trainer=False,autoAi=True):
        self.level = level

        [self.health_indi,
            self.attack_indi,
            self.defense_indi,
            self.spell_power_indi,
            self.spell_defense_indi,
            self.speed_indi] = rancom.getIndiValue()
        [self.health_base_point,
         self.attack_base_point,
         self.defense_base_point,
         self.spell_power_base_point,
         self.spell_defense_base_point,
         self.speed_base_point] = base_points_list
        self.health = cap.gethpCapValue(self.health_basic,self.level,self.health_indi,self.health_base_point)
        self.attack = cap.getCapValue(self.attack_basic,self.level,self.attack_indi,self.attack_base_point)
        self.defense = cap.getCapValue(self.defense_basic,self.level,self.defense_indi,self.defense_base_point)
        self.spell_power = cap.getCapValue(self.spell_power_basic,self.level,self.spell_power_indi,self.spell_power_base_point)
        self.spell_defense = cap.getCapValue(self.spell_defense_basic,self.level,self.spell_defense_indi,self.spell_defense_base_point)
        self.speed = cap.getCapValue(self.speed_basic,self.level,self.speed_indi,self.speed_base_point)
        self._max_health = self.health
        #buff提升的能力属性
        self.tmp_attack = 0
        self.tmp_defense = 0
        self.tmp_spell_power = 0
        self.tmp_spell_defense = 0
        self.tmp_speed = 0
        #属性道具提升的能力属性
        #self.prop_attack_up = 0
        #self.prop_defense_up = 0
        #self.prop_spell_power_up = 0
        #self.prop_spell_defense_up = 0
        #self.prop_speed_up = 0
        #buff debuff 进化解除
        self.debuff_dict = {}
        self.buff_dict = {}
        self.property_buff = {}
        #以下是进化时需要继承的选线
        self.skill_list = skill_list
        self.exp_for_current = exp_for_current
        self.realize_skill_list = [] #已经领悟的技能表
        self.status = {} #状态表
        self.carry_prop = carry_prop
        self.berry = None #树果
        #闪避
        self.dodge = 0
        #基础点数获得者，经验减半状态
        self.basic_point_getter = None
        #self.exp_status = []
        #遇见随机数
        #self.talent = 'TA002'
        #是否濒危
        self.alive = True
        #是否玩家所有
        self.has_trainer = has_trainer
        if self.has_trainer == True:
            #self.autoAi = False
            self.captured = True
        elif self.has_trainer == None:
            self.captured = None
        else:
            #self.autoAi = True
            self.captured = False
        self.autoAi = autoAi
        #最后使用过的技能
        self.last_used_skill = None

    def getDefense(self):
        if self.carry_prop != None and 'ST098' not in self.status:
            if self.carry_prop.up_type == 'defense':
                prop_defense_up = self.carry_prop.propCarry(self.defense)
                return self.defense + self.tmp_defense + prop_defense_up
        return self.defense + self.tmp_defense

    def getAttack(self):
        if self.carry_prop != None and 'ST098' not in self.status:
            if self.carry_prop.up_type == 'attack':
                prop_attack_up = self.carry_prop.propCarry(self.attack)
                return self.attack + self.tmp_attack + prop_attack_up
        return self.attack + self.tmp_attack

    def getSpellPower(self):
        if self.carry_prop != None and 'ST098' not in self.status:
            if self.carry_prop.up_type == 'spell_power':
                prop_spell_power_up = self.carry_prop.propCarry(self.spell_power)
                return self.spell_power + self.tmp_spell_power + prop_spell_power_up
        return self.spell_power + self.tmp_spell_power

    def getSpellDefense(self):
        if self.carry_prop != None and 'ST098' not in self.status:
            if self.carry_prop.up_type == 'spell_defense':
                prop_spell_defense_up = self.carry_prop.propCarry(self.spell_defense)
                return self.spell_defense + self.tmp_spell_defense + prop_spell_defense_up
        return self.spell_defense + self.tmp_spell_defense

    def getSpeed(self):
        if self.carry_prop != None and 'ST098' not in self.status:
            if self.carry_prop.up_type == 'speed':
                prop_speed_up = self.carry_prop.propCarry(self.speed)
                return self.speed + self.tmp_speed + prop_speed_up
        return self.speed + self.tmp_speed

    #不能初始化，不然用的是同一个地址
    skill_list={}
    def setSkills(self,key,value):
        self.skill_list[key] = value

    def removeSkills(self,key):
        self.skill_list.pop(key)

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

    def setStatus(self,key,value=1):
        self.status[key] = value

    def removeStatus(self,key):
        self.status.pop(key)






