from assist import system
from place import block

class Place(object):

    def __init__(self,name='',maplist={},treasure_box_list={},npc_list={},prize_box_list={},block=None,can_fishing=False
                    ,weather = None, place_status = None,map_id=None):
        self.name = name
        self.maplist = maplist
        self.treasure_box_list = treasure_box_list
        self.npc_list = npc_list
        self.prize_box_list = prize_box_list
        self.block = block
        self.can_fishing = can_fishing
        self.weather = weather
        self.place_status = place_status
        self.map_id = map_id  #地图编号

    def __str__(self):
        return self.name

    def showMap(self,player):
        can_go_list = []
        if player.map_run_list:
            if player.map_run_list[-1] != self:
                player.map_run_list.append(self)
        else:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        print('地图编号  %s ' % self.map_id ) #测试

        for key,vaule in player.map.items():
            if self.map_id in vaule[1]:
                can_go_list.append(key)
                print(key,':',vaule[0].name)

        print("请输入指令")
        #选择地图
        select_id = input(">")

        if select_id in can_go_list:
            if block.blockOpenOrNot(player,player.map[select_id][0]):
                player.map[select_id][0].showMap(player)
            else:
                print("当前区域未开放！")
                return self.showMap(player)
        else:
            system.showSystem(player, select_id)
        print("指令错误！")
        return self.showMap(player)

    def setMapList(self,key,value):
        self.maplist[key][1] = value

    def setNpcList(self,key,value):
        self.npc_list[key][1] = value