def healthRecoverBySkill(obj,obj_skill):
    '''
    生命恢复
    :param obj:
    :param obj_skill:
    :return:
    '''
    obj.health += round(obj._max_health * obj_skill.index_per)

    if obj.health >= obj._max_health:
        obj.health = obj._max_health

    print("生命恢复1次")


def healthRecoverMax(obj):
    '''
    生命恢复到最大值
    :param obj:
    :return:
    '''
    obj.health = obj._max_health

def healthRecoverByTalent(obj,per):

    obj.health += round(obj._max_health * per)

    if obj.health >= obj._max_health:
        obj.health = obj._max_health
    return True

def healthRecoreByDrug(obj,value):
    print("%s 回复了 %s HP" % (obj.name,value))
    obj.health += value

    if obj.health >= obj._max_health:
        obj.health = obj._max_health

    return True