from players import battering
from assist import show,exp,evolve
from battle import asscount
def explore(player,wild_pet):
    '''
    野外探险
    :param player:
    :return:
    '''
    #战斗前 清楚
    player.battle_pet_list.clear()

    if battering.battleing(player, wild_pet):
        if player.battle_run_success == False:
            for master_pet in player.battle_pet_list:
                # 清除buff
                master_pet.buff_dict.clear()
                # obj1.debuff_dict.clear()
                master_pet.property_buff.clear()

                # 计算获得的基础点数
                # print(master_pet.attack_base_point)
                # print("基础点数获得者",wild_pet.basic_point_getter)
                if wild_pet.basic_point_getter == master_pet:
                    asscount.getBasePoint(master_pet, wild_pet)
                # print(master_pet.attack_base_point)

                # 战斗结束之后结算
                # 经验值计算
                got_exp = exp.getBattleSuccessExp(player,wild_pet)
                print("%s 获得 %s 经验值" % (master_pet.name, got_exp))
                master_pet.exp_for_current += got_exp

                if exp.isLevelUp(master_pet):
                    show.showPetStatus(master_pet)
                # 进化判断
                if master_pet.canEvolve:
                    if master_pet.level >= master_pet.evolve_level:
                        print("精灵是否进化！ 1 yes  2 no ")
                        isEvo = input(">")
                        if int(isEvo) == 1:
                            player.setPet('Master', evolve.isEvolve(master_pet))

                        else:
                            print("精灵停止进化！")
        else:
            player.battle_run_success = False
        return True
    else:
        return False