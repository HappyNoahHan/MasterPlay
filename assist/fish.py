'''
    钓鱼功能模块
'''
from  pets import water
from battle import skill
import random
fishing_dict={
    '绿叶大道': {'129':(255,[])}
}

can_fishing_list = {
    '129': water.Magikarp(level=5,skill_list={'1': skill.scream()})
}



def fishing(place_name):
    fishing_list = fishing_dict[place_name]
    get_pet_no = getfish(fishing_list)
    return can_fishing_list[get_pet_no]


def getfish(dict):
    base = list(range(1,256))
    number = random.randint(1,255)
    for key,value in dict.items():
        value[1].clear()
        for x in range(0,value[0]):
            x = random.choice(base)
            value[1].append(x)
            base.remove(x)

    for key,value in dict.items():
        if number in value[1]:
            return key

