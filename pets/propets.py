import pets.pet
import battle.skill
from assist import rancom

class Fire(pets.pet.Pet):
    def __init__(self, level=1,skill_list={},exp_for_current=0,realize_skill_list=[],status=[],carry_prop=None,indi_list=rancom.getIndiValue(),base_points_list=[0] * 6):
        super().__init__(level=level,skill_list=skill_list,exp_for_current=exp_for_current,realize_skill_list=realize_skill_list,status=status,carry_prop=carry_prop,indi_list=indi_list,base_points_list=base_points_list)
        self.property = ['fire']
        self.can_learn_skills = ['A','B','N','T','S','C']
        self.info = '火系神奇宝贝'

    def __str__(self):
        return self.info

class Wood(pets.pet.Pet):
    def __init__(self, level=1,skill_list={},exp_for_current=0,realize_skill_list=[],status=[],carry_prop=None,indi_list=rancom.getIndiValue(),base_points_list=[0] * 6):
        super().__init__(level=level,skill_list=skill_list,exp_for_current=exp_for_current,realize_skill_list=realize_skill_list,status=status,carry_prop=carry_prop,indi_list=indi_list,base_points_list=base_points_list)

        self.property = ['wood']
        self.can_learn_skills = ['A','B','N','T','S','C']
        self.info = '木系神奇宝贝'

    def __str__(self):
        return self.info

class Fly(pets.pet.Pet):
    def __init__(self, level=1,skill_list={},exp_for_current=0,realize_skill_list=[],status=[],carry_prop=None,indi_list=rancom.getIndiValue(),base_points_list=[0] * 6):
        super().__init__(level=level,skill_list=skill_list,exp_for_current=exp_for_current,realize_skill_list=realize_skill_list,status=status,carry_prop=carry_prop,indi_list=indi_list,base_points_list=base_points_list)

        self.property = ['fly']
        self.can_learn_skills = ['A','N','F','B','T','S']
        self.info = '飞行神奇宝贝'

    def __str__(self):
        return self.info