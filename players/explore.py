from players import battering
from assist import show
def explore(player,wild_pet):
    '''
    野外探险
    :param player:
    :return:
    '''
    if battering.battleing(player, wild_pet):
        print(player.pet_list)
        show.showPetStatus(player.pet_list['Master'])
        return True
    else:
        return False