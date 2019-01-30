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
    return True

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

def restore(pet):
    '''
    pet 状态恢复
    :param pet:
    :return:
    '''
    pet.health = pet._max_health
    pet.debuff_dict.clear()
    pet.buff_dict.clear()
    pet.property_buff.clear()
    pet.status.clear()
    pet.alive = True
    pet.basic_point_getter = None

    for key,skill in pet.skill_list.items():
        skill.pp_value = skill._pp_value_max