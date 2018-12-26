from players import play
from pets import fly,wood,fire
from battle import skill
from place import grassfrom,village

import random

class Trainer(object):
    def __init__(self,name = '',pet_list=(),can_challenge = True,prize={},info =None,has_riddle=False):
        self.name = name
        self.pet_list = pet_list
        self.can_challenge = can_challenge
        self.prize = prize
        self.has_riddle = has_riddle
        self.info = info

    def __str__(self):
        return self.info





trainer_in_grass_no_1 = {
    '迷途少女': Trainer(name='迷途少女',
                        prize={'money': 500,'精灵球': 1,'雪鹰': 1},
                        info='打败我才能开启寻宝',
                        has_riddle=True,
                        pet_list=(fly.aiPidgey(level=5,skill_list={'1': skill.scream()},has_trainer=None),
                                fly.aiPidgey(level=4, skill_list={'1': skill.scream()}, has_trainer=None))),
    '眼睛少年': Trainer(name='眼镜少年',info='听说打败迷途少女才能开启这里宝藏...',can_challenge=False),
    '不良青年': Trainer(name='不良青年',info='据说这里有个漂亮的妹子，不知道躲哪里去了...',can_challenge=False),
    '和蔼的奶奶':Trainer(name='和蔼的奶奶',info='孙女又不知道躲哪去了...',can_challenge=False),
    '单身母亲':Trainer(name='单身母亲',info='少女好像有不为人知的异能...',can_challenge=False),
    '捕虫少年':Trainer(name='捕虫少年',info='听这里有宝藏的声音...',can_challenge=False),

}


def getTrainer(dict):
    choice_list = []
    for key,value in dict.items():
        choice_list.append(key)
    if choice_list.__len__() == 0:
        return None
    choice_trainer = random.choice(choice_list)
    #dict[choice_trainer].can_challenge = False

    return dict[choice_trainer]