
import assist.show
from assist import exp,evolve,capture,changepet,show,prize
from props import handbook,propmap
from battle import asscount,skilllistmap,battle,learnskill
import random,time

def battleing(player,wild_pet,change_pet = False,place=None):
    #将未发现的精灵加入图鉴
    if wild_pet.petNo not in handbook.pet_handbook_dict:
        handbook.setHandBook(wild_pet.petNo,wild_pet.getName(),wild_pet.getAttr())
    #谁获得基础点数
    wild_pet.basic_point_getter = player.pet_list['Master']
    print("=" * 30)
    master_pet = player.pet_list['Master']
    print("%s 准备战斗！" % master_pet.getName())
    #assist.show.showPetStatus(master_pet)
    #加入战斗精灵列表
    if master_pet not in player.battle_pet_list:
        player.battle_pet_list.append(master_pet)
    # 检查携带物
    # propmap.checkCarryPropForObj(master_pet)
    # propmap.checkCarryPropForObj(wild_pet)
    #assist.show.showPetStatus(master_pet)

    #判断是否交换过精灵
    if change_pet == False:
        if master_pet.getSpeed() > wild_pet.getSpeed():
            print("%s 优先进攻" % master_pet.getName())
            battle_end = battle.battleRun(player,master_pet, wild_pet,place)
        else:
            battle_end = battle.battleRun(player,wild_pet, master_pet,place)
    else:
        battle_end = battle.battleRun(player,wild_pet, master_pet,place)


    if battle_end == True:

        if wild_pet.has_captured == False or wild_pet.has_captured == None:
            if not master_pet.is_alive: #主战精灵濒危
                if wild_pet.is_alive: #对方未濒危
                    try:
                        #移除 死亡精灵无经验值
                        player.battle_pet_list.remove(master_pet)
                    except ValueError:
                        print("已经移除？？？")
                    if changepet.changePetAfterDie(player):
                        return battleing(player,wild_pet,change_pet=True,place=place)
                    else:
                        print("没有可以使用的精灵")
                        #无法出战
                        player.can_battle = False
                        return False
        #捕获成功代码
        else:
            capture.addPetOrNot(player,wild_pet)
                #print("99999999")
    #player.exp_status.clear()
    return True


def vsBattleing(player,trainer,challenge_list,place):
    '''
    训练师傅对战
    :param player:
    :param trainer:
    :param change_pet:
    :return:
    '''
    print("=" * 30)
    player.battle_pet_list.clear()
    if player.battle_run_success == False:
        trainer_master_pet = random.choice(challenge_list)
        print("%s 准备使用 %s Lv%s 进行战斗！" % (trainer.name,trainer_master_pet.getName(),trainer_master_pet.level))
        #show.showPetStatus(trainer_master_pet)

        if battleing(player,trainer_master_pet,place=place):
            if player.battle_run_success != True:
                challenge_list.remove(trainer_master_pet)
                if len(challenge_list) == 0:
                    print("挑战胜利！")
                    trainer.can_challenge = False
                    prize.getPrize(player,trainer.prize)
                    time.sleep(3)
                    exp.accountAfterBattleEnd(player, trainer_master_pet)
                    return True
                else:
                    if not player.pet_list['Master'].is_alive:
                        player.battle_pet_list.remove(player.pet_list['Master'])
                        if not changepet.changePetAfterDie(player):
                            print("没有可以使用的精灵")
                            # 无法出战
                            player.can_battle = False
                            return False
                    exp.accountAfterBattleEnd(player, trainer_master_pet)
                    #结算经验
                    return vsBattleing(player,trainer,challenge_list,place)
            return True
        else:
            return False
    else:
        return True
