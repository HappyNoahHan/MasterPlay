from pets import fly,wood,fire
from battle import skill
from place import grassfrom,village

import random

class Trainer(object):
    def __init__(self,name = '',pet_list=(),can_challenge = False,prize={},info =None,
                 has_riddle=False,is_npc=True,pet_change=None,change_condition=None):
        self.name = name
        self.pet_list = pet_list
        self.can_challenge = can_challenge
        self.prize = prize
        self.has_riddle = has_riddle
        self.is_npc = is_npc
        self.pet_change = pet_change
        self.change_condition = change_condition
        self.info = info

    def __str__(self):
        return self.info



trainer_in_grass_no_1 = {
    '迷途少女': Trainer(name='迷途少女',
                        prize={'money': 500,'精灵球': 1,'雪鹰': 1},
                        info='打败我才能开启寻宝',
                        can_challenge=True,
                        has_riddle=True,
                        is_npc = False,
                        pet_list=(fly.aiPidgey(level=5,skill_list={'1': skill.scream()},has_trainer=None),
                                fly.aiPidgey(level=4, skill_list={'1': skill.scream()}, has_trainer=None))),
    '眼睛少年': Trainer(name='眼镜少年',info='听说打败迷途少女才能开启这里宝藏...',),
    '不良青年': Trainer(name='不良青年',info='据说这里有个漂亮的妹子，不知道躲哪里去了...',),
    '和蔼的奶奶': Trainer(name='和蔼的奶奶',info='孙女又不知道躲哪去了...',prize={'精灵球':1}),
    '单身母亲': Trainer(name='单身母亲',info='少女好像有不为人知的异能...',),
    '捕虫少年': Trainer(name='捕虫少年',info='听这里有宝藏的声音...',),
    '喷火龙爱好者':Trainer(name='喷火龙爱好者',info='喷火龙Max！！！',
                     pet_change=fly.aiPidgey(level=99,skill_list={'1': skill.scream()},has_trainer=True,autoAi=False),
                     change_condition='火恐龙'),

}


def getTrainer(dict):
    choice_list = []
    for key,value in dict.items():
        if value.name == '迷途少女':
            choice_list.append(key)
    if choice_list.__len__() == 0:
        return None
    choice_trainer = random.choice(choice_list)
#dict[choice_trainer].can_challenge = False

    return dict[choice_trainer]