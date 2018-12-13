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