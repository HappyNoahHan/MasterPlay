def healthRecover(obj,obj_skill):
    '''
    生命恢复
    :param obj:
    :param obj_skill:
    :return:
    '''
    obj.health += obj._max_health * obj_skill.index_per

    if obj.health >= obj._max_health:
        obj.health = obj._max_health


def healthRecoverMax(obj):
    '''
    生命恢复到最大值
    :param obj:
    :return:
    '''
    obj.health = obj._max_health