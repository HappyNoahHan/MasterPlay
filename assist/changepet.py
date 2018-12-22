def changePet(player):
    print("请选择你要交换的精灵！")
    for key,value in player.pet_list.items():
        print(key,':',value.name)
    select_id = input(">")

    if select_id in player.pet_list:
        player.master_pet = player.pet_list[select_id]

    else:
        print("指令错误！重新选择！")
        return changePet(player)

    return True