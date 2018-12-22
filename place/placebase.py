class Place(object):
    def __init__(self,name=''):
        self.name = name

    def __str__(self):
        return self.name

    map = {}
    def showMap(self,player):
        for key,value in self.map.items():
            print(key,':',value)

        print("输入指令")

        select_id = input(">")

        self.map[select_id].showMap(player)