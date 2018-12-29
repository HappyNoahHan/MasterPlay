
from place import village,map


class Player(object):
    def __init__(self,money=1000,name = '',pet_list={}):
        self.name = name
        self.money = money
        self.pet_list = pet_list


    current_place = village.Village("新手村",maplist=map.village_map_for_start)

    map_run_list = [current_place]

    battle_pet_list = []
    battle_run_success = False



    def setPet(self,key,value):
        self.pet_list[key] = value


