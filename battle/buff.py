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
    obj.tmp_spell_power = 0
    obj.tmp_spell_defense = 0
    obj.tmp_speed = 0

    buff_remove_list = []  # buff 移除列表
    for key,value in obj.buff_dict.items():
        if key.buff_prop == 'Defense':
            if value[0] == 0:
                value[1] = 0
                buff_remove_list.append(key)
            obj.tmp_defense += round(obj.defense * value[1])

        elif key.buff_prop == 'Attack':
            if value[0] == 0:
                value[1] = 0
                buff_remove_list.append(key)
            obj.tmp_attack += round(obj.attack * value[1])

        elif key.buff_prop == 'SpellPower':
            if value[0] == 0:
                value[1] = 0
                buff_remove_list.append(key)
            obj.tmp_spell_power += round(obj.spell_power * value[1])

        elif key.buff_prop == 'SpellDefense':
            if value[0] == 0:
                value[1] = 0
                buff_remove_list.append(key)
            obj.tmp_spell_defense += round(obj.spell_defense * value[1])

        elif key.buff_prop == 'Health':
            if value[0] > 0:
                assist.life.healthRecoverBySkill(obj,key.getIndexPer()) #调用回复技能
            else:
                buff_remove_list.append(key)
        else:
            if value[0] == 0:
                value[1] = 0
                buff_remove_list.append(key)
            obj.tmp_speed += round(obj.speed * value[1])

    if buff_remove_list:
        for key in buff_remove_list:
            obj.buff_dict.pop(key)
            print("移除 %s 效果" % key.show_name)

    #战前debuff计算
    proDebuffCount(obj)


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
        print("%s 效果渐渐减弱" % key.show_name)

def damageDebuffCount(obj):
    '''
    伤害型debuff 计算
    :param obj:
    :return:
    '''
    debuff_remove_list = []
    for key,value in obj.debuff_dict.items():
        #调整系数 伤害debuff 战斗后结算
        if key.damage_debuff == True:
            index_number = assist.petattr.getAttrMap(key,obj)
            if value[0] >= 1:
                lost_health = round(obj.health * value[1] * index_number)
                obj.health -= lost_health
                print("受到 %s  %s 伤害" %(key.show_name,lost_health))
                value[0] -= 1
            else:
                debuff_remove_list.append(key)

    if debuff_remove_list:
        for key in debuff_remove_list:
            obj.debuff_dict.pop(key)
            print("移除 %s 伤害" % key.show_name)

def proDebuffCount(obj):
    '''
    属性debuff 计算
    :param obj:
    :return:
    '''
    debuff_move_list = []
    for key,value in obj.debuff_dict.items():
        if key.damage_debuff == False:
            if key.debuff_prop == 'Attack':
                if value[0] > 0:
                    tmp_attack = round(obj.attack * value[1])
                    obj.tmp_attack -= tmp_attack
                    value[0] -= 1
                else:
                    debuff_move_list.append(key)
            elif key.debuff_prop == 'Defense':
                if value[0] > 0:
                    tmp_defense = round(obj.defense * value[1])
                    obj.tmp_defense -= tmp_defense
                    value[0] -= 1
                else:
                    debuff_move_list.append(key)
            elif key.debuff_prop == 'SpellPower':
                if value[0] > 0:
                    tmp_spell_power = round(obj.spell_power * value[1])
                    obj.tmp_spell_power -= tmp_spell_power
                    value[0] -= 1
                else:
                    debuff_move_list.append(key)
            elif key.debuff_prop == 'SpellDefense':
                if value[0] > 0:
                    tmp_spell_defense = round(obj.spell_defense * value[1])
                    obj.tmp_spell_defense -= tmp_spell_defense
                    value[0] -= 1
                else:
                    debuff_move_list.append(key)

    if debuff_move_list:
        for key in debuff_move_list:
            obj.debuff_dict.pop(key)
            print("移除 %s 负面效果" % key.show_name)

def proBuffCount(obj,skill):
    '''
    属性增幅buff
    :param obj:
    :return:
    '''
    prop_buff_index = 1
    prop_buff_list = []
    if obj.property_buff:
        for key,value in obj.property_buff.items():
            if skill.property == key.property:
                prop_buff_list.append(value[1])

        prop_buff_index += sum(prop_buff_list)

    print('本属性增幅倍数: ',prop_buff_index)
    return prop_buff_index




def proBuffindex(obj):
    '''
    属性buff 每回合递减
    :param obj:
    :return:
    '''
    probuff_remove_list = []
    for key, value in obj.property_buff.items():
        if value[0] <= 0:
            probuff_remove_list.append(key)
        value[0] -= 1

    if probuff_remove_list:
        for key in probuff_remove_list:
            obj.property_buff.pop(key)
            print("移除 %s 增幅效果" % key.show_name)



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
                print("驱散  %s" % del_item[0].show_name)
        else:
            obj.buff_dict.clear()
            print("驱散成功！")
    else:
        print("对方没有buff")

    buffCount(obj)

def removeOwnDebuff(obj,num):
    '''
    清除自己的负面效果
    :param obj:
    :param num:
    :return:
    '''
    #print("使用解毒剂")
    if obj.debuff_dict:
        if num <= len(obj.debuff_dict.items()):
            for i in range(num):
                del_item = obj.debuff_dict.popitem()
                print("移除 %s 负面效果" % del_item[0].show_name)
        else:
            obj.debuff_dict.clear()
            print("驱散成功")
    else:
        print("自己没有debuff")

    return True

