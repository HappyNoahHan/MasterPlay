#type  001  解除状态类
from pets import statusmap
from assist import  life,ppvalue
class Berry(object):
    def __init__(self,type=None):
        self.type = type
    show_name = '树果'
    berry_code = 'BY000'

class RemoveTypeBerry(Berry):
    def __init__(self,clean_status=None):
        super().__init__(type='001')
        self.clean_status = clean_status

    def berryEffect(self,obj):
        for status in self.clean_status:
            if status in obj.status:
                obj.removeStatus(status)
                print("%s 食用 %s 解除了 %s ! "% (obj.name,self.show_name,statusmap.status_dict[status].status_show_name))

class RecoverTypeBerry(Berry):
    def __init__(self,recover_item=None): #('HP',10)
        super().__init__(type='002')
        self.recover_item = recover_item

    def berryEffect(self,obj):
        if self.recover_item[0] == 'HP':
            life.healthRecoreByDrug(obj,self.recover_item[1])
        elif self.recover_item[0] == 'PP':
            ppvalue.ppRecover(obj,self.recover_item[1])




class CheriBerry(RemoveTypeBerry):
    def __init__(self):
        super(CheriBerry, self).__init__(clean_status=['ST002'])
    show_name = '樱子果'
    berry_code = 'BY001'

class ChestoBerry(RemoveTypeBerry):
    def __init__(self):
        super(ChestoBerry, self).__init__(clean_status=['ST003'])
    show_name = '零余果'
    berry_code = 'BY002'

class PechaBerry(RemoveTypeBerry):
    def __init__(self):
        super(PechaBerry, self).__init__(clean_status=['ST007'])
    show_name = '桃桃果'
    berry_code = 'BY003'

class RawstBerry(RemoveTypeBerry):
    def __init__(self):
        super(RawstBerry, self).__init__(clean_status=['ST001'])
    show_name = '莓莓果'
    berry_code = 'BY004'

class AspearBerry(RemoveTypeBerry):
    def __init__(self):
        super(AspearBerry, self).__init__(clean_status=['ST008'])
    show_name = '利木果'
    berry_code = 'BY005'

class LeppaBerry(RecoverTypeBerry):
    def __init__(self):
        super(LeppaBerry, self).__init__(recover_item=('PP',10))
    show_name = '苹野果'
    berry_code = 'BY006'

class OranBerry(RecoverTypeBerry):
    def __init__(self):
        super(OranBerry, self).__init__(recover_item=('HP',10))
    show_name = '橙橙果'
    berry_code = 'BY007'


