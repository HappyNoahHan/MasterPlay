'''
    钓鱼功能模块
'''
from  pets import pet_init
import random

all_fish_dict = {
    'MAP05' : {
        '072': (255,[],5),
    },
}



def fishing(map_id):
    fishing_list = all_fish_dict[map_id]
    pet_no = getPetNo(fishing_list)
    level = all_fish_dict[map_id][pet_no][2]
    return pet_init.get_pet(pet_no,level=level)


def getPetNo(dict):
    base = list(range(1,256))
    number = random.randint(1,255)
    for key,value in dict.items():
        value[1].clear()
        for x in range(0,value[0]):
            x = random.choice(base)
            value[1].append(x)
            base.remove(x)

    for key,value in dict.items():
        if number in value[1]:
            return key

