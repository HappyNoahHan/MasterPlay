from players import trainer
class ShopNpc(object):
    def __init__(self,name='',info=None,sell_list={},sell_type=''):
        self.name = name
        self.info = info
        self.sell_list = sell_list
        self.sell_type = sell_type

    def showSellList(self):
        print(self.info)
        for key,item in self.sell_list.items():
            print(key,':',item[0],'  $',item[1])



shop_list_for_green_town={
    '1': ('精灵球',100),
}

shop_npc_list_for_green_town = {
    '1': ShopNpc(name='精灵球售卖员',info='我有球，你要吗？',sell_list=shop_list_for_green_town,sell_type='petball')
}

