def blockOpenOrNot(player,place):
    if place.block != None:
        if place.block in player.badge_dict:
            if player.badge_dict[place.block] == False:
                return False
        else:
            return False

    return True