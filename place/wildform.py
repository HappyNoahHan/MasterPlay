from place import placebase,wildpetlist,treasure,meetnpc,block
from players import explore,npcmap
from assist import show,riddle,prize,changepet,system
from props import bag
import random,time,os

class WildForm(placebase.Place):
    def __init__(self,name='',treasure_box_list={},block=None,weather=None,place_status=None,map_id=None):
        '''

        :param name:
        :param maplist:
        :param wild_pet_list: 取消 使用map_id
        :param treasure_box_list:
        :param npc_list:
        :param block:
        :param weather: 天气
        :param place_status:  场地状态
        '''
        super().__init__(name=name,treasure_box_list=treasure_box_list,block=block,map_id=map_id)
        self.weather = weather
        self.place_status = place_status

    def setPlaceStatus(self,key,value):
        self.place_status = [key,value]

    def setPlaceWeather(self,value):
        self.weather = value

    def showMap(self,player):
        can_go_list = []
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        print('地图编号  %s ' % self.map_id ) #测试

        for key,vaule in player.map.items():
            if self.map_id in vaule[1]:
                can_go_list.append(key)
                print(key,':',vaule[0].name)

        print("=" * 30)
        print("指令")
        print('fight || fi : 遭遇')
        print('battle || ba : 对战')
        print('search || sh: 寻宝')
        print('=' *30)

        print("请选择行动指令")

        select_id = input(">")

        if select_id == 'fi' or select_id == 'fight':
            print("精灵在哪里呀...在哪里呀...")
            time.sleep(3)
            #try:
            wild_pet = wildpetlist.getWildPet(self.map_id)
            #show.showPetStatus(wild_pet)
            print("你遇到了 %s ! lv: %s" % (wild_pet.name,wild_pet.level))
            if explore.explore(player,wild_pet,self):
                return self.showMap(player)
            else:
                print("无法继续战斗,请前往治疗")
                return self.showMap(player)
            #except AttributeError:
                #print("我在哪？我是谁？发生了什么？")
                #return self.showMap(player)

        elif select_id == 'ba' or select_id == 'battle':
            #训练师对战
            time.sleep(1)
            find_trainer = npcmap.getTrainer(self.map_id)
            if find_trainer != None:
                print("遇到了 %s ！" % find_trainer.name)
                print(find_trainer)
                meetnpc.meetNpc(player,find_trainer,self)
            else:
                print("除了空气和你,没有任何会唱歌的！")
            return self.showMap(player)

        elif select_id == 'sh' or select_id == 'search':
            print("东瞅瞅，西瞅瞅，瞅出个大活宝...")
            time.sleep(1)
            find_item = treasure.getTreasureBox(self.treasure_box_list)
            if find_item == None:
                print("什么也没有发现")
            else:
                treasure.getPropsToBag(find_item[0],find_item[1])
            return self.showMap(player)
        elif select_id in can_go_list:
            #player.old_place = self
            if block.blockOpenOrNot(player, player.map[select_id][0]):
                player.map[select_id][0].showMap(player)
            else:
                print("当前区域未开放！")
                return self.showMap(player)
        else:
            system.showSystem(player, select_id)
        print("指令错误！")
        return self.showMap(player)