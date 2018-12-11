'''
    天赋技能表
'''

from pets import pettalent

talent_dict={
    'TA001': pettalent.Firaga(),
    'TA002': pettalent.Growth(),
}


def checkTalent(obj,eff_time):
    '''
    检查生效时机
    :param obj:
    :param eff_time:
    :return:
    '''
    if eff_time in  talent_dict[obj.talent].effect_time:
        return True
    else:
        return False


def talentEffectMiddle(obj,skill,damage):
    # 伤害类天赋计算
    index_damage = damage

    if talent_dict[obj.talent].talent_type == '伤害类型':
        index_damage = talent_dict[obj.talent].talentEffect(skill, damage)

    return index_damage

def talentEffectAfter(obj,skill):

    if talent_dict[obj.talent].talent_type == '回复类型':
        talent_dict[obj.talent].talentEffect(obj)

    return True