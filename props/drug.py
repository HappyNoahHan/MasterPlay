import  assist.ppvalue
from assist import life
from pets import statusmap
from battle import buff

class Drug(object):
    drug_show_name = '药品'
    info = '药品'

    def __str__(self):
        return self.info


class ppRestoreMaxDrug(Drug):
    drug_show_name = 'pp大恢复剂'
    info = 'pp值恢复到满'

    def useDrug(self,skill):
        assist.ppvalue.ppRecoverMax(skill)

class ppMiddleRestoreDrug(Drug):
    drug_show_name = 'pp中恢复剂'
    info = 'pp值恢复20'
    restore_number = 20

    def useDrug(self,skill):
        assist.ppvalue.ppRecover(skill,self.restore_number)

class ppSmallRestorDrug(ppMiddleRestoreDrug):
    drug_show_name = 'pp小恢复剂'
    info = 'pp值恢复10'
    restore_number = 10


class PPRestoreDrug(Drug):
    def __init__(self,restore_value = 20):
        self.store_value = restore_value
        self.drug_info = 'PP恢复药剂'

    def useDrug(self,skill):
        assist.ppvalue.ppRecover(skill,self.store_value)


class HealthBigRestoreDrug(Drug):
    drug_show_name = '大生命药剂'
    info = '生命恢复到最大值'

    def useDrug(self,obj):
        life.healthRecoverMax(obj)

class HealthMiddleRestoreDrug(Drug):
    drug_show_name = '中生命药剂'
    info = '生命恢复30'
    restore_value = 30

    def useDrug(self,obj):
        life.healthRecoreByDrug(obj,self.restore_value)

class HealthRestoreDrug(Drug):
    def __init__(self,restore_value = 30,drug_show_name = ''):
        self.store_value = restore_value
        self.drug_info = '生命恢复药剂'
        self.drug_show_name = drug_show_name

    def useDrug(self,obj):
        return life.healthRecoreByDrug(obj,self.store_value)

class RemoveStatusDrug(Drug):
    def __init__(self,status_code = 'ST001'):
        self.info = '解除状态药剂'
        self.status_code = status_code

    def useDrug(self,obj):
        statusmap.removeStatus(obj,self.status_code)

class RemoveDebuffDrug(Drug):
    def __init__(self,remove_number = 1):
        self.info = '解除负面药剂'
        self.remove_number = remove_number

    def useDrug(self,obj):
        buff.removeOwnDebuff(obj,self.remove_number)








