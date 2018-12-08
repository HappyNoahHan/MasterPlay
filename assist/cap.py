def getCapValue(value,lv):
    '''
    计算能力值
    :param value:
    :return:
    '''

    return int(round((value * 2) * lv /100 + 5))


def gethpCapValue(value,lv):
    '''
    计算hp 能力
    :param value:
    :param lv:
    :return:
    '''

    return int(round((value * 2) * lv /100 + lv + 10))
