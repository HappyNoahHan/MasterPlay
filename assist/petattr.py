attr_map_dict ={
    'fire':{'fire': 1,'wood': 1.5},
    'wood':{'wood': 1},
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