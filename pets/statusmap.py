from pets import status
'''
    eg:ST009   麻痹 技能无法使用
'''

status_dict={
    'ST001' : status.Cauma()
}


def checkStatusAfterBattle(obj,skill,damage):
    damage_index = damage
    for value in obj.status:
        if value == 'ST001':
            damage_index = status_dict[value].statusEffect(skill,damage)

    return damage_index



def checkStatusBeforeBattle(obj):
    if 'ST009' in obj.status:
        return False

    return True
