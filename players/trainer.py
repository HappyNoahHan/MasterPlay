from players import play
from pets import fly,wood,fire
from battle import skill
from place import grassfrom,village

import random

class Trainer(object):
    def __init__(self,name = '',pet_list=(),can_challenge = True,prize={}):
        self.name = name
        self.pet_list = pet_list
        self.can_challenge = can_challenge
        self.prize = prize





trainer_in_grass_no_1 = {
    '迷途少女': Trainer(name='迷途少女',
                        prize={'money': 500,'精灵球': 1,'雪鹰': 1},
                        pet_list=(fly.aiPidgey(level=5,skill_list={'1': skill.scream()},has_trainer=None),
                                fly.aiPidgey(level=4, skill_list={'1': skill.scream()}, has_trainer=None))),

}


def getTrainer(dict):
    choice_list = []
    for key,value in dict.items():
        if value.can_challenge == True:
            choice_list.append(key)
    if choice_list.__len__() == 0:
        return None
    choice_trainer = random.choice(choice_list)
    #dict[choice_trainer].can_challenge = False

    return dict[choice_trainer]