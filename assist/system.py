from props import bag,handbook
from assist import prize,petbox,fish,show
from players import explore
import time

def showSystem(player,select_id):
    if select_id == 'bag':
        bag.showBag(player)
        return player.map_run_list[-1].showMap(player)
    elif select_id == 'back':
        if len(player.map_run_list) == 1:
            return player.map_run_list[-1].showMap(player)
        else:
            player.map_run_list.pop(-1)
            return player.map_run_list[-1].showMap(player)
    elif select_id == 'pet':
        handbook.showPets(player)
        return player.map_run_list[-1].showMap(player)
    elif select_id == 'book':
        handbook.showHandBook()
        return player.map_run_list[-1].showMap(player)
    elif select_id == 'search':
        get_prize = prize.getPrizeFromBox(player.map_run_list[-1].prize_box_list)
        if get_prize == None:
            print("没有任何发现！")
        else:
            prize.putPrizeToBag(get_prize)
        return player.map_run_list[-1].showMap(player)
    elif select_id == 'badge':
        for key,value in player.badge_dict.items():
            print(key,':',value)
        return player.map_run_list[-1].showMap(player)
    elif select_id == 'box':
        #for test
        petbox.petBoxAction(player)
        return player.map_run_list[-1].showMap(player)
    elif select_id == 'fishing':
        if player.map_run_list[-1].can_fishing == True:
            print("你正在钓鱼...")
            time.sleep(3)
            fished_pet = fish.fishing(player.map_run_list[-1].name)
            show.showPetStatus(fished_pet)
            print("你遇到了 %s ! lv: %s" % (fished_pet.name, fished_pet.level))
            if explore.explore(player, fished_pet):
                return player.map_run_list[-1].showMap(player)
            else:
                print("无法继续战斗,请前往治疗")
                return player.map_run_list[-1].showMap(player)
        else:
            print("什么也没有发生")
            return player.map_run_list[-1].showMap(player)



