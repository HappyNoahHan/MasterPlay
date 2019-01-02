from props import bag,handbook
from assist import prize

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

