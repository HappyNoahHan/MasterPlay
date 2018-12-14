'''
    背包
'''
from assist import show
from props import propmap
from battle import skilllistmap

bag_dict_map={
    '1':['yes','携带道具'],
    '2':['no','药品'],
    '3':['yes','精灵球'],
    '4':['yes','技能'],
    '5':['no','辅助'],
}

def showBattleBagOrNot(obj_attack):
    print("请选择使用的道具总类")
    for key,value in bag_dict_map.items():
        if value[0] == 'yes':

            print(key,':  ',value[1])
    select_id = input(">")

    if int(select_id) == 1:
        return showPropBag(obj_attack,propmap.prop_bag_dict)
    if int(select_id) == 4:
        return showSkillBag(skilllistmap.skill_bag_dict)



def showPropBag(obj_attack,dict):
    #show.showProps()
    print("编号 名称  数量")
    for key,value in dict.items():
        print(key,value[0].prop_show_name,value[1])
    print("请选择使用的道具")
    select_id = input(">")
    if obj_attack.carry_prop == None:
        #obj_attack.carry_prop = propmap.prop_bag_dict[int(select_id)]
        dict[int(select_id)][0].equipProp(obj_attack)
        dict[int(select_id)][1] -= 1
        if dict[int(select_id)][1] == 0:
            dict.pop(int(select_id))

    else:
        print('已装备了道具,请先卸载道具')
        return False
    return True

def showSkillBag(dict):
    for key,value in dict.items():
        print(key,value[0].skill_show_name,value[1])