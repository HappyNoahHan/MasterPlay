from props import handbook

def changePet(player):
    print("请选择你要交换的精灵！")
    for key,value in player.pet_list.items():
        print(key,':',value.name,' Lv%s' % value.level)
    print("0 : 返回！")
    select_id = input(">")

    if select_id in player.pet_list:
        #player.master_pet = player.pet_list[select_id]
        if player.pet_list[select_id].alive == True:
            backup_pet = player.pet_list['Master']
            player.setPet('Master',player.pet_list[select_id])
            player.setPet(select_id,backup_pet)
        else:
            print("精灵死亡,无法使用,请重新选择！")
            return changePet(player)
    elif select_id == '0':
        return False
    else:
        print("指令错误！重新选择！")
        return changePet(player)

    return True


def changePetAfterDie(player):
    print("=" * 30)
    alive_number = 0
    for key, value in player.pet_list.items():
        if value.alive == True:
            alive_number += 1
            print(key,":",value.name)

    if alive_number == 0:
        return False
    else:
        print("请选择精灵重新出战！")
        select_id = input(">")
        if select_id in player.pet_list:
            # player.master_pet = player.pet_list[select_id]
            if player.pet_list[select_id].alive == True:
                backup_pet = player.pet_list['Master']
                player.setPet('Master', player.pet_list[select_id])
                player.setPet(select_id, backup_pet)
            else:
                print("指令错误！重新选择！")
                return changePetAfterDie(player)
        else:
            print("指令错误！重新选择！")
            return changePetAfterDie(player)
    return True


def changePetWithNpc(player,condition,change_pet):
    '''
    与Npc 交换 精灵
    :param player:
    :return:
    '''
    current_pet_list = []
    for key,pet in player.pet_list.items():
        current_pet_list.append(pet.name)

    if condition in current_pet_list:
        print("哇 哇 哇  %s 是我的最爱 你是否愿意和我交换 %s " % (condition,change_pet.name))
        print("1 yes 2 no")
        select_id = input(">")
        if select_id == '1':
            for key,pet in player.pet_list.items():
                if pet.name == condition:
                    print(key,":",pet.name,'LV%s' % pet.level)
            print("请选择你要交换的精灵！")
            select_pet_id = input(">")
            if select_pet_id in player.pet_list:
                if player.pet_list[select_pet_id].name == condition:
                    player.setPet(select_pet_id,change_pet)
                    #player.pet_list[select_pet_id].autoAi = False
                    print("你获得了 %s lv%s" % (player.pet_list[select_pet_id].name,player.pet_list[select_pet_id].level))
                    # 将交换的精灵加入图鉴
                    if change_pet.pet_no in handbook.pet_handbook_dict:
                        if handbook.pet_handbook_dict[change_pet.pet_no][2][0] == False:
                            handbook.setHandBook(change_pet.pet_no, change_pet.name, change_pet.property,
                                                 capture=[True])
                    else:
                        handbook.setHandBook(change_pet.pet_no, change_pet.name, change_pet.property,
                                             capture=[True])
                    return True
        else:
            print("你拒绝了交换请求！")
            return False
    else:
        return False