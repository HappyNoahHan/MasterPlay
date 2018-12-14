from pets import fly,fire,wood
import battle.battle
import battle.skill
import battle.learnskill
import random
import assist.show
from assist import exp,evolve
from props import propmap
from battle import asscount


if __name__ == '__main__':
    print("=" * 30)
    print("小心，你已经进入了战斗！  ")

    #bird = fly.aiPidgey(4)
    gress = wood.aiOodish(level=5)
    #gress.health = 100
    print(gress)
    assist.show.showPetStatus(gress)
    battle.learnskill.learnSkill(gress,'B002')
    print("=" * 30)
    print("你的火狐狸准备战斗")
    fox = fire.Charmander(level=5)

    assist.show.showPetStatus(fox)

    if battle.learnskill.learnSkill(fox,'S002'):
        assist.show.learnSkill('N001')
    # if battle.learnskill.learnSkill(fox,'A009'):
    #    assist.show.learnSkill('A004')
    #battle.learnskill.learnSkill(fox,'N001')

    #测试用例
    #fox.skill_first = battle.skill.steadiness()
    #fox.speed = 255
    #fox.realize_skill_list.append('S001')
    #print(fox.health_indi)
    #fox.status.append('ST001')
    #fox.status.append('ST002')
    #print(fox.status)
    #propmap.prop_dict['火焰之心'].equipProp(fox)
    #propmap.prop_dict['火焰之心'].removeProp(fox)
    #propmap.prop_dict['五彩迷光'].equipProp(gress)
    #propmap.prop_dict['攻击之爪'].equipProp(fox)

    propmap.checkCarryPropForObj(fox)
    propmap.checkCarryPropForObj(gress)
    assist.show.showPetStatus(fox)


    if fox.getSpeed() > gress.getSpeed():
        print("%s 优先进攻" % fox.name)
        battle_end = battle.battle.battleRun(fox,gress)
    else:
        battle_end = battle.battle.battleRun(gress,fox)

    if battle_end == True:
        if fox.health <= 0:
            assist.show.gameOver()
        else:
            #计算获得的基础点数
            #print(fox.attack_base_point)
            asscount.getBasePoint(fox,gress)
            #print(fox.attack_base_point)

            # 战斗结束之后结算
            # 经验值计算
            got_exp = exp.getBattleSuccessExp(gress)
            print("%s 获得 %s 经验值" % (fox.name, got_exp))
            fox.exp_for_current += got_exp

            if exp.isLevelUp(fox):
                assist.show.showPetStatus(fox)
            # 进化判断
            if fox.canEvolve:
                if fox.level >= fox.evolve_level:
                    print("精灵是否进化！ 1 yes  2 no ")
                    isEvo = input(">")
                    if int(isEvo) == 1:
                        fox = evolve.isEvolve(fox)
                    else:
                        print("精灵停止进化！")
            # 清除buff
            fox.buff_dict.clear()
            # obj1.debuff_dict.clear()
            fox.property_buff.clear()
            assist.show.battleOver()




