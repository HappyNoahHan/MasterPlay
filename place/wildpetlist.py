from  pets import fly,wood,water,skilltree
from battle import skill
import random

wild_pet_list_in_grass_no_1 ={
    '026': (127,'grass_no1',[]),
    '043': (128,'grass_no1',[]),
}

wild_pet_list_in_maelstrom_no_1={
    '072': (51,'maelstrom_no1',[]),
    '118': (102,'maelstrom_no1',[]),
    '120': (102,'maelstrom_no1',[]),
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


    if pet_no == '026':
        if place == 'grass_no1':
            return fly.Pidgey(level=random.randint(2, 4),skill_list = skilltree.getInitSkillList('041'))
    elif pet_no == '043':
        if place == 'grass_no1':
            #return wood.Oodish(level=random.randint(2, 4),skill_list = skilltree.getInitSkillList('041'))
            return water.Seadra(level=random.randint(2, 4), skill_list=skilltree.getInitSkillList('041'))
    elif pet_no == '069':
        if place == 'grass_no2':
            return wood.Bellsprout(level=random.randint(6,8),skill_list={'1':skill.azorLeaf(),'2':skill.StunSpore()})

    elif pet_no == '072':
        if place == 'maelstrom_no1':
            return water.Tentacool(level=random.randint(10,12),skill_list={'1':skill.WaterGun()})

    elif pet_no == '118':
        if place == 'maelstrom_no1':
            return water.Goldeen(level=random.randint(11,13),skill_list={'1':skill.WaterGun(),'2':skill.WaterGun()})

    elif pet_no == '120':
        if place == 'maelstrom_no1':
            return water.Staryu(level=random.randint(11, 13),skill_list={'1': skill.WaterGun(), '2': skill.WaterGun()})
