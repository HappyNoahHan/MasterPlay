from players import trainer,npc
from pets import fly,fire,wood,water,skilltree,rock
from battle import skill
#has_trainter = None 指npc 精灵
trainer_in_grass_no_1 = {
    '迷途少女': trainer.Trainer(name='迷途少女',
                        prize={'money': 500,'精灵球': 1},
                        info='打败我才能开启寻宝',
                        can_challenge=True,
                        has_riddle=True,
                        is_npc = False,
                        pet_list=(fly.Pidgey(level=5,skill_list={'1': skill.fireBall()},has_trainer=None),
                                fly.Pidgey(level=4, skill_list={'1': skill.fireBall()}, has_trainer=None))),
    '眼睛少年': trainer.Trainer(name='眼镜少年',info='听说打败迷途少女才能开启这里宝藏...',),
    '不良青年': trainer.Trainer(name='不良青年',info='据说这里有个漂亮的妹子，不知道躲哪里去了...',),
    '和蔼的奶奶': trainer.Trainer(name='和蔼的奶奶',info='孙女又不知道躲哪去了...',prize={'精灵球':1}),
    '单身母亲': trainer.Trainer(name='单身母亲',info='少女好像有不为人知的异能...',),
    '捕虫少年': trainer.Trainer(name='捕虫少年',info='听这里有宝藏的声音...',),
}

trainer_in_maelstrom_no_1 = {
    '游泳少年': trainer.Trainer(name='游泳少年',
                            prize={'money':600},
                            info='游泳更健康',
                            can_challenge=True,
                            is_npc = False,
                            pet_list=(water.Tentacool(level=12,skill_list={'1':skill.WaterBall()},has_trainer=None),),
                            ),
    '金鱼妹妹':trainer.Trainer(name='金鱼妹妹',
                           prize={'money':700},
                           info='我的金鱼最可爱',
                           can_challenge=True,
                           is_npc=False,
                           pet_list=(water.Goldeen(level=11,skill_list={'1':skill.WaterBall()},has_trainer=None),
                                     water.Goldeen(level=12,skill_list={'1':skill.WaterBall(),'2':skill.WaterCannon()},has_trainer=None))
                           ),
    '游泳健将': trainer.Trainer(name="游泳健将",
                            prize={'money':700,'激流球':1},
                            info='看我这肌肉!你羡慕吗？跟我学吧！！！',
                            can_challenge=True,
                            is_npc=False,
                            pet_list=(water.Horsea(level=12,skill_list={'1':skill.WaterCannon()},has_trainer=None),)
                            ),
    '岸边游客A':trainer.Trainer(name='岸边游客A',info='听说这里是水系宝贝的天堂'),
    '岸边游客B':trainer.Trainer(name='岸边游客B',info='我是不会下水的,太危险了'),
    '有梦想的训练家':trainer.Trainer(name='有梦想的训练家',info='激流道馆的霞是我的偶像！'),
    '迷路的热血少年':trainer.Trainer(name='迷路的热血少年',info='爷爷说穿过这里就是激流镇！'),
    '睿智的老人':trainer.Trainer(name='睿智的老人',info='这里的精灵掌控水的力量,却惧怕小草'),
}

shop_list_for_green_town_petball={
    '1': ('精灵球',100),
    '2': ('火焰球',200)
}
shop_npc_list_for_green_town = {
    '1': npc.ShopNpc(name='精灵球售卖员', info='我有球，你要吗？', sell_list=shop_list_for_green_town_petball, sell_type='petball'),
    '2': trainer.Trainer(name='导购小姐姐',info='欢迎光临,有什么可以帮忙你的吗？'),
    '3': trainer.Trainer(name='奇怪的人',info='不要伸张，这个送给你...',prize={'攻击之爪':1}),
    '4': trainer.Trainer(name='玩鸟少女',info='我的波波最强大...',
                         prize={'money':100},
                         can_challenge=True,
                         is_npc=False,
                         pet_list=(fly.Pidgey(level=5,skill_list={'1':skill.fireBall()},has_trainer=None),)),
}



hospital_npc_list_for_green_town = {
    '1': npc.Hosptial(name='小琪小姐',info='我是绿叶镇的治疗师,你可能见过我的很多姐妹。'),
    '2': trainer.Trainer(name='年老的长者',info='我的孙子也像你这么大...',prize={'火之石':1}),
    '3': trainer.Trainer(name='喷火龙爱好者',info='喷火龙Max！！！',
                     pet_change=fly.Pidgey(level=99,skill_list={'1': skill.fireBall()},has_trainer=True,autoAi=False),
                     change_condition='波波'),
    '4':npc.NonPeopleNpc(name='垃圾桶',info='你翻了翻垃圾桶!',prize={'A001':1}),
}

petgym_npc_list_for_green_town = {
    '1':[trainer.Trainer(name='绿叶学徒A',info='先过我这关！！！',
                        can_challenge=True,
                        prize={'money':150},
                        is_npc = False,
                        has_riddle = True,
                        pet_list=(rock.Geodude(level=8,skill_list={'1':skill.DownRock()},has_trainer=None),)
                        ),True],
    '2':[trainer.Trainer(name='绿叶学徒B',info='我和你练练',
                        can_challenge=True,
                        prize={'money':150},
                        is_npc = False,
                        has_riddle = True,
                        pet_list=(rock.Geodude(level=9,skill_list={'1':skill.DownRock(),'2':skill.RockFall()},has_trainer=None),)
                        ),False],
    '3':[trainer.Trainer(name='绿叶馆长',info='我最讨厌鸟儿',
                         can_challenge=True,
                         prize={'money':150,'绿叶徽章': 1},
                         is_npc=False,
                         pet_list=(rock.Geodude(level=9,skill_list={'1':skill.DownRock(),'2':skill.RockFall()},has_trainer=None),
                                   rock.Onix(level=10,skill_list={'1':skill.DownRock(),'2':skill.fireBall(),'3':skill.Earthquake()},has_trainer=None)
                                   )),False],
    '4':[trainer.Trainer(name='守馆老人',info="带一个草系宝贝来,不然你会悲剧的~"),True],
}