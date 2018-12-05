def buffCount(obj):
    '''
    战斗前buff 计算
    :param obj:
    :return:
    '''
    obj.tmp_defense = 0
    obj.tmp_attack = 0
    buff_remove_list = []  # buff 移除列表
    for key,value in obj.buff_dict.items():
        if key.skill_model == '0002':
            if value[0] > 0:
                obj.tmp_defense += value[1]
            else:
                value[1] = 0
                obj.tmp_defense += value[1]
                buff_remove_list.append(key)
        else:
            pass
    for key in buff_remove_list:
        obj.buff_dict.pop(key)

    if not obj.buff_dict:
        print("移除buff")


def buffIndex(obj):
    '''
    buff 每回合 递减
    :param obj:
    :return:
    '''
    for key,value in obj.buff_dict.items():
        if value[0] >= 1:
            value[0] -= 1
        else:
            value[0] -= 1
            #buff_remove_list.append(key)
        print("buff 效果渐渐减弱")
        print(key.skill_show_name,value)

def debuffCount(obj):
    '''
    战斗后buff计算
    :param obj:
    :return:
    '''
    debuff_remove_list = []
    for key,value in obj.debuff_dict.items():
        if key.skill_model == '0003':
            if value[0] >= 1:
                obj.health -= int(obj.health * value[1])
                value[0] -= 1
            else:
                debuff_remove_list.append(key)

    for key in debuff_remove_list:
        obj.debuff_dict.pop(key)
        print("移除debuff")
