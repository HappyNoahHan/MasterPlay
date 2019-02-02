from battle import skilllistmap
import random


pet_skill_tree = {
    '026':{ '2' : 'N001',
            '5' : 'N002',
    },
    '118':{ '5': 'D002',
            '12': 'D003',
            },

}


def getSkillList(pet_no,pet_level):
    skill_code_list = []
    #skill_init_list = []
    pet_can_get_skill_list = pet_skill_tree[pet_no]
    for key,value in pet_can_get_skill_list.items():
        if pet_level >= int(key):
            skill_code_list.append(value)

    if skill_code_list.__len__() >= 4:
        skill_init_list = random.sample(skill_code_list,4)
    else:
        skill_init_list = skill_code_list.copy()

    skill_list = {}

    for key in skill_init_list:
        for x in ['1','2','3','4']:
            if x not in skill_list:
                skill_list[x] = skilllistmap.skill_dict[key]()
                break

    return skill_list





