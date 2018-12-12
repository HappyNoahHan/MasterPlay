'''
    进化表
    继承  技能列表  已领悟技能
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

    new_obj = evolve_dict[obj.name](level= obj.level,
                                    skill_list=obj.skill_list,
                                    exp_for_current=obj.exp_for_current,
                                    realize_skill_list=obj.realize_skill_list,
                                    status=obj.status,
                                    carry_prop=obj.carry_prop)

    show.showPetStatus(new_obj)
    print(new_obj.realize_skill_list)
    return new_obj