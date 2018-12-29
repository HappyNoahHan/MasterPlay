from place import placebase,hospital,grassfrom,wildpetlist,treasure,village
from players import trainer
from props import bag
class Town(placebase.Place):
    def showMap(self,player):
        #player.current_place = self
        super().showMap(player)
        print("输入指令")

        select_id = input(">")
        if select_id in self.maplist:
            self.maplist[select_id][0].showMap(player)
        else:
            if select_id == 'bag':
                bag.showBag(player)
                return self.showMap(player)
            elif select_id == 'back':
                player.map_run_list.pop(-1)
                return player.map_run_list[-1].showMap(player)
        print("指令错误！")
        return self.showMap(player)