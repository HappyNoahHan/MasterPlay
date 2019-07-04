from players import explore,npcmap
from assist import prize,changepet,riddle
import time

def meetNpc(player,npcer,place):
    time.sleep(2)
    if npcer.is_npc == False:
        if npcer.can_challenge == True:
            if explore.trainerVS(player, npcer,place):
                if npcer.has_riddle == True and npcer.can_challenge == False:
                    riddle_condiction = riddle.openTheRiddle(npcer)
                    if riddle_condiction[2] == 'trainer':
                        npcmap.setNpcList(riddle_condiction[0], riddle_condiction[1],place.map_id)
                    else:
                        pass
                # return self.showMap(player)
            else:
                print("无法继续战斗,请前往治疗")
    else:
        try:
            if npcer.prize:
                prize.getPrize(player, npcer.prize)
            elif npcer.pet_change:
                if changepet.changePetWithNpc(player, npcer.change_condition, npcer.pet_change):
                    npcer.pet_change = None
        except AttributeError: #非物品道具并没有交换选项
            print("什么也没有发生")
    return place.showMap(player)