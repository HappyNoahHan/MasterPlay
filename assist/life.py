from pets import statusmap
def checkStatus(func):
    def wrapper(*args,**kwargs):
        if statusmap.checkHealBlockOrNot(args[0]):
            print("%s 无法被治疗~" % args[0].name)
            return True
        return func(*args,**kwargs)
    return wrapper

@checkStatus
def healthRecoverBySkill(obj,obj_skill):
    '''
    生命恢复
    :param obj:
    :param obj_skill:
    :return:
    '''
    recover_health = round(obj._max_health * obj_skill.index_per)
    obj.health += recover_health

    if obj.health >= obj._max_health:
        obj.health = obj._max_health

    print("%s 回复了 %s 点HP!" % (obj.name, recover_health))

@checkStatus
def healthRecoverMax(obj):
    '''
    生命恢复到最大值
    :param obj:
    :return:
    '''
    obj.health = obj._max_health
    return True

@checkStatus
def healthRecoverByTalent(obj,per):

    obj.health += round(obj._max_health * per)

    if obj.health >= obj._max_health:
        obj.health = obj._max_health
    return True

@checkStatus
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

@checkStatus
def healthRecoverFromDamage(obj,damage,recover_per):
    recover_health = round(damage * recover_per)
    if recover_health == 0:
        recover_health = 1

    obj.health += recover_health
    if obj.health >= obj._max_health:
        obj.health = obj._max_health

    print("%s 吸取了 %s 点HP！" % (obj.name,recover_health))

@checkStatus
def healthRecoverFromImprintSkill(obj,turns):
    if turns == 1:
        recover_health = round(obj._max_health * 0.25)
    elif turns == 2:
        recover_health = round(obj._max_health * 0.5)
    else:
        recover_health = obj._max_health

    obj.health += recover_health
    if obj.health >= obj._max_health:
        obj.health = obj._max_health
    print("%s 回复 %s 点HP！" % (obj.name, recover_health))
