def getCapValue(value,lv,value_indi):
    '''
    计算能力值
    :param value:
    :return:
    '''

    return int((value * 2 + value_indi) * lv /100 + 5)


def gethpCapValue(value,lv,value_indi):
    '''
    计算hp 能力
    :param value:
    :param lv:
    :return:
    '''

    return int((value * 2 + value_indi ) * lv /100 + lv + 10)

def getCapValueForUp(value,lv,value_indi,now_value):
    '''
    计算1级属性提升
    :param now_value: 现在的值
    :return:
    '''

    return getCapValue(value,lv,value_indi) - now_value

def gethpCapValueForUp(value,lv,value_indi,now_value):
    '''
    计算1级hp属性提升
    :param value:
    :param lv:
    :return:
    '''

    return gethpCapValue(value,lv,value_indi) - now_value