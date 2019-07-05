from place import placebase,meetnpc
from assist import system
from players import npcmap

class PetGym(placebase.Place):
    def showMap(self, player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('=' * 30)
        print('当前地图  %s ' % self.name)
        print('地图编号  %s ' % self.map_id)
        npc_list = npcmap.getNpcList(self.map_id)
        for key, item in npc_list.items():
            print(key, ':', item.name)
        print("请选择挑战")
        select_id = input(">")
        system.showSystem(player, select_id)
        if select_id in npc_list:
            if npc_list[select_id].is_special == True:
                pass
                return self.showMap(player)
            else:
                print(npc_list[select_id])
                meetnpc.meetNpc(player, npc_list[select_id], self)
        print("指令错误！")
        return self.showMap(player)