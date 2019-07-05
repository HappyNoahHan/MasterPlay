import random
from props import petballmap,drugmap,propmap
from battle import  skilllistmap

treasure_dict={
    'MAP08' : {
        '精灵球': [1,'normal','petball'],
        '小型回复药剂': [2,'normal','drug'],
        '灼伤解除剂': [1,'normal','drug'],
        #'火焰果':[1,'normal','drug'],
        '火焰之心':[1,'elite','prop'],
    },
    'MAP05' : {
        '精灵球': [3,'normal','petball'],
        '小型回复药剂': [2,'normal','drug'],
        '灼伤解除剂': [2,'normal','drug'],
        #'火焰果':[1,'normal','drug'],
        '攻击之爪':[1,'elite','prop'],
    },
}

def getTreasureBox(map_id):

    kind = getWhich()

    if kind == None:
        return None
    else:
        try:
            can_select_box = []
            for key,value in treasure_dict[map_id].items():
                if value[1] == kind:
                    can_select_box.append(key)
        except KeyError:
            return None

        if can_select_box.__len__() == 0:
            return None

        get_prop = random.choice(can_select_box)
        get_kind = treasure_dict[map_id][get_prop][2]

        treasure_dict[map_id][get_prop][0] -= 1
        if treasure_dict[map_id][get_prop][0] == 0:
            treasure_dict[map_id].pop(get_prop)

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


