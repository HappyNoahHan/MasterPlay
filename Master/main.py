from pets import fly,fire,wood
import assist.show
from assist import exp,evolve
from props import propmap,drugmap,petballmap
from battle import asscount,skilllistmap,battle,learnskill
from players import play,battering
from place import  hospital


if __name__ == '__main__':
    player = play.Player()
    print(player.current_place)

    player.current_place.showMap(player)







