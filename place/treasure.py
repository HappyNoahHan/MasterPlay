import random
from props import petballmap,drugmap,propmap
from battle import  skilllistmap

treasure_box_for_grass_no_1 ={
    '精灵球': [1,'normal','petball'],
    '小型回复药剂': [2,'normal','drug'],
    '灼伤解除剂': [1,'normal','drug'],
    #'火焰果':[1,'normal','drug'],
    '火焰之心':[1,'elite','prop'],
}

treasure_box_for_maelstrom_no_1 ={
    '精灵球': [3,'normal','petball'],
    '小型回复药剂': [2,'normal','drug'],
    '灼伤解除剂': [2,'normal','drug'],
    #'火焰果':[1,'normal','drug'],
    '攻击之爪':[1,'elite','prop'],
}


def getTreasureBox(place):

    kind = getWhich()

    if kind == None:
        return None
    else:
        if len(place) == 0:
            return None
        can_select_box = []
        for key,value in place.items():
            if value[1] == kind:
                can_select_box.append(key)

        if can_select_box.__len__() == 0:
            return None
        get_prop = random.choice(can_select_box)
        get_kind = place[get_prop][2]

        place[get_prop][0] -= 1
        if place[get_prop][0] == 0:
            place.pop(get_prop)

        return [get_prop,get_kind]



def getWhich():
    '''
    1-100 没有
    100-200 普通
    200-235 稀有
    235-250 精英
    250-255 传说
    :param place:
    :return:
    '''
    number = random.randint(1,255)

    if  0 < number < 101:
        return None
    elif 100 < number < 201:
        return 'normal'
    elif 200 < number < 236:
        return 'uncommon'
    elif 235 < number < 251:
        return 'elite'
    else:
        return 'legend'


def getPropsToBag(prop_name,kind,number=1):
    if kind == 'petball':
        petballmap.getPetBall(prop_name,number)
    elif kind == 'drug':
        drugmap.getDrug(prop_name,number)
    elif kind == 'prop':
        propmap.getProp(prop_name,number)
    elif kind == 'skill':
        skilllistmap.getSkill(prop_name,number)
    else:
        pass


