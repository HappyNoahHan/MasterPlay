from place import placebase,meetnpc
from assist import system

class PetGym(placebase.Place):
    def showMap(self, player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('=' * 30)
        print('当前地图  %s ' % self.name)
        for key, item in self.npc_list.items():
            if item[1] == True:
                print(key, ':', item[0].name)
        print("请选择挑战")
        select_id = input(">")
        system.showSystem(player, select_id)
        if select_id in self.npc_list:
            if self.npc_list[select_id][1] != False:
                if self.npc_list[select_id][0].is_special == True:
                    pass
                    return self.showMap(player)
                else:
                    print(self.npc_list[select_id][0])
                    meetnpc.meetNpc(player, self.npc_list[select_id][0], self)
        print("指令错误！")
        return self.showMap(player)