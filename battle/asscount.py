'''
    辅助计算 包括战前 战后
'''
from battle import buff


def checkBuffBeforeBattle(obj_attack,obj_defense):
    if obj_attack.buff_dict:
        buff.buffCount(obj_attack)
        buff.buffIndex(obj_attack)
    else:
        print("没有buff")

    if obj_defense.buff_dict:
        buff.buffCount(obj_defense)


def checkCarryPropBeforeBattle(obj,value):
    pass