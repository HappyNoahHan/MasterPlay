'''
    背包
'''
from assist import show
from props import propmap,drugmap,petballmap,handbook
from battle import skilllistmap,learnskill
from players import price

bag_dict_map={
    '1':['no','携带道具'],
    '2':['yes','药品'],
    '3':['yes','精灵球'],
    '4':['no','技能'],
    '5':['no','辅助'],
    '0':['both','关闭背包'],
}

def showBattleBagOrNot(player,obj_defense):
    print("=" * 30)
    print("战斗背包界面")
    print("=" * 30)
    print("请选择使用的道具总类")
    for key,value in bag_dict_map.items():
        if value[0] == 'yes' or value[0] == 'both':
            print(key,':  ',value[1])
    print("金钱: %s" % player.money)
    select_id = input(">")
    if select_id == '0':
        print("返回上级")
        return None
    #elif select_id == '1':
    #    return showPropBag(obj_attack,obj_defense,propmap.prop_bag_dict)
    elif select_id == '2':
        return showBattleDrugBag(player,obj_defense,drugmap.drug_bag_dict)
    elif select_id == '3':
        return showBattlePetBallBag(player,obj_defense,petballmap.petball_bag_dict)
    #elif select_id == '4':
    #    return showSkillBag(obj_attack,obj_defense,skilllistmap.skill_bag_dict)
    else:
        print("指令错误！")
        return showBattleBagOrNot(player,obj_defense)


def showBag(player):
    print("=" * 30)
    print("背包界面")
    print("=" * 30)
    for key,value in bag_dict_map.items():
        print(key,":",value[1])
    print("金钱: %s" % player.money)
    print("请输入指令")
    select_id = input(">")
    if select_id == '1':
        return showPropBag(player,propmap.prop_bag_dict)
    elif select_id == '4':
        return showSkillBag(player,skilllistmap.skill_bag_dict)
    elif select_id == '2':
        return showDrugBag(player,drugmap.drug_bag_dict)
    elif select_id == '3':
        return showPetBallBag(player,petballmap.petball_bag_dict)
    elif select_id == '0':
        return False
    else:
        print("指令错误！")
        return showBag(player)

def showPropBag(player,dict):
    #show.showProps()
    print("=" * 30)
    print("携带物品界面")
    print("=" * 30)
    print("编号 名称  数量")
    for key,value in dict.items():
        print(key,value[0].show_name,value[1])
    print('0','返回上级!')
    print("请选择道具")
    select_id = input(">")
    try:
        if int(select_id) in dict:
            if useOrSell():
                pet = selectPet(player)
                if pet.carry_prop == None:
                    #obj_attack.carry_prop = propmap.prop_bag_dict[int(select_id)]
                    dict[int(select_id)][0].equipProp(pet)
                    dict[int(select_id)][1] -= 1
                    if dict[int(select_id)][1] == 0:
                        dict.pop(int(select_id))
                else:
                    print('已装备了道具,请先卸载道具')
            else:

                sellProps(player,dict,int(select_id))

        elif select_id == '0':
            print("返回上级！")
        else:
            print("指令错误！")
            return showPropBag(player, dict)
    except ValueError:
        print("指令错误！")
        return showPropBag(player, dict)
    return showBag(player)

def showSkillBag(player,dict):
    print("=" * 30)
    print("技能学习物品界面")
    print("=" * 30)
    for key,value in dict.items():
        print(key,value[0].show_name,value[1])
    print('0','返回上级！')
    print("请选择使用的道具")
    select_id = input(">")
    try:
        if int(select_id) in dict:
            if useOrSell():
                pet = selectPet(player)
                if learnskill.learnSkill(pet,dict[int(select_id)][0].skill_code,realize=False):
                    dict[int(select_id)][1] -= 1
                    if dict[int(select_id)][1] == 0:
                        dict.pop(int(select_id))
                else:
                    print("%s 无法学习！" % pet.name)
            else:
                sellProps(player,dict,int(select_id))

        elif select_id == '0':
            print("返回上级！")
        else:
            print("指令错误!")
            return showSkillBag(player,dict)
    except ValueError:
        print("指令错误!")
        return showSkillBag(player, dict)
    return showBag(player)

def showBattleDrugBag(player,obj_defense,dict):
    print("=" * 30)
    print("药品界面")
    print("=" * 30)
    for key,value in dict.items():
        print(key,value[0].show_name,value[1])
    print('0','返回上级！')

    print("请选择使用的道具")
    select_id = input(">")
    try:
        if int(select_id) in dict:
            pet = selectPet(player)
            if dict[int(select_id)][0].useDrug(pet):
                dict[int(select_id)][1] -= 1
                if dict[int(select_id)][1] == 0:
                    dict.pop(int(select_id))
            else:
                return False
        elif select_id == '0':
            print("返回上级！")
            return showBattleBagOrNot(player,obj_defense)
        else:
            print("指令错误!")
            return showBattleDrugBag(player,obj_defense,dict)
    except ValueError:
        print("指令错误!")
        return showBattleDrugBag(player, obj_defense, dict)
    return True

def showDrugBag(player,dict):
    print("=" * 30)
    print("药品界面")
    print("=" * 30)
    for key,value in dict.items():
        print(key,value[0].show_name,value[1])
    print('0','返回上级！')

    print("请选择使用的道具")
    select_id = input(">")
    try:
        if int(select_id) in dict:
            if useOrSell():
                pet = selectPet(player)
                if dict[int(select_id)][0].useDrug(pet):
                    dict[int(select_id)][1] -= 1
                    if dict[int(select_id)][1] == 0:
                        dict.pop(int(select_id))
                else:
                    return False
            else:
                sellProps(player,dict,int(select_id))
        elif select_id == '0':
            print("返回上级！")

        else:
            print("指令错误!")
            return showDrugBag(player,dict)
    except ValueError:
        print("指令错误!")
        return showDrugBag(player, dict)
    return showBag(player)




def showBattlePetBallBag(player,obj_defense,dict):
    print("=" * 30)
    print("精灵球界面")
    print("=" * 30)
    for key,value in dict.items():
        print(key,value[0].show_name,value[1])
    print('0','返回上级！')

    print("请选择使用的道具")
    select_id = input(">")
    try:
        if int(select_id) in dict:
            dict[int(select_id)][1] -= 1
            if dict[int(select_id)][0].usePetBall(obj_defense):
                # 将未捕获的精灵加入图鉴
                if obj_defense.pet_no in handbook.pet_handbook_dict:
                    if handbook.pet_handbook_dict[obj_defense.pet_no][2][0] == False:
                        handbook.setHandBook(obj_defense.pet_no, obj_defense.name, obj_defense.property,capture=[True])
                obj_defense.captured = True
                if dict[int(select_id)][1] == 0:
                    dict.pop(int(select_id))
                return True
            else:
                if dict[int(select_id)][1] == 0:
                    dict.pop(int(select_id))
                return False
        elif select_id == '0':
            print("返回上级！")
            return showBattleBagOrNot(player,obj_defense)
        else:
            print("指令错误!")
            return showBattlePetBallBag(player,obj_defense,dict)
    except ValueError:
        print("指令错误!")
        return showBattlePetBallBag(player, obj_defense, dict)

def showPetBallBag(player,dict):
    print("=" * 30)
    print("精灵球界面")
    print("=" * 30)
    for key,value in dict.items():
        print(key,value[0].show_name,value[1])
    print('0','返回上级！')
    print("请选择道具")
    select_id = input(">")
    try:
        if int(select_id) in dict:
            sellProps(player,dict,int(select_id))
            return showBag(player)
        elif select_id == '0':
            print("返回上级")
            return showBag(player)
        else:
            print("指令错误！")
            return showPetBallBag(player,dict)
    except ValueError:
        print("指令错误！")
        return showPetBallBag(player, dict)

def selectPet(player):
    print("请选择使用的精灵！")
    for key, pet in player.pet_list.items():
        print(key, ":", pet.name)
    pet_id = input(">")
    if pet_id == '0':
        pet_id = 'Master'
    if pet_id in player.pet_list:
        return player.pet_list[pet_id]
    else:
        print("指令错误！")
        return selectPet(player)


def useOrSell():
    print("请选择使用或售卖 1 Use others Sell" )
    select_id = input(">")
    if select_id == '1':
        return True
    else:
        return False

def sellProp(player,prop):
    print("出售 %s" % prop[0].show_name)
    print("售卖的个数")
    number = input(">")

    if int(number) <= prop[1]:
        get_money = getSellMoney(prop[0].show_name,int(number))
        if get_money > 0:
            player.money += get_money
            print("money:", player.money)
            prop[1] -= int(number)
    else:
        print("没有足够的数量售卖")
        return sellProp(player,prop)


def sellProps(player,dict,id):
    sellProp(player,dict[id])
    if dict[id][1] == 0:
        dict.pop(id)


def getSellMoney(prop_name,number):
    if prop_name not in price.props_price:
        print("道具不可出售")
        return 0
    else:
        if price.props_price[prop_name][0] == None:
            print("道具不可出售")
            return 0
        return price.props_price[prop_name][1] * number

def isDigt(x):
    '''
    判断是否是数字
    :param x:
    :return:
    '''
    try:
        x = int(x)
        return isinstance(x,int)
    except:
        return False