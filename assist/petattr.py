from functools import reduce
attr_map_dict ={
    #属性克制表
    'normal':{'rock':0.5,'steel':0.5,'ghost':0},
    'fire':{'fire': 0.5,'wood': 2,'water': 0.5,'ice':2,'insect':2,'rock':0.5,'dragon':0.5,'steel':2},
    'wood':{'wood': 0.5,'fire': 0.5,'water': 2,'poison':0.5,'fly':0.5,'ground':2,'rock':2,'dragon':0.5,'steel':2},
    'water':{'water': 0.5,'fire': 2,'wood': 0.5,'ground':2,'rock':2,'dragon':0.5},
    'rock':{'fire':2,'ice':2,'combat':0.5,'fly':2,'ground':0.5,'insect':2,'steel':0.5},
    'fly' :{'rock': 0.5,'wood':2,'electric':0.5,'combat':2,'insect':2,'steel':0.5},
    'ground':{'fire':2,'electric':2,'wood':0.5,'poison':2,'fly':0,'insect':0.5,'rock':2,'steel':2},
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
    try:
        for value in obj.prop:
            if value not in attr_map_dict[obj_skill.property]:
                restrain_amendment.append(int(1))
            else:
                restrain_amendment.append(attr_map_dict[obj_skill.property][value])
    except KeyError:
        print("测试代码,属性克制类型未添加！")
        restrain_amendment.append(1)

    #匿名函数+reduce 得到个元素乘积
    attr_index = reduce(lambda x,y:x*y,restrain_amendment)

    if 'ghost' in obj.prop and 'ST121' in obj.status:
        if obj_skill.property == 'normal' or obj_skill.property == 'combat':
            if attr_index == 0:
                attr_index = 1

    return attr_index