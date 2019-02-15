import pets.pet


class PropInit(pets.pet.Pet):
    def __init__(self, level=1,skill_list={},exp_for_current=0,carry_prop=None,base_points_list=[0] * 6,has_trainer=False,autoAi=True):
        super().__init__(level=level,skill_list=skill_list,exp_for_current=exp_for_current,carry_prop=carry_prop,base_points_list=base_points_list,has_trainer=has_trainer,autoAi=autoAi)

    name = '未知'
    style = '未知'

    def __str__(self):
        return self.style + '神奇宝贝' + ':' + self.name