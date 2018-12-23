def changePet(player):
    print("请选择你要交换的精灵！")
    for key,value in player.pet_list.items():
        print(key,':',value.name)
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

