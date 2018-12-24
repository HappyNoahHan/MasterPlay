from pets import fly,fire,wood
import assist.show
from assist import exp,evolve,capture,changepet
from props import propmap,drugmap,petballmap
from battle import asscount,skilllistmap,battle,learnskill
from players import play
import os

def battleing(player,wild_pet,change_pet = False):
    #谁获得基础点数
    wild_pet.basic_point_getter = player.pet_list['Master']
    print("=" * 30)
    master_pet = player.pet_list['Master']
    print("%s 准备战斗！" % master_pet.name)
    assist.show.showPetStatus(master_pet)
    #加入战斗精灵列表
    if master_pet not in player.battle_pet_list:
        player.battle_pet_list.append(master_pet)
    # 检查携带物
    propmap.checkCarryPropForObj(master_pet)
    propmap.checkCarryPropForObj(wild_pet)
    #assist.show.showPetStatus(master_pet)

    #判断是否交换过精灵
    if change_pet == False:
        if master_pet.getSpeed() > wild_pet.getSpeed():
            print("%s 优先进攻" % master_pet.name)
            battle_end = battle.battleRun(player,master_pet, wild_pet)
        else:
            battle_end = battle.battleRun(player,wild_pet, master_pet)
    else:
        battle_end = battle.battleRun(player,wild_pet, master_pet)


    if battle_end == True:

        if wild_pet.captured == False:
            if master_pet.health <= 0:
                master_pet.alive = False
                player.battle_pet_list.remove(master_pet)
                if changepet.changePetAfterDie(player):
                    return battleing(player,wild_pet,change_pet=True)
                else:
                    print("没有可以使用的精灵")
                    return False
        #捕获成功代码
        else:
            if capture.addPetOrNot(player,wild_pet):
                print("99999999")

    #player.exp_status.clear()

    return True