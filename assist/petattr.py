attr_map_dict ={
    'fire':{'fire': 1,'wood': 2,'water': 0.5},
    'wood':{'wood': 1,'fire': 0.5,'water': 1},
    'water':{'water': 1,'fire': 2,'wood': 1},
    'fly' :{'stone': 2,},
    'light':{'dark': 2},
    'dark' :{'light': 2},
}


def getAttrMap(obj_skill,obj):
    '''
    五行相克属性 修正
    :param obj_skill:
    :param obj:
    :return:
    '''
    restrain_amendment = []

    for value in obj.property:
        if value not in attr_map_dict[obj_skill.property]:
            restrain_amendment.append(int(1))
        else:
            restrain_amendment.append(attr_map_dict[obj_skill.property][value])

    return max(restrain_amendment)