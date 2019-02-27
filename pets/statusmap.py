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
    'ST005' : status.BigPoisoning(),
    'ST006' : status.Chaos(),
    'ST007' : status.Poisoning(),
    'ST008' : status.Frozen(),
    'ST009' : status.ArmorBreak(),
    'ST010' : status.Bound(),
    'ST011' : status.GuardBreak(),
    'ST012' : status.PowerSave(),
}


def checkStatusAfterBattle(obj,skill,damage):
    damage_index = damage
    for key,value in obj.status.items():
        if key == 'ST001':
            if not skill.spell_skill:
                print("物理招式，伤害减半")
                damage_index = round(damage_index / 2)

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
        if obj.status['ST003'] > 2 and obj.status['ST003'] <= 4:
            if status_dict['ST003'].statusEffect():
                print("%s 清醒了！" % obj.name)
                removeStatus(obj,'ST003')
                return False

        elif obj.status['ST003'] > 4:
            removeStatus(obj,'ST003')
            return False

        obj.status['ST003'] += 1
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
            print("%s 被麻痹,没有成功使用技能~" % obj.name)
            return True
        if checkSleepingOrNot(obj):
            print("%s 睡眠中,无法使用技能~" % obj.name)
            time.sleep(3)
            return True
        if checkShrinkaOrNot(obj):
            print("%s 畏缩不前,没有成功使用技能~" % obj.name)
            return True
        if checkFrozenOrNot(obj):
            print("%s 冰冻中, 无法使用任何技能" % obj.name)
            return True
    else:
        print("%s 没有处于任何状态！" % obj.name)
    return False

def checkStatusAfterTurn(obj):
    '''
    检查回合结束 中毒 灼伤 伤害
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

    if 'ST007' in obj.status:
        damage = status_dict['ST007'].statusEffect(obj._max_health)
        print("%s 中毒损失了 %s HP" % (obj.name, damage))
        obj.health -= damage
        if obj.health <= 0:
            return False

    if 'ST001' in obj.status:
        damage = status_dict['ST001'].statusEffect(obj._max_health)
        print("%s 因灼伤损失了 %s HP" % (obj.name, damage))
        obj.health -= damage
        if obj.health <= 0:
            return False

    if 'ST010' in obj.status:
        if obj.status['ST010'] > 4:
            removeStatus(obj,'ST010')
            return True
        elif obj.status['ST010'] == 4:
            if rancom.statusRandom(50):
                removeStatus(obj,'ST010')
                return True
        obj.status['ST010'] += 1
        damage = status_dict['ST010'].statusEffect(obj._max_health)
        print("%s 因束缚损失了 %s HP" % (obj.name, damage))
        obj.health -= damage
        if obj.health <= 0:
            return False
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
            print("%s 解除了 %s 状态：" % (obj.name, status_dict[status_code].status_show_name))
        else:
            print("并没有什么效果~")
    return True

def checkUnlockOrNot(obj):
    '''
    lock bound 状态下无法逃走
    :param obj:
    :return:
    '''
    if 'ST099' in obj.status or 'ST010' in obj.status:
        return False
    return True

def checkChaosOrNot(obj):
    if 'ST006' in obj.status:
        if obj.status['ST006'] > 2 and obj.status['ST006'] < 5:
            if rancom.statusRandom(25): #1/4 几率自我解除
                print("%s 解除了混乱状态~" % obj.name)
                removeStatus(obj,'ST006')
                return False

        elif obj.status['ST006'] >= 5:
            print("%s 解除了混乱状态~" % obj.name)
            removeStatus(obj,'ST006')
            return False

        obj.status['ST006'] += 1
        if status_dict['ST006'].statusEffect():
            return True

    return False


def checkStatusEnd(player):
    '''
    战斗结束之后 检查状态 主要使将某些状态减弱 剧毒-->中毒
    :param player:
    :return:
    '''
    for key,pet in player.pet_list.items():
        if 'ST005' in pet.status:
            removeStatus(pet,'ST005')
            pet.setStatus('ST007')

def resetStatusAfterChange(pet):
    '''
    交换后重置剧毒状态回合
    :param pet:
    :return:
    '''
    if 'ST005' in pet.status:
        pet.setStatus('ST005')

def checkFrozenOrNot(obj):
    '''
    检查是否是冰冻状态
    :param obj:
    :return:
    '''
    if 'ST008' in obj.status:
        if status_dict['ST008'].statusEffect():
            print("%s 解除了 冰冻！" % obj.name)
            removeStatus(obj,'ST008')
            return False
        return True
    return False

def checkArmorBreakOrNot(obj,defense):
    '''
    检查是否破甲
    :param obj:
    :return:
    '''
    if 'ST009' in obj.status:
        return status_dict['ST009'].statusEffect(defense,obj.status['ST009'])

    return defense

def checkNoChange(obj):
    if 'ST010' in obj.status:
        return False

    return True

def checkGuardBreakOrNot(obj,spell_defense):
    '''
    检查特防降低
    :param obj:
    :param spell_defense:
    :return:
    '''
    if 'ST011' in obj.status:
        return status_dict['ST011'].statusEffect(spell_defense,obj.status['ST011'])

    return spell_defense

def checkPowerSave(obj,defense,spell_defense):
    '''
    检查 蓄力
    :param obj:
    :param defense:
    :param spell_defense:
    :return:
    '''
    if 'ST012' in obj.status:
        return status_dict['ST012'].statusEffect(defense,spell_defense)
    return defense,spell_defense

def checkPropBeforeBattle(obj_attack,obj_defense,attack,defense,spell_power,spell_defense,speed):

    # 2.0检查是否破甲
    defense = checkArmorBreakOrNot(obj_defense, defense)
    # 2.0检查破防
    spell_defense = checkGuardBreakOrNot(obj_defense, spell_defense)
    # 2.1 检查蓄力
    defense,spell_defense = checkPowerSave(obj_defense,defense,spell_defense)

    #2.0 检查是否在麻痹状态下 速度减半
    if 'ST002' in obj_attack.status:
        speed = int(speed / 2)


    return attack,defense,spell_power,spell_defense,speed

