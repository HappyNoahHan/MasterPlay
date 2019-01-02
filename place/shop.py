from place import  placebase,treasure,meetnpc
from assist import system,prize,changepet
import time

class Shop(placebase.Place):

    def showMap(self,player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        for key,item in self.npc_list.items():
            print(key,':',item.name)
        print("请选择售货员")
        select_id = input(">")
        system.showSystem(player, select_id)
        if select_id in self.npc_list:
            if self.npc_list[select_id].is_special == True:
                self.npc_list[select_id].showSellList()
                self.buy(player,self.npc_list[select_id])
                return self.showMap(player)
            else:
                print(self.npc_list[select_id])
                meetnpc.meetNpc(player, self.npc_list[select_id], self)
        else:
            print("指令错误！")
            return self.showMap(player)


    def buy(self,player,shop_npc):
        print("选择你需要购买的道具!")
        select_id = input(">")
        if select_id in shop_npc.sell_list:
            print("你要买的数量:")
            number = input(">")
            if isDigt(number):
                price = int(number) * shop_npc.sell_list[select_id][1]
                if price > player.money:
                    print("你没有足够的金钱！购买失败")
                    return False
                else:
                    player.money -= price
                    treasure.getPropsToBag(shop_npc.sell_list[select_id][0],shop_npc.sell_type,number=int(number))
                    print("购买成功！")
                    return True
            else:
                print("数量错误,购买失败！")
                return False
        elif select_id in 'quit':
            print("退出购买！")
            return self.showMap(player)
        else:
            print("指令错误！请重新选择！")
            return self.buy(player,shop_npc)






def isDigt(x):
    '''
    判断是否是数字
    :param x:
    :return:
    '''
    try:
        x = int(x)
        return isinstance(x,int)
    except:
        return False
