from place import placebase,wildpetlist,treasure,meetnpc,block
from players import explore,trainer
from assist import show,riddle,prize,changepet,system
from props import bag
import random,time,os

class Grassform(placebase.Place):
    def __init__(self,name='',maplist={},wild_pet_list={},treasure_box_list={},npc_list={},block=None):
        super().__init__(name=name,maplist=maplist,treasure_box_list=treasure_box_list,npc_list=npc_list,block=block)
        self.wild_pet_list = wild_pet_list



    def showMap(self,player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        for key,value in self.maplist.items():
            if value[1] != False:
                print(key,':',value[0])

        print("请选择行动指令")


        select_id = input(">")
        if select_id in self.maplist:
            if self.maplist[select_id][1] != False:
                if select_id == '1':
                    print("正在草丛探险...")
                    time.sleep(3)
                    wild_pet = wildpetlist.getWildPet(self.wild_pet_list)
                    show.showPetStatus(wild_pet)
                    print("你遇到了 %s ! lv: %s" % (wild_pet.name,wild_pet.level))
                    if explore.explore(player,wild_pet):
                        return self.showMap(player)
                    else:
                        print("无法继续战斗,请前往治疗")
                        return self.showMap(player)

                elif select_id == '2':
                    #训练师对战
                    time.sleep(1)
                    find_trainer = trainer.getTrainer(self.npc_list)
                    if find_trainer != None:
                        print("遇到了 %s ！" % find_trainer.name)
                        print(find_trainer)
                        meetnpc.meetNpc(player,find_trainer,self)
                    else:
                        print("除了石头与空气,没有任何活物！")
                    return self.showMap(player)

                elif select_id == '3':
                    print("正在草丛寻宝...")
                    time.sleep(1)
                    find_item = treasure.getTreasureBox(self.treasure_box_list)
                    if find_item == None:
                        print("什么也没有发现")
                    else:
                        treasure.getPropsToBag(find_item[0],find_item[1])
                    return self.showMap(player)
                else:
                    #player.old_place = self
                    if block.blockOpenOrNot(player, self.maplist[select_id][0]):
                        self.maplist[select_id][0].showMap(player)
                    else:
                        print("当前区域未开放！")
                        return self.showMap(player)
        else:
            system.showSystem(player,select_id)
        print("指令错误！")
        return self.showMap(player)



