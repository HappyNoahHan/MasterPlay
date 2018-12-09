'''
    净化表
'''

from pets import fire
from assist import  show

evolve_dict={
    '小火龙': fire.Charmeleon(6),
}



def petEvolve():
    pass




def isEvolve(obj):
    '''
    进化属性 重载
    :param obj:
    :return:
    '''
    inherit_skill_list = obj.skill_list
    inherit_exp_for_current = obj.exp_for_current
    new_obj = evolve_dict[obj.name]


    new_obj.skill_list = inherit_skill_list
    new_obj.exp_for_current = inherit_exp_for_current
    show.showPetStatus(new_obj)
    return new_obj