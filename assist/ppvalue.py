from assist import show

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

def ppRecoverMax(obj):
    '''
    技能品牌值恢复到最大
    :param obj:
    :return:
    '''
    print("请选择要恢复的技能")
    for key,value in obj.skill_list.items():
        print(key,":",value.skill_show_name,' ',value.pp_value)
    select_id = input(">")
    if show.checkSelectID(select_id, obj.skill_list):
        obj.skill_list[select_id].pp_value = obj.skill_list[select_id]._pp_value_max
    else:
        return ppRecoverMax(obj)
    return True

def ppAddLong(obj,number):
    '''
    技能pp值永久增加
    :param obj_skill:
    :param number:
    :return:
    '''
    print("请选择要恢复的技能")
    for key,value in obj.skill_list.items():
        print(key,":",value.skill_show_name,' ',value.pp_value)
    select_id = input(">")

    if show.checkSelectID(select_id,obj.skill_list):
        obj.skill_list[select_id]._pp_value_max += number
    else:
        return ppAddLong(obj,number)
    return True


def ppRecover(obj,number):
    '''
    技能pp值恢复一定数量
    :param obj_skill:
    :return:
    '''
    print("请选择要恢复的技能")
    for key,value in obj.skill_list.items():
        print(key,":",value.skill_show_name,' ',value.pp_value)
    select_id = input(">")
    if show.checkSelectID(select_id,obj.skill_list):
        obj.skill_list[select_id].pp_value += number

        if obj.skill_list[select_id].pp_value > obj.skill_list[select_id]._pp_value_max:
            obj.skill_list[select_id].pp_value = obj.skill_list[select_id]._pp_value_max
    else:
        return ppRecover(obj,number)

    return True