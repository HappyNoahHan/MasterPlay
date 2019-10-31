from pets import skilltree,newpets
from battle import skilllistmap
from database import petdata
import random


def getInitSkillList(pet_no):
    '''
    野生精灵初始技能~
    :param pet_no:
    :return:
    '''

    skill_init_list = skilltree.pet_skill_tree[pet_no]['init'].copy()

    if skill_init_list.__len__() >= 4:
        skill_init_list = random.sample(skill_init_list,4)

    skill_list = {}

    for key in skill_init_list:
        for x in ['1','2','3','4']:
            if x not in skill_list:
                skill_list[x] = skilllistmap.skill_dict[key]()
                break

    return skill_list

def get_pet(pet_no,level=1):

    skill_list = getInitSkillList(pet_no)
    return newpets.Pets(int(pet_no),level,skill_list=skill_list)

    #return pet_map.all_pet_dict[pet_no](level=level,skill_list=skill_list)

def get_skill_tree(pet_no):
    skill_tree = []
    skill_msg = petdata.get_learn_skill(pet_no)
    for msg in skill_msg:
        key  = msg[1].split('Lv.')[1].strip('-')
        value = msg[2]
        skill_tree.append((key,value))

    return skill_tree

def get_init_skill_list(pet_no,level):
    skill_tree = get_skill_tree(pet_no)

    key_list = []
    for key in skill_tree:
        if int(key[0]) < level:
            key_list.append(key)

    if key_list.__len__() > 4:
        key_list = random.sample(key_list,4)

    return key_list

