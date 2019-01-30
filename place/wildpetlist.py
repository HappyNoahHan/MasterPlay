from  pets import fly,wood,skilltree
from battle import skill
import random

wild_pet_list_in_grass_no_1 ={
    '026': (127,'grass_no1',[]),
    '043': (128,'grass_no1',[]),
}

def meetWildPet(dict):
    '''
    遭遇野生精灵
    :param dict:
    :return:
    '''
    per_base = list(range(1, 256))
    number = random.randint(1,255)

    for key,value in dict.items():
        value[2].clear()
        for i in range(0,value[0]):
            x = random.choice(per_base)
            value[2].append(x)
            per_base.remove(x)

    for key,value in dict.items():
        if number in value[2]:
            wild_pet_no = key
            return wild_pet_no,value[1]


def getWildPet(pet_list):
    pet_no,place = meetWildPet(pet_list)

    if pet_no == '043':
        if place == 'grass_no1':
            return wood.aiOodish(level=random.randint(5, 7), skill_list={'1': skill.scream()})
    elif pet_no == '026':
        if place == 'grass_no1':
            return fly.aiPidgey(level=random.randint(3, 5), skill_list={'1': skill.scream()})
            #return fly.aiPidgey(level=5,skill_list = skilltree.getSkillList('026',5))
