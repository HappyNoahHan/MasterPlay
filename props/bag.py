'''
    背包
'''
from assist import show
from props import propmap,drugmap
from battle import skilllistmap,learnskill

bag_dict_map={
    '1':['no','携带道具'],
    '2':['yes','药品'],
    '3':['yes','精灵球'],
    '4':['no','技能'],
    '5':['no','辅助'],
    '0':['both','返回上级']
}

def showBattleBagOrNot(obj_attack):
    print("请选择使用的道具总类")
    for key,value in bag_dict_map.items():
        if value[0] == 'yes' or value[0] == 'both':
            print(key,':  ',value[1])
    select_id = input(">")
    if select_id == '0':
        print("返回上级")
        return False
    elif select_id == '1':
        return showPropBag(obj_attack,propmap.prop_bag_dict)
    elif select_id == '2':
        return showDrugBag(obj_attack,drugmap.drug_bag_dict)
    elif select_id == '4':
        return showSkillBag(obj_attack,skilllistmap.skill_bag_dict)
    else:
        print("指令错误！")
        return showBattleBagOrNot(obj_attack)




def showPropBag(obj_attack,dict):
    #show.showProps()
    print("编号 名称  数量")
    for key,value in dict.items():
        print(key,value[0].prop_show_name,value[1])
    print('0','返回上级!')
    print("请选择使用的道具")
    select_id = input(">")
    if int(select_id) in dict:
        if obj_attack.carry_prop == None:
            #obj_attack.carry_prop = propmap.prop_bag_dict[int(select_id)]
            dict[int(select_id)][0].equipProp(obj_attack)
            dict[int(select_id)][1] -= 1
            if dict[int(select_id)][1] == 0:
                dict.pop(int(select_id))
        else:
            print('已装备了道具,请先卸载道具')
            return False
    elif select_id == '0':
        print("返回上级！")
        return showBattleBagOrNot(obj_attack)
    else:
        print("指令错误！")
        return showPropBag(obj_attack,dict)
    return True

def showSkillBag(obj_attack,dict):
    for key,value in dict.items():
        print(key,value[0].skill_show_name,value[1])
    print('0','返回上级！')

    print("请选择使用的道具")
    select_id = input(">")
    if int(select_id) in dict:
        if learnskill.learnSkill(obj_attack,dict[int(select_id)][0].skill_code,realize=False):
            dict[int(select_id)][1] -= 1
            if dict[int(select_id)][1] == 0:
                dict.pop(int(select_id))
        else:
            return False
    elif select_id == '0':
        print("返回上级！")
        return showBattleBagOrNot(obj_attack)
    else:
        print("指令错误!")
        return showSkillBag(obj_attack,dict)
    return True


def showDrugBag(obj_attack,dict):
    for key,value in dict.items():
        print(key,value[0].drug_show_name,value[1])
    print('0','返回上级！')

    print("请选择使用的道具")
    select_id = input(">")
    if int(select_id) in dict:
        if dict[int(select_id)][0].useDrug(obj_attack):
            dict[int(select_id)][1] -= 1
            if dict[int(select_id)][1] == 0:
                dict.pop(int(select_id))
        else:
            return False
    elif select_id == '0':
        print("返回上级！")
        return showBattleBagOrNot(obj_attack)
    else:
        print("指令错误!")
        return showDrugBag(obj_attack,dict)
    return True