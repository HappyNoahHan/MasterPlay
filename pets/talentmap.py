'''
    天赋技能表
'''

from pets import pettalent,statusmap

talent_dict={
    'TA001': pettalent.Talent(name='精神力',talent_code='TA001'),
    'TA002': pettalent.ProUpTalent(name='猛火',talent_code='TA002',up_type='power',match_property='fire',up_number=1.5,up_cause=3),
    'TA003': pettalent.ProUpTalent(name='虫之预感',talent_code='TA003',up_type='power',match_property='insect',up_cause=3,up_number=1.5),
}


def addStatusOrNot(pet,status_code,place):
    '''
    检查天赋是否免疫
    :param pet:
    :param status_code:
    :param place:
    :return:
    '''
    if 'ST100' not in pet.status:
        if status_code == 'ST004':
            if pet.talent in ['TA001',]:
                return False
        if status_code == 'ST003' and place.place_status:
            #电磁场 不能睡眠
            if place.place_status[0] == 'ST034':
                return False

        if 'ST114' in pet.status:
            #神秘守护  无法被异常状态
            if status_code in statusmap.abnormal_list:
                return False

        return True
    else:
        print("天赋失效～")
        return False

def checkTalentBeforeBattle(pet,skill,attack, defense, spell_power, spell_defense, speed, power):
    if pet.talent != None:
        if 'ST100' not in pet.status:
            if talent_dict[pet.talent].up_type == 'power':
                power = talent_dict[pet.talent].checkTalent(power,pet.health,pet._max_health,skill.property)
        else:
            print("天赋失效～")
    return attack,defense,spell_power,spell_defense,speed,power