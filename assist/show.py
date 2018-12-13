import battle.skilllistmap
from props import propmap

def printTurn(name):
    print("%s 的回合" % name)

def noDamage():
    print("攻击几乎任何效果！造成1点伤害 ！")

def battleOver():
    print("战斗结束！")

def gameOver():
    print("战斗失败！")

def petDie(name):
    print("%s 死亡" % name)

def petThink(name):
    print("%s 正在思考！" % name)

def petSelectSkill(name):
    print("%s 正在思考选择技能!" % name)

def petUseRun(name):
    print("%s 开始逃跑了" % name)

def petUseOrdinaryAttack(name):
    print("%s 使用普通攻击" % name)

def petUseDefense(name):
    print("%s 开始了防御姿态" % name)

def showSelect():
    print("请选择使用的指令1：特殊攻击 2.交换精灵 3.使用道具 4.临阵脱逃")

def showProps():
    #测试
    print("请选择使用的道具：1 PP恢复剂")

def showPetStatus(obj):
    '''
    显示精灵状态
    :param obj:
    :return:
    '''
    propmap.checkCarryPropForObj(obj)
    print("%s 的生命值：%s  攻击值 %s 防御值 %s 法攻值 %s 法防值 %s  速度 %s 等级: Lv%s" % (obj.name,obj.health,obj.getAttack(),obj.getDefense(),obj.getSpellPower(),obj.getSpellDefense(),obj.getSpeed(),obj.level))

def showPetSkills(obj):
    for key,value in obj.skill_list.items():
        print(key,':',value.skill_show_name)

def learnSkill(code):
    print("%s 学习成功！" % battle.skilllistmap.skill_dict[code].skill_show_name)

def useSkill(obj,skill):
    print("%s 使用 %s 攻击！" % (obj.name, skill.skill_show_name))


def propertyUp(health_up,attack_up,defense_up,spell_power_up,spell_defense_up,speed_up):
    print("生命 up %s !" % health_up)
    print("攻击 up %s !" % attack_up)
    print("防御 up %s !" % defense_up)
    print("法攻 up %s !" % spell_power_up)
    print("法防 up %s !" % spell_defense_up)
    print("速度 up %s !" % speed_up)