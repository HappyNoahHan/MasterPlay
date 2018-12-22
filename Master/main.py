from pets import fly,fire,wood
import assist.show
from assist import exp,evolve
from props import propmap,drugmap,petballmap
from battle import asscount,skilllistmap,battle,learnskill
from players import play,battering


if __name__ == '__main__':
    player = play.Player()
    print("玩家 %s" % player.name)
    print("=" * 30)

    #bird = fly.aiPidgey(4)
    wild_pet= wood.aiOodish(level=5)
    print("小心，你遇到了 %s ！" % wild_pet.name)
    #gress.health = 100
    assist.show.showPetStatus(wild_pet)
    learnskill.learnSkill(wild_pet,'A004',realize=False)


    if battering.battleing(player,wild_pet):
        print(player.pet_list)
        assist.show.showPetStatus(player.pet_list['4'])






