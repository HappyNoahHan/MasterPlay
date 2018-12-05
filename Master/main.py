import pets.bibibird,pets.firefox
import battle.battle
import battle.skill
import battle.learn_skill
import random
if __name__ == '__main__':
    print("=" * 30)
    print("小心，你已经进入了战斗！  ")

    bird = pets.bibibird.WildBBBird('野生哔哔鸟',random.randint(50,60),
                               random.randint(8,11),
                               random.randint(4,6),10)
    bird.showStatus()
    print("=" * 30)
    print("你的火狐狸准备战斗")
    fox = pets.firefox.FireFox('火狐狸',50,20,100,20)

    if battle.learn_skill.learnSkill(fox,'N002'):
        print("技能学习成功！")
    #fox.skill_first = battle.skill.steadiness()

    if fox.speed > bird.speed:
        print("%s 优先进攻" % fox.name)
        battle.battle.battleRun(fox,bird)
    else:
        battle.battle.battleRun(bird,fox)
