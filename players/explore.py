from players import battering
from assist import show,exp,evolve,life,changepet,prize
from battle import asscount
from props import propmap
from pets import statusmap,pet_map
import random,time

def explore(player,wild_pet,place):
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

    if battering.battleing(player, wild_pet,place=place):
        if 'ST101' in wild_pet.status:
            print("%s 被吹飞"% wild_pet.name)
            return True

        if player.battle_run_success == False: #未逃跑
            if wild_pet.has_captured == False:
                if not player.pet_list['Master'].is_alive:
                    player.battle_pet_list.remove(player.pet_list['Master'])
                    if not changepet.changePetAfterDie(player):
                        print("没有可以使用的精灵")
                        # 无法出战
                        player.can_battle = False
                        return False
                exp.accountAfterBattleEnd(player,wild_pet)

        else:
            player.battle_run_success = False
        statusmap.checkStatusEnd(player)
        return True
    else:
        return False

def trainerVS(player,trainer,place):
    '''
    对战训练师
    :param player:
    :param trainer:
    :return:
    '''
    if player.can_battle == False:
        print("是什么给你的勇气还能挑衅？？？")
        return False

    try:
        challenge_list = list(trainer.getPetList())
    #trainer_master_pet = random.choice(challenge_list)
    except KeyError:
        print("没有实装角色pet_list!!!")
        trainer.can_challenge = False
        return True

    if battering.vsBattleing(player,trainer,challenge_list,place):
        if player.battle_run_success == False:
            pass
        else:
            player.battle_run_success = False
    else:
        return False
    for pet in trainer.getPetList():
        life.restore(pet)
        pet.reward_money = None #重置
    statusmap.checkStatusEnd(player)
    return True
