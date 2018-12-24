from props import bag

class Place(object):
    def __init__(self,name=''):
        self.name = name

    def __str__(self):
        return self.name

    maplist = {}
    def showMap(self,player):
        print('='*30)
        print('当前地图  %s ' % self.name)
        for key,value in self.maplist.items():
            print(key,':',value)

        print("输入指令")

        select_id = input(">")
        if select_id in self.maplist:
            self.maplist[select_id].showMap(player)
        elif select_id == '9' or select_id == 'bag':
            bag.showBag(player)
            return self.showMap(player)
        else:
            print("指令错误！")
            return self.showMap(player)