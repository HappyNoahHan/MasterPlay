from players import trainer,npc
from pets import fly,fire,wood
from battle import skill

trainer_in_grass_no_1 = {
    '迷途少女': trainer.Trainer(name='迷途少女',
                        prize={'money': 500,'精灵球': 1,'雪鹰': 1},
                        info='打败我才能开启寻宝',
                        can_challenge=True,
                        has_riddle=True,
                        is_npc = False,
                        pet_list=(fly.aiPidgey(level=5,skill_list={'1': skill.scream()},has_trainer=None),
                                fly.aiPidgey(level=4, skill_list={'1': skill.scream()}, has_trainer=None))),
    '眼睛少年': trainer.Trainer(name='眼镜少年',info='听说打败迷途少女才能开启这里宝藏...',),
    '不良青年': trainer.Trainer(name='不良青年',info='据说这里有个漂亮的妹子，不知道躲哪里去了...',),
    '和蔼的奶奶': trainer.Trainer(name='和蔼的奶奶',info='孙女又不知道躲哪去了...',prize={'精灵球':1}),
    '单身母亲': trainer.Trainer(name='单身母亲',info='少女好像有不为人知的异能...',),
    '捕虫少年': trainer.Trainer(name='捕虫少年',info='听这里有宝藏的声音...',),
    '喷火龙爱好者':trainer.Trainer(name='喷火龙爱好者',info='喷火龙Max！！！',
                     pet_change=fly.aiPidgey(level=99,skill_list={'1': skill.scream()},has_trainer=True,autoAi=False),
                     change_condition='火恐龙'),

}

shop_list_for_green_town_petball={
    '1': ('精灵球',100),
}
shop_npc_list_for_green_town = {
    '1': npc.ShopNpc(name='精灵球售卖员', info='我有球，你要吗？', sell_list=shop_list_for_green_town_petball, sell_type='petball')
}



hospital_npc_list_for_green_town = {
    '1': npc.Hosptial(name='小琪小姐',info='我是绿叶镇的治疗师,你可能见过我的很多姐妹。')
}