def getCapValue(basic,lv,value_indi,base_point):
    '''
    计算能力值
    :param value:
    :return:
    '''

    return int((basic * 2 + base_point /4 + value_indi) * lv /100 + 5)


def gethpCapValue(basic,lv,value_indi,base_point):
    '''
    计算hp 能力
    :param value:
    :param lv:
    :return:
    '''

    return int((basic * 2 + base_point /4 + value_indi ) * lv /100 + lv + 10)

def getAbility(ability,tmp_ability,status,carry_prop,prop_type=None):

    if 'ST098' not in status and carry_prop:
        if carry_prop.prop_type == prop_type:
            prop_ability = carry_prop.propCarry(ability)
            return ability + tmp_ability + prop_ability

    return ability + tmp_ability
