import pets.bibibird,pets.firefox
import battle.battle
import battle.skill
import battle.learn_skill
import random
import assist.show
if __name__ == '__main__':
    print("=" * 30)
    print("小心，你已经进入了战斗！  ")

    bird = pets.bibibird.WildBBird('野生哔哔鸟',random.randint(99,100),
                               random.randint(18,21),
                               random.randint(4,6),10)

    bird.showStatus()
    battle.learn_skill.learnSkill(bird,'A004')
    print("=" * 30)
    print("你的火狐狸准备战斗")
    fox = pets.firefox.FireFox('火狐狸',100,20,10,20)

    if battle.learn_skill.learnSkill(fox,'N002'):
        assist.show.learnSkill('N002')
    if battle.learn_skill.learnSkill(fox,'T002'):
        assist.show.learnSkill('A004')
    battle.learn_skill.learnSkill(fox,'S001')
    #fox.skill_first = battle.skill.steadiness()

    if fox.speed > bird.speed:
        print("%s 优先进攻" % fox.name)
        battle.battle.battleRun(fox,bird)
    else:
        battle.battle.battleRun(bird,fox)
