from players import battering
from assist import show,exp,evolve,life
from battle import asscount
def explore(player,wild_pet):
    '''
    野外探险
    :param player:
    :return:
    '''
    #战斗前 清除
    if player.can_battle == False:
        print("自己是个什么鸟样没有B数吗？？？")
        return False

    player.battle_pet_list.clear()

    if battering.battleing(player, wild_pet):
        if player.battle_run_success == False:
            if wild_pet.captured == False:
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
                    if evolve.canEvolveOrNot(master_pet):
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

def trainerVS(player,trainer):
    '''
    对战训练师
    :param player:
    :param trainer:
    :return:
    '''
    if player.can_battle == False:
        print("是什么给你的勇气还能挑衅？？？")
        return False
    challenge_list = list(trainer.pet_list)

    if battering.vsBattleing(player,trainer,challenge_list):
        if player.battle_run_success == False:
            for get_exp_pet in player.battle_pet_list:
                # 清除buff
                get_exp_pet.buff_dict.clear()
                get_exp_pet.property_buff.clear()

                got_exp = 0
                for pet in trainer.pet_list:
                    # 计算获得的基础点数
                    if pet.basic_point_getter == get_exp_pet:
                        print("基础点数获得者", pet.basic_point_getter)
                        asscount.getBasePoint(get_exp_pet, pet)
                    # 战斗结束之后结算
                    # 经验值计算
                    got_exp += exp.getBattleSuccessExp(player, pet)
                print("%s 获得 %s 经验值" % (get_exp_pet.name, got_exp))
                get_exp_pet.exp_for_current += got_exp

                if exp.isLevelUp(get_exp_pet):
                    show.showPetStatus(get_exp_pet)
                # 进化判断
                if evolve.canEvolveOrNot(get_exp_pet):

                    print("精灵是否进化！ 1 yes  2 no ")
                    isEvo = input(">")
                    if int(isEvo) == 1:
                        player.setPet('Master', evolve.isEvolve(get_exp_pet))

                    else:
                        print("精灵停止进化！")

        else:
            player.battle_run_success = False
    else:
        return False
    for pet in trainer.pet_list:
        life.restore(pet)
    return True
