class Place(object):
    def __init__(self,name=''):
        self.name = name

    def __str__(self):
        return self.name

    maplist = {}
    def showMap(self,player):
        print("=" * 30)
        for key,value in self.maplist.items():
            print(key,':',value)

        print("输入指令")

        select_id = input(">")

        self.maplist[select_id].showMap(player)