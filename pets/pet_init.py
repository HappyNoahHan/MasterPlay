from pets import skilltree,newpets
from battle import skilllistmap
from database import petdata
import random


def getInitSkillList(skill_init_list):
    '''
    野生精灵初始技能~
    :param pet_no:
    :return:
    '''

    skill_list = {}

    for key in skill_init_list.keys():
        for x in ['1','2','3','4']:
            if x not in skill_list:
                skill_list[x] = skilllistmap.skill_dict[key]()
                break

    return skill_list

def get_pet(pet_no,level=1):
    skill_init_list = get_init_skill_list(pet_no,level)
    skill_list = getInitSkillList(skill_init_list)
    return newpets.Pets(pet_no,level,skill_list=skill_list)

    #return pet_map.all_pet_dict[pet_no](level=level,skill_list=skill_list)

def get_skill_tree(pet_no):
    skill_tree = []
    sql = 'select * from levelUpLearnSkill where petNo=%d' % pet_no
    sql += " and learn_condition like 'Lv.%'"
    skill_msg = petdata.get_data(sql)
    #print(skill_msg)
    for msg in skill_msg:
        key  = msg[1].split('Lv.')[1].strip('-')
        value = msg[2]
        skill_tree.append((key,value))

    return skill_tree

def get_init_skill_list(pet_no,level):
    skill_list={}
    skill_tree = get_skill_tree(pet_no)

    key_list = []
    for key in skill_tree:
        if int(key[0]) < level:
            key_list.append(key)

    if key_list.__len__() > 4:
        key_list = random.sample(key_list,4)

    for value in key_list:
        sql = 'select id from skillInfo where skill_name=%s' % repr(value[1])
        skill_id = petdata.get_data(sql)
        skill_list[skill_id[0][0]] = value[1]

    return skill_list

