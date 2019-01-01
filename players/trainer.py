from players import npc
import random

class Trainer(npc.Npc):
    def __init__(self,name = '',pet_list=(),can_challenge = False,prize={},info =None,
                 has_riddle=False,is_npc=True,pet_change=None,change_condition=None):
        super().__init__(name=name,info=info,is_npc = is_npc)
        #self.name = name
        self.pet_list = pet_list
        self.can_challenge = can_challenge
        self.prize = prize
        self.has_riddle = has_riddle
        #self.is_npc = is_npc
        self.pet_change = pet_change
        self.change_condition = change_condition
        #self.info = info

    def __str__(self):
        return self.info


def getTrainer(dict):
    choice_list = []
    for key,value in dict.items():
        #if value.name == '喷火龙爱好者':
        choice_list.append(key)
    if choice_list.__len__() == 0:
        return None
    choice_trainer = random.choice(choice_list)
#dict[choice_trainer].can_challenge = False

    return dict[choice_trainer]