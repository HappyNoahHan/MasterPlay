from pets import status
from assist import rancom
'''
    eg:ST009   麻痹 技能无法使用
'''

status_dict={
    'ST001' : status.Cauma(),
    'ST002' : status.Paralysis(),
}


def checkStatusAfterBattle(obj,skill,damage):
    damage_index = damage
    for value in obj.status:
        if value == 'ST001':
            damage_index = status_dict[value].statusEffect(skill,damage)

    return damage_index



def checkStatusBeforeBattle(obj):
    if 'ST002' in obj.status:

        if status_dict['ST002'].statusEffect():
            return True

    return False
