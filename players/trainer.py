from players import npc
from pets import pet_map
import random

class Trainer(npc.Npc):
    def __init__(self,name = None,can_challenge = False,prize={},info =None,
                 has_riddle=False,is_npc=True,pet_change=False,change_condition=None
                 ,trainer_id =None):
        super().__init__(name=name,info=info,is_npc = is_npc)
        #self.name = name
        #self.pet_list = pet_list  用训练大师编号
        self.can_challenge = can_challenge
        self.prize = prize
        self.has_riddle = has_riddle
        #self.is_npc = is_npc
        self.pet_change = pet_change
        self.change_condition = change_condition
        #self.info = info
        self.trainer_id = trainer_id

    def __str__(self):
        return self.info

    def getPetList(self):
        return pet_map.trainer_pet_dict[self.trainer_id]
