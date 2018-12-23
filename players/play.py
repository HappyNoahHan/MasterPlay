from pets import fire,fly
from place import village
from battle import skill

class Player(object):
    def __init__(self):
        self.name = '小智'


    master_pet = fire.Charmander(level=5,skill_list={'1':skill.fireBall()})
    a=fire.Charmeleon(level=15,skill_list={'1':skill.fireBall()})
    b=fire.Charmeleon(level=20,skill_list={'1':skill.fireBall()})

    pet_list = {
        '1': master_pet,
        '2': a,
        '3': b,
    }


    current_place = village.Village("新手村")



    def setPet(self,key,value):
        self.pet_list[key] = value


