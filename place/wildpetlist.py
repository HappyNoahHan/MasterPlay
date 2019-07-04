from  pets import fly,wood,water,skilltree
from battle import skill
from props import berrymap
import random

wild_pet_list={
    'MAP08':{
        '026':(50,[]),
        '043':(50,[]),
    },
    'MAP05':{
        '072':(20,[]),
        '118':(40,[]),
        '120':(40,[]),
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
    pet_no = meetWildPet(wild_pet_list[map_id])

    if map_id == 'MAP08':
        if pet_no == '026':
            return fly.Pidgey(level=random.randint(2, 4), skill_list=skilltree.getInitSkillList('041'))
        else:
            return water.Seadra(level=random.randint(2, 4), skill_list=skilltree.getInitSkillList('041'))