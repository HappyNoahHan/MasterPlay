from pets import status
import time
'''
    eg:ST009   麻痹 技能无法使用
'''

status_dict={
    'ST001' : status.Cauma(),
    'ST002' : status.Paralysis(),
    'ST003' : status.Sleeping(),
    'ST004' : status.Shrink(),
}


def checkStatusAfterBattle(obj,skill,damage):
    damage_index = damage
    for value in obj.status:
        if value == 'ST001':
            damage_index = status_dict[value].statusEffect(skill,damage)

    return damage_index



def checkParalysisOrNot(obj):
    '''
    检查是否是麻痹状态 有一定几率无法成功使用技能
    :param obj:
    :return:
    '''
    if 'ST002' in obj.status:
        if status_dict['ST002'].statusEffect():
            print("%s 处于麻痹状态,无法做出行动!" % obj.name)
            return True
    return False

def checkSleepingOrNot(obj):
    '''
    检查是否是睡眠状态
    :param obj:
    :return:
    '''
    if 'ST003' in obj.status:
        if status_dict['ST003'].statusEffect():
            print("%s 清醒了！" % obj.name)
            removeStatus(obj,'ST003')
            return False
        return True
    return False

def checkShrinkaOrNot(obj):
    '''
    检查畏缩状态
    :param obj:
    :return:
    '''
    if 'ST004' in obj.status:
        if status_dict['ST004'].statusEffect():
            print("%s 畏缩不前,没有做出任何动作！" % obj.name)
            return True
    return False

def checkStatusBeforeBattle(obj):
    if obj.status:
        if checkParalysisOrNot(obj):
            return True
        if checkSleepingOrNot(obj):
            print("%s 睡眠中,无法使用技能~" % obj.name)
            time.sleep(3)
            return True
        if checkShrinkaOrNot(obj):
            return True
    else:
        print("%s 没有处于任何状态！" % obj.name)
    return False


def removeStatus(obj,status_code):
    '''
    移除状态 药品 技能等
    :param obj:
    :param status_code:
    :return:
    '''
    #全能解状态药剂
    #print("使用解除剂")
    if status_code != None:
        if status_code == 'all':
            obj.status.clear()

        if status_code in obj.status:
            obj.status.remove(status_code)

        print("%s 当前状态：" % obj.name, obj.status)

    return True


