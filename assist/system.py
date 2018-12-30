from props import bag,handbook

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
