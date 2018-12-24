from place import placebase,wildpetlist,treasure
from players import explore
from assist import show
from props import bag
import random,time,os

class Grassform(placebase.Place):
    def __init__(self,name='',wild_pet_list={}):
        super().__init__(name=name)
        self.wild_pet_list = wild_pet_list

    maplist = {
        '1':'野外探险',
        '2':'搜索玩家',
        '3':'寻宝',
        '0':'返回',
    }



    def showMap(self,player):
        print('='*30)
        print('当前地图  %s ' % self.name)
        for key,value in self.maplist.items():
            print(key,':',value)

        print("请选择行动指令")

        select_id = input(">")

        if select_id == '1':
            print("正在草丛探险...")
            time.sleep(3)
            wild_pet = wildpetlist.getWildPet(self.wild_pet_list)
            show.showPetStatus(wild_pet)
            print("你遇到了 %s ! lv: %s" % (wild_pet.name,wild_pet.level))
            if explore.explore(player,wild_pet):
                return self.showMap(player)
            else:
                show.gameOver()
                os._exit(1)

        elif select_id == '2':
            pass
        elif select_id == '3':
            print("正在草丛寻宝...")
            time.sleep(1)
            find_item = treasure.getTreasureBox(treasure.treasure_box_for_grass_no_1)
            if find_item == None:
                print("什么也没有发现")
            else:
                treasure.getPropsToBag(find_item[0],find_item[1])
            return self.showMap(player)


        elif select_id == '0':
            player.current_place.showMap(player)
        elif select_id == '9' or select_id == 'bag':
            bag.showBag(player)
            return self.showMap(player)
        else:
            print("指令错误！")
            return self.showMap(player)


