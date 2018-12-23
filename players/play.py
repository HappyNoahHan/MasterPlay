from pets import fire,fly
from place import village
from battle import skill
from assist import rancom

class Player(object):
    def __init__(self):
        self.name = '小智'


    a = fire.Charmander(level=1,skill_list={'1':skill.fireBall()})
    b = fire.Charmeleon(level=10,skill_list={'1':skill.fireBall()})
    c = fire.Charmeleon(level=10,skill_list={'1':skill.fireBall()})


    pet_list = {
        'Master': a,
        '1': c,
        '2': b,
    }


    current_place = village.Village("新手村")



    def setPet(self,key,value):
        self.pet_list[key] = value


