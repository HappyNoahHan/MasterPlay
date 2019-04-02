from functools import reduce
attr_map_dict ={
    #属性克制表
    'normal':{'rock':0.5,'steel':0.5,'ghost':0},
    'fire':{'fire': 0.5,'wood': 2,'water': 0.5,'ice':2,'insect':2,'rock':0.5,'dragon':0.5,'steel':2},
    'wood':{'wood': 0.5,'fire': 0.5,'water': 2,'poison':0.5,'fly':0.5,'ground':2,'rock':2,'dragon':0.5,'steel':0.5,'insect':0.5},
    'water':{'water': 0.5,'fire': 2,'wood': 0.5,'ground':2,'rock':2,'dragon':0.5},
    'rock':{'fire':2,'ice':2,'combat':0.5,'fly':2,'ground':0.5,'insect':2,'steel':0.5},
    'fly' :{'rock': 0.5,'wood':2,'electric':0.5,'combat':2,'insect':2,'steel':0.5},
    'ground':{'fire':2,'electric':2,'wood':0.5,'poison':2,'fly':0,'insect':0.5,'rock':2,'steel':2},
    'electric':{'water':2,'wood':0.5,'electric':0.5,'ground':0,'fly':2,'dragon':0.5},
    'ice':{'fire':0.5,'water':0.5,'wood':2,'ice':0.5,'ground':2,'fly':2,'dragon':2,'steel':0.5},
    'combat':{'normal':2,'ice':2,'poison':0.5,'fly':0.5,'insect':0.5,'psychic':0.5,'rock':2,'ghost':0,'dark':2,'steel':2,'fairy':0.5},
    'poison':{'wood':2,'poison':0.5,'ground':0.5,'rock':0.5,'ghost':0.5,'steel':0,'fairy':2},
    'psychic':{'combat':2,'poison':2,'psychic':0.5,'dark':0,'steel':0.5},
    'insect':{'fire':0.5,'wood':2,'combat':0.5,'poison':0.5,'fly':0.5,'psychic':2,'ghost':0.5,'dark':2,'steel':0.5,'fairy':0.5},
    'ghost':{'normal':0,'psychic':2,'ghost':2,'dark':0.5},
    'dragon':{'dragon':2,'steel':0.5,'fairy':0},
    'dark':{'combat':0.5,'psychic':2,'ghost':2,'dark':0.5,'fairy':0.5},
    'steel':{'fire':0.5,'water':0.5,'electric':0.5,'ice':2,'rock':2,'steel':0.5,'fairy':2},
    'fairy':{'fire':0.5,'combat':2,'poison':0.5,'dragon':2,'dark':2,'steel':0.5},
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