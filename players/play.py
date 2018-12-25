from pets import fire,fly
from place import village
from battle import skill
from assist import rancom

class Player(object):
    def __init__(self,money=0,name = '',pet_list={}):
        self.name = name
        self.money = money
        self.pet_list = pet_list


    current_place = village.Village("新手村")

    battle_pet_list = []
    battle_run_success = False



    def setPet(self,key,value):
        self.pet_list[key] = value


