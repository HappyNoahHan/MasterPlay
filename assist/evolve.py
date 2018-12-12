'''
    净化表
'''

from pets import fire
from assist import  show

evolve_dict={
    '小火龙': fire.Charmeleon,
}


def isEvolve(obj):
    '''
    进化属性 重载
    :param obj:
    :return:
    '''
    inherit_skill_list = obj.skill_list
    inherit_exp_for_current = obj.exp_for_current
    inherit_realize_skill_list = obj.realize_skill_list
    inherit_carry_prop = obj.carry_prop
    new_obj = evolve_dict[obj.name](level = obj.level)


    new_obj.skill_list = inherit_skill_list
    new_obj.exp_for_current = inherit_exp_for_current
    new_obj.realize_skill_list = inherit_realize_skill_list
    new_obj.carry_prop = inherit_carry_prop
    show.showPetStatus(new_obj)
    #print(new_obj.realize_skill_list)
    return new_obj