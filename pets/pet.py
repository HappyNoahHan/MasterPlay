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
    def __init__(self,level=1,skill_list={},exp_for_current=0,carry_prop=None,base_points_list=[],has_trainer=False,is_autoAi=True):
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
        #临时提升的能力属性
        self.tmp_attack = 0
        self.tmp_defense = 0
        self.tmp_spell_power = 0
        self.tmp_spell_defense = 0
        self.tmp_speed = 0
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
        #是否捕获
        self.has_captured = self.has_trainer

        self.is_autoAi = False
        #最后使用过的技能
        self.last_used_skill = None
        #赏金
        self.reward_money = None

    def getDefense(self):
        return cap.getAbility(self.defense,self.tmp_defense,self.status,self.carry_prop,prop_type='DE')

    def getAttack(self):
        return cap.getAbility(self.attack,self.tmp_attack,self.status,self.carry_prop,prop_type='AT')

    def getSpellPower(self):
        return cap.getAbility(self.spell_power,self.tmp_spell_power,self.status,self.carry_prop,prop_type='SPO')

    def getSpellDefense(self):
        return cap.getAbility(self.spell_defense,self.tmp_spell_defense,self.status,self.carry_prop,prop_type='SDE')

    def getSpeed(self):
        return cap.getAbility(self.speed,self.tmp_speed,self.status,self.carry_prop,prop_type='SP')
    #不能初始化，不然用的是同一个地址
    skill_list={}
    def setSkills(self,key,value):
        self.skill_list[key] = value

    def removeSkills(self,key):
        self.skill_list.pop(key)

    def setStatus(self,key,value=1):
        self.status[key] = value

    def removeStatus(self,key):
        self.status.pop(key)







