import  assist.ppvalue

class Drug(object):
    drug_show_name = '药品'
    info = '药品'

    def __str__(self):
        return self.info


class ppDrug(Drug):
    drug_show_name = 'pp恢复剂'
    info = 'pp值恢复到满'
