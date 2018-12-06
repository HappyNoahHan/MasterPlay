import assist.petattr
import assist.life
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
        if key.buff_prop == 'Defense':
            if value[0] > 0:
                obj.tmp_defense += value[1]
            else:
                value[1] = 0
                obj.tmp_defense += value[1]
                buff_remove_list.append(key)

        elif key.buff_prop == 'Attack':
            if value[0] == 0:
                value[1] = 0
                buff_remove_list.append(key)
            obj.tmp_attack += value[1]

        elif key.buff_prop == 'Health':
            if value[0] > 0:
                assist.life.healthRecover(obj,key) #调用回复技能
            else:
                buff_remove_list.append(key)
        else:
            pass
    if buff_remove_list:
        for key in buff_remove_list:
            obj.buff_dict.pop(key)
            print("移除 %s 效果" % key.skill_show_name)


def buffIndex(obj):
    '''
    所有增益buff 每回合 递减（debuff等是自己管自己）
    :param obj:
    :return:
    '''
    for key,value in obj.buff_dict.items():
        if value[0] >= 1:
            value[0] -= 1
        else:
            value[0] -= 1
            #buff_remove_list.append(key)
        print("%s 效果渐渐减弱" % key.skill_show_name)

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
            print("移除 %s 伤害" % key.skill_show_name)

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
            print("移除 %s 增幅效果" % key.skill_show_name)

    return pro_index


def removeObjBuff(obj,num):
    '''
    驱散对方增益buff
    :param obj:
    :param num:
    :return:
    '''
    if obj.buff_dict:
        if num <= len(obj.buff_dict.items()):
            for i in range(num):
                del_item = obj.buff_dict.popitem()
                print("驱散  %s" % del_item[0].skill_show_name)
        else:
            obj.buff_dict.clear()
            print("驱散成功！")
    else:
        print("对方没有buff")

    buffCount(obj)

def removeOwnDebuff(obj,num):
    if obj.debuff_dict:
        if num <= len(obj.debuff_dict.items()):
            for i in range(num):
                del_item = obj.debuff_dict.popitem()
                print("移除 %s 负面效果" % del_item[0].skill_show_name)
        else:
            obj.debuff_dict.clear()
            print("驱散成功")
    else:
        print("自己没有debuff")