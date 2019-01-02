from place import placebase,village,meetnpc
from props import bag
from assist import  system,prize,changepet
import time

class Hospital(placebase.Place):

    def restore(self,player):
        for key,pet in player.pet_list.items():
            #清楚状态
            pet.health = pet._max_health
            pet.debuff_dict.clear()
            pet.buff_dict.clear()
            pet.property_buff.clear()
            pet.status.clear()
            pet.alive = True

            for key,skill in pet.skill_list.items():
                skill.pp_value = skill._pp_value_max

    def showMap(self,player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        for key,item in self.npc_list.items():
            print(key,':',item.name)
        print("请选择你要交流的对象")
        select_id = input(">")
        system.showSystem(player, select_id)
        if select_id in self.npc_list:
            if self.npc_list[select_id].is_special == True:
                if self.npc_list[select_id].recoverOrNot():
                    self.restore(player)
                    time.sleep(3)
                    print("所有精灵状态恢复")
                    return self.showMap(player)
                else:
                    print("你拒绝恢复你的精灵")
                    return self.showMap(player)
            else:
                print(self.npc_list[select_id])
                meetnpc.meetNpc(player,self.npc_list[select_id],self)

        else:
            print("指令错误！")
            return self.showMap(player)



def restore(pet):
    pet.health = pet._max_health
    pet.debuff_dict.clear()
    pet.buff_dict.clear()
    pet.property_buff.clear()
    pet.status.clear()
    pet.alive = True
    pet.basic_point_getter = None

    for key,skill in pet.skill_list.items():
        skill.pp_value = skill._pp_value_max

