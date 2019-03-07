
import assist.show
from assist import exp,evolve,capture,changepet,show,prize
from props import handbook
from battle import asscount,skilllistmap,battle,learnskill
import random,time

def battleing(player,wild_pet,change_pet = False,place=None):
    #将未发现的精灵加入图鉴
    if wild_pet.pet_no not in handbook.pet_handbook_dict:
        handbook.setHandBook(wild_pet.pet_no,wild_pet.name,wild_pet.prop)
    #谁获得基础点数
    wild_pet.basic_point_getter = player.pet_list['Master']
    print("=" * 30)
    master_pet = player.pet_list['Master']
    print("%s 准备战斗！" % master_pet.name)
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
            print("%s 优先进攻" % master_pet.name)
            battle_end = battle.battleRun(player,master_pet, wild_pet,place)
        else:
            battle_end = battle.battleRun(player,wild_pet, master_pet,place)
    else:
        battle_end = battle.battleRun(player,wild_pet, master_pet,place)


    if battle_end == True:

        if wild_pet.captured == False or wild_pet.captured == None:
            if master_pet.health <= 0:
                master_pet.alive = False
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


def vsBattleing(player,trainer,challenge_list):
    '''
    训练师傅对战
    :param player:
    :param trainer:
    :param change_pet:
    :return:
    '''
    print("=" * 30)
    if player.battle_run_success == False:
        trainer_master_pet = random.choice(challenge_list)
        print("%s 准备使用 %s Lv%s 进行战斗！" % (trainer.name,trainer_master_pet.name,trainer_master_pet.level))
        #show.showPetStatus(trainer_master_pet)

        if battleing(player,trainer_master_pet):
            if player.battle_run_success != True:
                challenge_list.remove(trainer_master_pet)
                if len(challenge_list) == 0:
                    print("挑战胜利！")
                    trainer.can_challenge = False
                    prize.getPrize(player,trainer.prize)
                    time.sleep(3)
                    return True
                else:
                    return vsBattleing(player,trainer,challenge_list)
            return True
        else:
            return False
    else:
        return True

