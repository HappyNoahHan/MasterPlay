class PetBox(object):
    #pet_list 用默认会导致用的是同一个dict
    def __init__(self,name=None,pet_list={},max_number = 16):
        self.name = name
        self.pet_list = pet_list
        self.max_number = max_number

    def setName(self,value):
        self.name = value

    def setPetList(self,pet):
        for key in range(1,self.max_number+1):
            if key not in self.pet_list:
                self.pet_list[key] = pet
                return True
        return False

    def removePet(self,pet):
        del_id = 0
        for key,item in self.pet_list.items():
            if item == pet:
                del_id = key
        self.pet_list.pop(int(del_id))

    def __str__(self):
        return self.name

pet_box_map=[
    PetBox(name='保存箱1',pet_list={}),
    PetBox(name='保存箱2',pet_list={}),
]


def putPetToBox(pet):
    for pet_box in pet_box_map:
        if pet_box.pet_list.__len__() < pet_box.max_number:
            pet_box.setPetList(pet)
            return True
    return False

def getBox(func):
    def inner():
        print("请选择保存箱！")
        return func()
    return inner

@getBox
def getPetBox():
    for key,value in enumerate(pet_box_map):
        print(key,":",value.name)
    select_id = input(">")
    if isDigt(select_id) == False:
        if select_id in 'quit':
            return None
        else:
            print("指令错误！")
            return getPetBox()
    try:
        if pet_box_map[int(select_id)] in pet_box_map:
           return pet_box_map[int(select_id)]
    except:
        print("指令错误！")
        return getPetBox()

def getOtherBox(box):
    for key,value in enumerate(pet_box_map):
        if value != box:
            print(key,':',value.name)
    print("请选择目标存储箱！")
    select_id = input(">")
    if isDigt(select_id) == False:
        if select_id in 'quit':
            return None
        else:
            print("指令错误！")
            return getPetBox()
    try:
        if pet_box_map[int(select_id)] in pet_box_map and pet_box_map[int(select_id)] != box:
            return pet_box_map[int(select_id)]
    except:
        print("指令错误!")
        return getOtherBox(box)

def getPetFromBox(box):
    for key,pet in box.pet_list.items():
        print(key,':',pet.name,'Lv%s' % pet.level)
    print("请选择精灵")
    select_id = input(">")
    if isDigt(select_id) == False:
        if select_id in 'quit':
            return None
        else:
            print("指令错误！")
            return getPetFromBox(box)

    if int(select_id) in box.pet_list:
        return box.pet_list[int(select_id)]
    else:
        print("指令错误！")
        return getPetFromBox(box)



def petBoxAction(player):
    print("=" * 30)
    print("精灵传输系统界面")
    print('1','转换')
    print('2','存入')
    print('3','取出')
    print('4','重命名')
    print('5','退出')
    print('请选择你要操作得选项')
    select_id = input(">")
    if select_id == '1':
        if changePetBox():
            pass
        else:
            return petBoxAction(player)
    elif select_id == '2':
        if getPetIntoBox(player):
            pass
        else:
            return petBoxAction(player)
    elif select_id == '3':
        if getPetOutOfBox(player):
            pass
        else:
            return petBoxAction(player)
    elif select_id == '4':
        if renameBox():
            pass
        else:
            return petBoxAction(player)
    elif select_id == '5':
        return False
    else:
        print("指令错误!")
        return petBoxAction(player)


def changePetBox():
    print("="*30)
    print("整理精灵箱")
    select_box = getPetBox()
    if select_box != None:
        select_pet = getPetFromBox(select_box)
        if select_pet != None:
            change_to_box = getOtherBox(select_box)
            if change_to_box != None:
                change_to_box.setPetList(select_pet)
                select_box.removePet(select_pet)
                print(select_pet.name,'已经被存储到',change_to_box)
    return False

def renameBox():
    print("="*30)
    print("重命名")
    select_box = getPetBox()
    if select_box != None:
        print("输入新名字")
        name = input("new name: >")
        select_box.setName(name)
    return False

def getPetOutOfBox(player):
    '''
    取出精灵
    :return:
    '''
    print("=" * 30)
    print("取出精灵")
    select_box = getPetBox()
    if select_box != None:
        select_pet = getPetFromBox(select_box)
        if select_pet != None:
            if petPetIntoPlayerPetList(player,select_pet) == False:
                print("提取失败！")
            else:
                print("提取成功！")
                select_box.removePet(select_pet)

    return False



def petPetIntoPlayerPetList(player,pet):
    if len(player.pet_list) < 6:
        for key in ['1','2','3','4','5']:
            if key not in player.pet_list:
                player.setPet(key,pet)
                print("取出 %s " % pet.name)
                return True
    else:
        print("无法携带更多的出战精灵")
        return False

def getPetIntoBox(player):
    print("=" * 30)
    print("存放")
    for key,pet in player.pet_list.items():
        if key != 'Master':
            print( key,':',pet.name,'Lv%s' % pet.level)

    print("请选择存入的精灵")
    select_pet = input("请选择>")
    if select_pet in player.pet_list:
        select_box = getPetBox()
        if select_box != None:
            if select_box.setPetList(player.pet_list[select_pet]):
                print("存放成功！")
                player.pet_list.pop(select_pet)
            else:
                print("该箱子没有足够的空间,存放失败！")
    else:
        print("指令错误!")
        return getPetIntoBox(player)
    return False


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