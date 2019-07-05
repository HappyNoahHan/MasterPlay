from place import village,map,topmap


class Player(object):
    def __init__(self,money=1000,name = '',pet_list={}):
        self.name = name
        self.money = money
        self.pet_list = pet_list

    trainer_id = 'Player01'#训练师编号


    map = map.whole_map

    current_place = topmap.top_map_dict['MAP00']

    map_run_list = [current_place]
    #是否能出战
    can_battle = True

    battle_pet_list = []
    battle_run_success = False

    badge_dict = {
        '绿叶徽章': False,
        '火焰徽章': False,
    }

    def setBadge(self,key):
        self.badge_dict[key] = True



    def setPet(self,key,value):
        self.pet_list[key] = value


