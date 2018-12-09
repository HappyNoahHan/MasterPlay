def getCapValue(value,lv,value_indi):
    '''
    计算能力值
    :param value:
    :return:
    '''

    return int(round((value * 2 + value_indi) * lv /100 + 5))


def gethpCapValue(value,lv,value_indi):
    '''
    计算hp 能力
    :param value:
    :param lv:
    :return:
    '''

    return int(round((value * 2 + value_indi ) * lv /100 + lv + 10))

def getCapValueForOne(value,lv,value_indi):
    '''
    计算1级属性提升
    :param value:
    :return:
    '''

    return getCapValue(value,lv,value_indi) - getCapValue(value,lv-1,value_indi)

def gethpCapValueForOne(value,lv,value_indi):
    '''
    计算1级hp属性提升
    :param value:
    :param lv:
    :return:
    '''

    return gethpCapValue(value,lv,value_indi) -gethpCapValue(value,lv-1,value_indi)
