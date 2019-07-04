from place import placebase,meetnpc
from assist import  system
from players import npcmap
import time

class Hospital(placebase.Place):

    def restore(self,player):
        for key,pet in player.pet_list.items():
            #清楚状态
            pet.health = pet._max_health
            pet.status.clear()
            pet.alive = True

            for key,skill in pet.skill_list.items():
                skill.pp_value = skill._pp_value_max
        player.can_battle = True

    def showMap(self,player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        print('地图编号  %s ' % self.map_id)

        npc_list = npcmap.getNpcList(self.map_id)

        for key,item in npc_list.items():
            print(key,':',item.name)
        print("请选择你要交流的对象")
        select_id = input(">")
        system.showSystem(player, select_id)
        if select_id in npc_list:
            if npc_list[select_id].is_special == True:
                if npc_list[select_id].recoverOrNot():
                    self.restore(player)
                    time.sleep(3)
                    print("所有精灵状态恢复")
                    return self.showMap(player)
                else:
                    print("你拒绝恢复你的精灵")
                    return self.showMap(player)
            else:
                print(npc_list[select_id])
                meetnpc.meetNpc(player,npc_list[select_id],self)

        else:
            print("指令错误！")
            return self.showMap(player)





