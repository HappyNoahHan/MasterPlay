import random

def randomRange():
    '''
    概率随机数
    :return:
    '''
    x = random.randint(1,100)
    if x in range(1,71):
        return 1
    elif x in range(71,81):
        return 2
    elif x in range(81,91):
        return 3
    else:
        return 4

def statusRandom(value):
    x = random.randint(1,100)

    if x <= value:
        return True
    else:
        return False


def getIndiValue():
    indi_list = []

    for i in range(6):
        indi_list.append(random.randint(1,31))

    return indi_list

def canChoiceList(obj):
    choice_list = []

    for key,skill in obj.skill_list.items():
        if 'ST122' not in obj.status:
            if obj.skill_list[key].use_condition != None:
                if obj.skill_list[key].use_condition in obj.status:
                    choice_list.append(key)
            else:
                if not skill.lock:
                    choice_list.append(key)
        else:
            if skill.spell_skill != None:
                if obj.skill_list[key].use_condition != None:
                    if obj.skill_list[key].use_condition in obj.status:
                        choice_list.append(key)
                else:
                    if not skill.lock:
                        choice_list.append(key)


    return choice_list

#多段技能触发几段
def getStepOfSkill():
    num = random.randint(1,100)

    if num < 34:
        return 2
    elif 33 < num < 67:
        return 3
    elif 66 < num < 84:
        return 4
    else:
        return 5
