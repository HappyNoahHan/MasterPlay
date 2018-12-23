from place import placebase,wildpetlist
from pets import wood,fly
from players import explore
from battle import skill
import random,time

class Grassform(placebase.Place):
    def __init__(self,name='',wild_pet_list={}):
        super().__init__(name=name)
        self.wild_pet_list = wild_pet_list

    map = {
        '1':'野外探险',
        '2':'搜索玩家',
        '3':'寻宝',
        '0':'返回',
    }



    def showMap(self,player):
        for key,value in self.map.items():
            print(key,':',value)

        print("请选择行动指令")

        select_id = input(">")

        if select_id == '1':
            print("正在草丛探险...")
            time.sleep(3)
            wild_pet = wildpetlist.meetWildPet(self.wild_pet_list)
            print("你遇到了 %s !" % wild_pet.name)
            if explore.explore(player,wild_pet):
                return self.showMap(player)
        elif select_id == '2':
            pass
        elif select_id == '3':
            pass
        elif select_id == '0':
            player.current_place.showMap(player)
        else:
            print("指令错误！")
            return self.showMap(player)


