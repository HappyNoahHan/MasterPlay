from pets import status
from assist import rancom
'''
    eg:ST009   麻痹 技能无法使用
'''

status_dict={
    'ST001' : status.Cauma(),
    'ST002' : status.Paralysis(),
    'ST003' : status.Sleeping(),
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


def removeStatus(obj,status_code='all'):
    '''
    移除状态 药品 技能等
    :param obj:
    :param status_code:
    :return:
    '''
    #全能解状态药剂
    if status_code == 'all':
        obj.status.clear()

    if status_code in obj.status:
        obj.status.remove(status_code)


