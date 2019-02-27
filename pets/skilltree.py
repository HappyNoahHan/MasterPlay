from battle import skilllistmap
import random


pet_skill_tree = {
    '023':{
        'init': ['N007','N008'],
        4: 'P004',
        9: 'T003',
        12: 'N009',
        17: 'N006',
        20: 'P005',
        25: ['N010','N011','N012'],
        28: 'P006',
        33: 'E002',
        36: 'P007',
        38: 'P008',
        41: 'I001',
        44: 'P009',
        49: 'P010',
    },
    '024': {
        'init': ['N007', 'N008','T004','I002','H001','A002','P004','T003'],
        'evolve':['T004'],
        4: 'P004',
        9: 'T003',
        12: 'N009',
        17: 'N006',
        20: 'P005',
        27: ['N010', 'N011', 'N012'],
        32: 'P006',
        39: 'E002',
        44: 'P007',
        48: 'P008',
        51: 'I001',
        56: 'P009',
        63: 'P010',
    },
    '026':{ '2' : 'N001',
            '5' : 'N002',
    },
    '118':{ '5': 'D002',
            '12': 'D003',
            },
    '041':{
        'init': ['B006'],
        5: 'N003',
        7: 'Q002',
        11: 'T003',
        13: 'F002',
        17: 'Q001',
        19: 'F004',
        23: 'N004',
        25: 'P002',
        29: 'N005',
        31: 'C003',
        35: 'I001',
        37: 'P003',
        41: 'F003',
    },
    '042':{
        'init':['B006','Q002','T003','N003','N006'],
        'evolve':['T004'],
        5:'N003',
        7: 'Q002',
        11: 'T003',
        13: 'F002',
        17: 'Q001',
        19: 'F004',
        24: 'N004',
        27: 'P002',
        32: 'N005',
        35: 'C003',
        40: 'I001',
        43: 'P003',
        48: 'F003',

    },

}


def getInitSkillList(pet_no):
    '''
    野生精灵初始技能~
    :param pet_no:
    :return:
    '''
    skill_init_list = pet_skill_tree[pet_no]['init'].copy()

    if skill_init_list.__len__() >= 4:
        skill_init_list = random.sample(skill_init_list,4)

    skill_list = {}

    for key in skill_init_list:
        for x in ['1','2','3','4']:
            if x not in skill_list:
                skill_list[x] = skilllistmap.skill_dict[key]()
                break

    return skill_list





