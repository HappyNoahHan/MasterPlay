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

attr_list=['普通','格斗','飞行','毒','地面','岩石','虫','幽灵',
           '钢','火','水','草','电','超能力','冰','龙','恶','妖精']
attr_code_list=['normal','combat','fly','poison','ground','rock','insect','ghost',
                'steel','fire','water','wood','electric','psychic','ice','dragon','dark','fairy']
attr_map = dict(map(lambda x,y:[x,y],attr_code_list,attr_list))

def getResistFromInitStr(resist_init_str):
    '''
    从克制表中拿到具体数值
    :param str: 克制关系字符串
    :return: 克制关系list
    '''
    resist_init_list = list(resist_init_str)
    resist_str=''
    resist_list=[]

    get_mode = 1

    for value in resist_init_list:
        if get_mode == 1:
            if value != '0':
                resist_list.append(value)
            else:
                get_mode = 2
                resist_str += value
        elif get_mode == 2:
            if value != '.':
                get_mode = 1
                resist_list.append(resist_str)
                resist_str = ''
                resist_list.append(value)
            else:
                get_mode = 3
                resist_str += value
        else:
            resist_str += value
            if value != '2':
                resist_list.append(resist_str)
                get_mode = 1
    return resist_list



def getResistance(obj):
    '''
    克制字典
    :param obj:
    :return: 克制字典
    '''
    resist_init_str = obj.getAttrRelationShip()
    resist_list = getResistFromInitStr(resist_init_str)

    #合并成字典 2种方法
    #resist_relationship = dict(map(lambda x,y:[x,y],attr_list,resist_list))
    resist_relationship = {key:value for key,value in zip(attr_list,resist_list)}

    return resist_relationship

def getAttrMap(obj_skill,obj):
    '''
    五行相克属性 修正
    :param obj_skill:
    :param obj:
    :return:
    '''

    resist_relationship = getResistance(obj)

    attr_index = resist_relationship[attr_map[obj_skill.property]]

    '''
    if 'ghost' in obj.prop and 'ST121' in obj.status:
        if obj_skill.property == 'normal' or obj_skill.property == 'combat':
            if attr_index == 0:
                attr_index = 1
    '''
    return float(attr_index)