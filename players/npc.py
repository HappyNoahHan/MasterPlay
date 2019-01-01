class Npc(object):
    def __init__(self,name='',info=None,is_npc = True):
        #is_npc 控制是否是有功能的
        self.is_npc = is_npc
        self.name = name
        self.info = info

    def __str__(self):
        return self.info

class ShopNpc(Npc):
    def __init__(self,name='',info=None,sell_list={},sell_type='',is_npc=False):
        super().__init__(name=name,info=info,is_npc=is_npc)
        self.sell_list = sell_list
        self.sell_type = sell_type

    def showSellList(self):
        print(self.info)
        for key,item in self.sell_list.items():
            print(key,':',item[0],'  $',item[1])

class Hosptial(Npc):
    def __init__(self,name='',info=None,is_npc = False):
        super().__init__(name=name,info=info,is_npc=is_npc)


    def recoverOrNot(self):
        print("是否恢复你的所有精灵？ y/yes  others  no!")
        select_id = input(">")
        if select_id in 'yes' or select_id in 'YES':
            return True
        else:
            return False






