from pets import pet, wood, fire, fly
import math


def getExpForUp(lv):
    '''
    求升级经验值
    :param lv:
    :return:
    '''
    if lv > 1:
        return pow(lv + 1, 3) - pow(lv, 3)
    else:
        return 1


def getBattleSuccessExp(obj):
    '''
    战斗获胜经验
    :param lv:
    :return:
    '''
    if obj.autoAi == True:
        ai_index = 1
    else:
        ai_index = 1.5

    #后续版本 随身道具
    #if withExpfruit == True:
    #    fruit_index = 1.5
    #else:
    #    fruit_index = 1

    got_exp = round((obj.level * obj.basic_exp_value)/7 * ai_index * 1)

    return got_exp




def isLevelUp(obj):
    '''
    判断是否升级
    :param obj:
    :return:
    '''
    if obj.level == 100:
        print("%s 已经是最高等级" % obj.name)
        return True

    if obj.exp_for_current >= getExpForUp(obj.level):

        obj.exp_for_current -= getExpForUp(obj.level)
        obj.level += 1
        print('%s 升到 %s 级！' % (obj.name,obj.level))
        return isLevelUp(obj)
    else:
        return True