from pets import fly
from battle import skill
class PetBox(object):
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

    def removePet(self,pet):
        del_id = 0
        for key,item in self.pet_list.items():
            if item == pet:
                del_id = key
                print(key)
        print(del_id)
        self.pet_list.pop(int(del_id))

pet_box_map=[
    PetBox(name='保存箱1',pet_list={1:fly.aiPidgey(level=5,skill_list={'1': skill.scream()},has_trainer=None)}),
    PetBox(name='保存箱2'),
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
        else:
            print("指令错误！")
            return getPetBox()
    except:
        return None

def getPetFromBox(box):
    for key,pet in box.pet_list.items():
        print(key,':',pet.name,'Lv%s' % pet.name)
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
    else:
        return False


def changePetBox():
    select_box = getPetBox()
    if select_box != None:
        select_pet = getPetFromBox(select_box)
        if select_pet != None:
            change_to_box = getPetBox()
            if change_to_box != None:
                change_to_box.setPetList(select_pet)
                select_box.removePet(select_pet)
                print(change_to_box)
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