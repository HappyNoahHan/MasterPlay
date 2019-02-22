from pets import status
from assist import rancom

import time
'''
    eg:ST009   麻痹 技能无法使用
'''

status_dict={
    'ST001' : status.Cauma(),
    'ST002' : status.Paralysis(),
    'ST003' : status.Sleeping(),
    'ST004' : status.Shrink(),
    'ST005' : status.Poisoning(),
    'ST006' : status.Chaos(),
}


def checkStatusAfterBattle(obj,skill,damage):
    damage_index = damage
    for value in obj.status:
        if value == 'ST001':
            damage_index = status_dict[value].statusEffect(skill,damage)

    return damage_index



def checkParalysisOrNot(obj):
    '''
    检查是否是麻痹状态 有1/4几率无法成功使用技能
    :param obj:
    :return:
    '''
    if 'ST002' in obj.status:
        if status_dict['ST002'].statusEffect():
            print("%s 处于麻痹状态,技能使用失败!" % obj.name)
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

def checkPoisoning(obj):
    '''
    检查是否中毒
    :param obj:
    :return:
    '''
    if 'ST005' in obj.status:
        damage = status_dict['ST005'].statusEffect(obj.status['ST005'],obj._max_health)
        print("%s 中毒损失了 %s HP" % (obj.name,damage))
        obj.health -= damage
        if obj.health <= 0:
            return False
        #obj._max_health -= damage
        obj.status['ST005'] += 1

    return True


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
            obj.removeStatus(status_code)

        print("%s 当前状态：" % obj.name, obj.status)

    return True

def checkUnlockOrNot(obj):
    if 'ST099' in obj.status:
        return False
    return True

def checkChaosOrNot(obj):
    if 'ST006' in obj.status:
        if obj.status['ST006'] > 2 and obj.status['ST006'] < 5:
            if rancom.statusRandom(25): #1/4 几率自我解除
                print("%s 自行解除了混乱状态~" % obj.name)
                removeStatus(obj,'ST006')
                return False
            else:
                return True
        if obj.status['ST006'] >= 5:
            print("%s 自行解除了混乱状态~" % obj.name)
            removeStatus(obj,'ST006')
            return False
        if status_dict['ST006'].statusEffect():
            obj.status['ST006'] += 1
            return True
    return False


