def ppCount(obj_skill):
    '''
    技能pp值计算
    :param obj_skill:
    :return:
    '''
    if obj_skill.pp_value > 0:
        obj_skill.pp_value -= 1
        return True

    else:
        print("技能pp值不足")
        return False

def ppRecoverMax(obj_skill):
    '''
    技能品牌值恢复到最大
    :param obj:
    :return:
    '''
    obj_skill.pp_value = obj_skill._pp_value_max

def ppAddLong(obj_skill,number):
    '''
    技能pp值永久增加
    :param obj_skill:
    :param number:
    :return:
    '''
    obj_skill._pp_value_max += number


def ppRecover(obj_skill,number):
    '''
    技能pp值恢复一定数量
    :param obj_skill:
    :return:
    '''
    obj_skill.pp_value += number

    if obj_skill.pp_value > obj_skill._pp_value_max:
        obj_skill.pp_value = obj_skill._pp_value_max