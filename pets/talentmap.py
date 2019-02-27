'''
    天赋技能表
'''

from pets import pettalent

talent_dict={
    'TA001': pettalent.Talent(name='精神力',talent_code='TA001'),
    'TA002': pettalent.ProUpTalent(name='猛火',talent_code='TA002',up_type='power',match_property='fire',up_number=1.5,up_cause=3),
    'TA003': pettalent.ProUpTalent(name='虫之预感',talent_code='TA003',up_type='power',match_property='insect',up_cause=3,up_number=1.5),
}


def addStatusOrNot(pet,status_code):
    if 'ST100' not in pet.status:
        if status_code == 'ST004':
            if pet.talent in ['TA001',]:
                return False
        return True
    else:
        print("天赋失效～")
        return False

def checkTalentBeforeBattle(pet,skill,attack, defense, spell_power, spell_defense, speed, power):
    if 'ST100' not in pet.status:
        if talent_dict[pet.talent].up_type == 'power':
            power = talent_dict[pet.talent].checkTalent(power,pet.health,pet._max_health,skill.property)
    else:
        print("天赋失效～")
    return attack,defense,spell_power,spell_defense,speed,power