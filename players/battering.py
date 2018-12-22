from pets import fly,fire,wood
import assist.show
from assist import exp,evolve,capture
from props import propmap,drugmap,petballmap
from battle import asscount,skilllistmap,battle,learnskill
from players import play


def battleing(player,wild_pet,change_pet = False):
    #谁获得基础点数
    wild_pet.basic_point_getter = player.master_pet
    print("=" * 30)
    master_pet = player.master_pet
    print("%s 准备战斗！" % master_pet.name)
    assist.show.showPetStatus(master_pet)


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
                assist.show.gameOver()
            else:
                # 计算获得的基础点数
                # print(master_pet.attack_base_point)
                print("基础点数获得者",wild_pet.basic_point_getter)
                if wild_pet.basic_point_getter == master_pet:
                    asscount.getBasePoint(master_pet, wild_pet)
                # print(master_pet.attack_base_point)

                # 战斗结束之后结算
                # 经验值计算
                got_exp = exp.getBattleSuccessExp(wild_pet)
                print("%s 获得 %s 经验值" % (master_pet.name, got_exp))
                master_pet.exp_for_current += got_exp

                if exp.isLevelUp(master_pet):
                    assist.show.showPetStatus(master_pet)
                # 进化判断
                if master_pet.canEvolve:
                    if master_pet.level >= master_pet.evolve_level:
                        print("精灵是否进化！ 1 yes  2 no ")
                        isEvo = input(">")
                        if int(isEvo) == 1:
                            player.master_pet = evolve.isEvolve(master_pet)
                        else:
                            print("精灵停止进化！")

        #捕获成功代码
        else:
            if capture.addPetOrNot(player,wild_pet):
                print("99999999")

        # 清除buff
        master_pet.buff_dict.clear()
        # obj1.debuff_dict.clear()
        master_pet.property_buff.clear()
        assist.show.battleOver()

    player.exp_status = 1

    return True