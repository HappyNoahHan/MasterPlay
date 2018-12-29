from place import  placebase,treasure

class Shop(placebase.Place):
    def __init__(self,name='',sell_list={}):
        super().__init__(name=name)
        self.sell_list = sell_list
        self.name = name


    def showMap(self,player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        print('1:    shopping')
        #print("其他:      退出")
        select_id = input(">")
        if select_id == '1':
            self.buy(player)
            return self.showMap(player)
        elif select_id == 'back':
            player.map_run_list.pop(-1)
            return player.map_run_list[-1].showMap(player)

    def buy(self,player):
        for key,item in self.sell_list.items():
            print(key,":",item[0],'价格:',item[1])
        print("选择你需要购买的道具!")
        select_id = input(">")
        if select_id in self.sell_list:
            print("你要买的数量:")
            number = input(">")
            if isDigt(number):
                price = int(number) * self.sell_list[select_id][1]
                if price > player.money:
                    print("你没有足够的金钱！购买失败")
                    return False
                else:
                    player.money -= price
                    treasure.getPropsToBag(self.sell_list[select_id][0],self.sell_list[select_id][2],number=int(number))
                    print("购买成功！")
                    return True
            else:
                print("数量错误,购买失败！")
                return False
        else:
            print("指令错误！请重新选择！")
            return self.buy(player)






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


shop_list_for_green_town={
    '1': ('精灵球',100,'petball'),
}