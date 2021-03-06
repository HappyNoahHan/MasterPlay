import battle.skilllistmap
from pets import  statusmap,talentmap
from assist import weathermap
from props import propmap

def printTurn(name):
    print("%s 的回合" % name)

def noDamage():
    print("攻击几乎任何效果！造成1点伤害 ！")

def battleOver():
    print("战斗结束！")

def gameOver():
    print("游戏结束！")

def petDie(pet):
    pet.is_alive = False
    print("%s 濒危" % pet.getName())

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
    #propmap.checkCarryPropForObj(obj)
    if obj.is_autoAi == True:
        show_tag = 'WildPet'
    else:
        show_tag = ' '
    print("%s  ||  生命值：%s  攻击值 %s 防御值 %s 法攻值 %s 法防值 %s  速度 %s ||  等级: Lv%s  %s" %
          (obj.getName(),obj.hp,obj.getAttack(),obj.getDefense(),
           obj.getSpecialAttack(),obj.getSpecialDefense(),
           obj.getSpeed(),obj.level,show_tag)
          ,end=' || ')
    #if obj.talent:
    #    print("天赋: %s" % talentmap.talent_dict[obj.talent].name,end=' || ')
    if obj.status:
        for status in obj.status:
            print(statusmap.status_dict[status],end=' ')
        print()
    else:
        print()

def showPetSkills(obj):
    for key,value in obj.skill_list.items():
        print(key,':',value.show_name,end=' || ')
        print(value.skill_power,end=' || ')
        print("技能描述：",value.skill_info,end=' || ')
        print("类别: ",value.property)

def learnSkill(code):
    print("%s 学习成功！" % battle.skilllistmap.skill_dict[code].show_name)

def useSkill(obj,skill):
    print("%s 使用 %s 攻击！" % (obj.getName(), skill.show_name))


def propertyUp(health_up,attack_up,defense_up,spell_power_up,spell_defense_up,speed_up):
    print("生命 up %s !" % health_up)
    print("攻击 up %s !" % attack_up)
    print("防御 up %s !" % defense_up)
    print("法攻 up %s !" % spell_power_up)
    print("法防 up %s !" % spell_defense_up)
    print("速度 up %s !" % speed_up)

def checkSelectID(id,dict):
    '''
    检查选择项目正确
    :param id:
    :param dict:
    :return:
    '''
    if id in dict:
        return True
    else:
        print("指令错误!")
        return False

def showPetErrorStatus(obj):
    print("%s 当前状态: " % obj.getName(),end=" ")
    if obj.status:
        for status in obj.status:
            print(statusmap.status_dict[status],end=' ')
            print("%s 层!" % obj.status[status],end=' ')
        print()
    else:
        print("None")


def showPlaceMessage(place):
    if place.place_status != None:
        print("场地： %s %s回合" % (statusmap.status_dict[place.place_status[0]].status_show_name,
              place.place_status[1]),end=' ')
    if place.weather:
        print("天气： %s" % weathermap.weather_dict[place.weather].name)

