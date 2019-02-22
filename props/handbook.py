from assist import  show,changepet

pet_handbook_dict={
    #'001':('妙蛙种子',['wood',False]),
    '004':('小火龙',['fire'],[True]),
    '005':('火恐龙',['fire'],[True]),
    #'026':('波波',['fly',False]),
    #'043':('走路草',['wood',False]),
    #'072':('毒刺水母',['water',False]),
    #'118':('角金鱼',['water',False]),

}




def showPets(player):
    for key,pet in player.pet_list.items():
        if key == 'Master':
            print('0',end=':  ') , show.showPetStatus(pet)
        else:
            print(key,end=':  ') , show.showPetStatus(pet)
        print(pet.status)
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
    print(pet)
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

def showHandBook():
    print("="*30)
    print("精灵图鉴")
    for key,value in pet_handbook_dict.items():
        if value[2][0] == False:
            print(key,':',value[0],'分类',end=':')
            showProp(value[1])
            print('未捕获！')
        else:
            print(key, ':', value[0], '分类', end=':')
            showProp(value[1])
            print('捕获！')

def showProp(value):
    for k in value:
        if k == 'fire':
            print('火', end=' ')
        elif k == 'wood':
            print('草', end=' ')
        elif k == 'fly':
            print('飞行',end=' ')
        elif k == 'water':
            print('水',end=' ')
        elif k == 'electricity':
            print('电',end=' ')
        elif k == 'rock':
            print('岩石',end=' ')
        pass

def setHandBook(key,name,prop,capture=[False]):
    pet_handbook_dict[key] = (name,prop,capture)