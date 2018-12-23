import pets.pet


class Fire(pets.pet.Pet):
    def __init__(self, level=1,skill_list={},exp_for_current=0,carry_prop=None,base_points_list=[0] * 6):
        super().__init__(level=level,skill_list=skill_list,exp_for_current=exp_for_current,carry_prop=carry_prop,base_points_list=base_points_list)
        self.property = ['fire']
        self.can_learn_skills = ['A','B','N','T','S','C']
        self.info = '火系神奇宝贝'

    def __str__(self):
        return self.info

class Wood(pets.pet.Pet):
    def __init__(self, level=1,skill_list={},exp_for_current=0,carry_prop=None,base_points_list=[0] * 6):
        super().__init__(level=level,skill_list=skill_list,exp_for_current=exp_for_current,carry_prop=carry_prop,base_points_list=base_points_list)

        self.property = ['wood']
        self.can_learn_skills = ['A','B','N','T','S','C']
        self.info = '木系神奇宝贝'

    def __str__(self):
        return self.info

class Fly(pets.pet.Pet):
    def __init__(self, level=1, skill_list={}, exp_for_current=0, carry_prop=None, base_points_list=[0] * 6):
        super().__init__(level=level, skill_list=skill_list, exp_for_current=exp_for_current, carry_prop=carry_prop,base_points_list=base_points_list)

        self.property = ['fly']
        self.can_learn_skills = ['A','N','F','B','T','S']
        self.info = '飞行神奇宝贝'

    def __str__(self):
        return self.info