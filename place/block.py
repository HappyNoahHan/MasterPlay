#from place import topmap

def blockOpenOrNot(player,place):
    #place = topmap.top_map_dict[place_id]
    if place.block != None:
        if place.block in player.badge_dict:
            if player.badge_dict[place.block] == False:
                return False
        else:
            return False

    return True