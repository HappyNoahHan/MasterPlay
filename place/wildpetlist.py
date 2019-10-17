from  pets import pet_init
import random

wild_pet_list={
    'MAP08':{
        #no   几率    等级范围
        '016':(50,[],range(2,6)),
        '021':(50,[],range(2,6)),
    },
    'MAP05':{
        '072':(20,[],range(7,11)),
        '118':(40,[],range(7,11)),
        '120':(40,[],range(7,11)),
    },
}


def meetWildPet(dict):
    '''
    遭遇野生精灵
    :param dict:
    :return:
    '''
    per_base = list(range(1,101))
    number = random.randint(1,100)

    for key,value in dict.items():
        value[1].clear()
        for i in range(0,value[0]):
            x = random.choice(per_base)
            value[1].append(x)
            per_base.remove(x)

    for key,value in dict.items():
        if number in value[1]:
            wild_pet_no = key
            return wild_pet_no


def getWildPet(map_id):
    '''

    :param map_id:
    :return: NUMBER AND LEVEL
    '''
    pet_no = meetWildPet(wild_pet_list[map_id])
    level = random.choice(wild_pet_list[map_id][pet_no][2])

    return pet_init.get_pet(pet_no,level=level)

