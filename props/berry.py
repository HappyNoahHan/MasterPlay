#type  001  解除状态类
from pets import statusmap
class Berry(object):
    def __init__(self,type=None):
        self.type = type
    show_name = '无名'

class RemoveTypeBerry(Berry):
    def __init__(self,status=None):
        super().__init__(type='001')
        self.status = status

    def berryEffect(self,obj):
        if self.status in obj.status:
            obj.removeStatus(self.status)
            print("%s 食用 %s 解除了 %s ! "% (obj.name,self.show_name,statusmap.status_dict[self.status].status_show_name))

class CheriBerry(RemoveTypeBerry):
    def __init__(self):
        super(CheriBerry, self).__init__(status='ST002')
    show_name = '樱子果'
    berry_code = 'BY001'

class ChestoBerry(RemoveTypeBerry):
    def __init__(self):
        super(ChestoBerry, self).__init__(status='ST003')
    show_name = '零余果'
    berry_code = 'BY002'


