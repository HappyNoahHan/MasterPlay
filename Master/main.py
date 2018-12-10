from pets import fly,fire,wood
import battle.battle
import battle.skill
import battle.learnskill
import random
import assist.show
if __name__ == '__main__':
    print("=" * 30)
    print("小心，你已经进入了战斗！  ")

    #bird = fly.aiPidgey(4)
    gress = wood.aiOodish(level=5)

    print(gress)
    assist.show.showPetStatus(gress)
    battle.learnskill.learnSkill(gress,'B002')
    print("=" * 30)
    print("你的火狐狸准备战斗")
    fox = fire.Charmander(level=5)
    print(fox.health_indi)
    assist.show.showPetStatus(fox)

    if battle.learnskill.learnSkill(fox,'N002'):
        assist.show.learnSkill('N001')
    if battle.learnskill.learnSkill(fox,'A004'):
        assist.show.learnSkill('A004')
    battle.learnskill.learnSkill(fox,'T002')
    #测试用例
    #fox.skill_first = battle.skill.steadiness()
    #fox.speed = 255



    if fox.speed > gress.speed:
        print("%s 优先进攻" % fox.name)
        battle.battle.battleRun(fox,gress)
    else:
        battle.battle.battleRun(gress,fox)




