'''
首先求出A

A=（最大ＨＰ×3-当前ＨＰ×2）×捕获率×捕获修正⁄最大ＨＰ×3+状态修正
捕获修正是指精灵球的捕获率修正
状态修正：
冰冻、睡眠：+10
中毒、灼伤、麻痹：+5
系统在0～255之间产生一个随机数，当该数小于A时，捕获成功。

当最大ＨＰ×3大于255，则（最大ＨＰ×3）和（当前ＨＰ×2）都取原值的1/4，如果后者为零，则强制修正为1。这个减法本身有可能导致溢出。
'''
import random

def captureOrNot(obj_defense,capture_index,status_index = 0):
    if obj_defense.captured == True:
        print("%s 不可捕获" % obj_defense)
        return False
    if 'ST001' in obj_defense.status:
        status_index += 5
    if 'ST003' in obj_defense.status or 'ST002' in obj_defense.status:
        status_index += 10

    if obj_defense._max_health * 3 > 255:
        base_capt = ((obj_defense._max_health * 3 / 4 - obj_defense.health * 2 / 4) * obj_defense.capture_rate * capture_index) / ((obj_defense._max_health * 3) + status_index)
    else:
        base_capt = ((obj_defense._max_health * 3  - obj_defense.health * 2 ) * obj_defense.capture_rate * capture_index )/ (( obj_defense._max_health * 3) + status_index)
    print("基础捕获",base_capt)

    random_number = random.randint(0,255)

    if random_number < int(base_capt):
        print("捕获 %s 成功！" % obj_defense.name)
        return True
    else:
        print("捕获失败")
        return False

def addPetOrNot(player,wild_pet):
    '''
    加入精灵组
    :param player:
    :param wild_pet:
    :return:
    '''
    wild_pet.has_trainer = True
    wild_pet.autoAi = False
    wild_pet.captured = True
    wild_pet.basic_point_getter = None

    print("是否给新精灵命名 1 yes 2 no")
    select_id = input(">")
    if select_id == '1':
        print("请输入新的名字")
        wild_pet.name = input()


    for key in ['1','2','3','4','5','6']:
        if key not in player.pet_list:
            player.pet_list[key] = wild_pet
            return True
        else:
            #传输到保存箱
            pass

    return True