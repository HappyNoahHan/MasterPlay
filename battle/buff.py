import assist.petattr
import math
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
    if buff_remove_list:
        for key in buff_remove_list:
            obj.buff_dict.pop(key)
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
            #调整系数
            index_number = assist.petattr.getAttrMap(key,obj)

            if value[0] >= 1:
                lost_health = round(obj.health * value[1] * index_number)
                obj.health -= lost_health
                print("受到 %s  %s 伤害" %(key.skill_show_name,lost_health))
                value[0] -= 1
            else:
                debuff_remove_list.append(key)

    if debuff_remove_list:
        for key in debuff_remove_list:
            obj.debuff_dict.pop(key)
            print("移除debuff")

def proBuffCount(obj):
    '''
    属性增幅buff
    :param obj:
    :return:
    '''
    pro_index = []
    probuff_remove_list = []
    for key,value in obj.property_buff.items():
        if key.property in obj.property:
            if value[0] > 0:
                pro_index.append(value[1])
                print("增幅%s " % value[1])
            else:
                probuff_remove_list.append(key)
        value[0] -= 1

    if probuff_remove_list:
        for key in probuff_remove_list:
            obj.property_buff.pop(key)
            print("移除增幅buff")

    return pro_index


