from place import placebase
from pets import wood,fly
from players import explore
from battle import skill
import random

class Grassform(placebase.Place):
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
            wild_pet = wood.aiOodish(level=random.randint(3,5),skill_list={'1':skill.scream()})
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

    wild_pet_list={
        wood.aiOodish(level=random.randint(3,5),skill_list={'1':skill.scream()}): 0.5,
        fly.aiPidgey(level=random.randint(3,5),skill_list={'1':skill.scream()}): 0.5,
    }
