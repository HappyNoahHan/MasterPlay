from place import placebase,wildpetlist,treasure,village,town
from players import explore,trainer
from assist import show,riddle,prize,changepet
from props import bag
import random,time,os

class Grassform(placebase.Place):
    def __init__(self,name='',maplist={},wild_pet_list={},treasure_box_list={},trainer_list={}):
        super().__init__(name=name,maplist=maplist)
        self.wild_pet_list = wild_pet_list
        self.treasure_box_list = treasure_box_list
        self.trainer_list = trainer_list
        self.maplist = maplist



    def showMap(self,player):
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
                    find_trainer = trainer.getTrainer(self.trainer_list)
                    print("遇到了 %s ！" % find_trainer.name)
                    print(find_trainer)
                    time.sleep(2)
                    if find_trainer.is_npc == False:
                        if find_trainer.can_challenge == True:
                            if explore.trainerVS(player,find_trainer):
                                if find_trainer.has_riddle == True and find_trainer.can_challenge == False:
                                    riddle_condiction = riddle.openTheRiddle(find_trainer)
                                    self.setMapList(riddle_condiction[0],riddle_condiction[1])
                                #return self.showMap(player)
                            else:
                                print("无法继续战斗,请前往治疗")
                    else:
                        if find_trainer.prize:
                            prize.getPrize(player, find_trainer.prize)
                        if find_trainer.pet_change:
                            if changepet.changePetWithNpc(player,find_trainer.change_condition,find_trainer.pet_change):
                                find_trainer.pet_change = None
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
                    return self.maplist[select_id][0].showMap(player)
        else:
            if select_id == 'bag':
                bag.showBag(player)
                return self.showMap(player)
            elif select_id == 'back':
                return player.current_place.showMap(player)
        print("指令错误！")
        return self.showMap(player)



