from props import bag

class Place(object):

    def __init__(self,name='',maplist={}):
        self.name = name
        self.maplist = maplist

    def __str__(self):
        return self.name

    def showMap(self,player):
        if player.map_run_list[-1] != self:
            player.map_run_list.append(self)
        print('='*30)
        print('当前地图  %s ' % self.name)
        for key,value in self.maplist.items():
            if value[1] == True:
                print(key,':',value[0])

    def setMapList(self,key,value):
        self.maplist[key][1] = value