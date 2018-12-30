from assist import  show,changepet

def showPets(player):
    for key,pet in player.pet_list.items():
        if key == 'Master':
            print('0',end=':  ') , show.showPetStatus(pet)
        else:
            print(key,end=':  ') , show.showPetStatus(pet)
    print()
    print("请选择你要详细查看的精灵或者退出(其他输入)!")
    select_id = input(">")
    if select_id in player.pet_list:
        detail(player.pet_list[select_id])
    elif select_id == '0':
        print("主战精灵信息:")
        #print("="*30)
        detail(player.pet_list['Master'])
    else:
        return False

    if select_id != '0':
        print("是否需要把当前精灵设置为主战精灵? 1 yes other no")
        changer_or_not = input(">")
        if changer_or_not == '1':
            print('ssdhskd')
            backup_pet = player.pet_list['Master']
            player.setPet('Master',player.pet_list[select_id])
            player.setPet(select_id,backup_pet)
    return showPets(player)




def detail(pet):
    print("="*30)
    print("%s 的详细信息:" % pet.name)
    #性格 等等等后续
    print("技能列表:")
    for key,skill in pet.skill_list.items():
        print(key,':',skill.show_name,'PP:',skill._pp_value_max, end=" || ")
        print('技能描叙:',skill)
    print()

    print('携带物:')
    if pet.carry_prop != None:
        print(pet.carry_prop.name)
    else:
        print('None')

