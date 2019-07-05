from pets import skilltree,pet_map
from battle import skilllistmap
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

    return pet_map.all_pet_dict[pet_no](level=level,skill_list=skill_list)

