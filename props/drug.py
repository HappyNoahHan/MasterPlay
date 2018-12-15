import  assist.ppvalue
from assist import life
from pets import statusmap
from battle import buff

class Drug(object):
    drug_show_name = '药品'
    info = '药品'

    def __str__(self):
        return self.info

#PP
class ppRestoreMaxDrug(Drug):
    drug_show_name = '完美pp回复剂'
    info = 'pp值恢复到满'

    def useDrug(self,obj):
        return assist.ppvalue.ppRecoverMax(obj)

class PPRestoreDrug(Drug):
    def __init__(self,restore_value = 20,drug_show_name = ''):
        self.store_value = restore_value
        self.drug_info = 'PP恢复药剂'
        self.drug_show_name = drug_show_name

    def useDrug(self,obj):
        return assist.ppvalue.ppRecover(obj,self.store_value)
#health

class HealthMaxRestoreDrug(Drug):
    drug_show_name = '完美生命药剂'
    info = '生命恢复到最大值'

    def useDrug(self,obj):
        return life.healthRecoverMax(obj)

class HealthRestoreDrug(Drug):
    def __init__(self,restore_value = 30,drug_show_name = ''):
        self.store_value = restore_value
        self.drug_info = '生命恢复药剂'
        self.drug_show_name = drug_show_name

    def useDrug(self,obj):
        return life.healthRecoreByDrug(obj,self.store_value)

#解毒

class RemoveStatusDrug(Drug):
    def __init__(self,status_code = 'all',drug_show_name =''):
        self.info = '解除状态药剂'
        self.status_code = status_code
        self.drug_show_name = drug_show_name

    def useDrug(self,obj):
        return statusmap.removeStatus(obj,self.status_code)

class RemoveDebuffDrug(Drug):
    def __init__(self,remove_number = 1,drug_show_name =''):
        self.info = '解除负面效果药剂'
        self.remove_number = remove_number
        self.drug_show_name = drug_show_name

    def useDrug(self,obj):
        return buff.removeOwnDebuff(obj,self.remove_number)








