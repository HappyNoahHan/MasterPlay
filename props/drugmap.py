from props import drug

drug_dict = {
    '小型回复药剂': drug.HealthRestoreDrug(restore_value=10,show_name='小型回复药剂'),
    '中型回复药剂': drug.HealthRestoreDrug(restore_value=30,show_name='中型回复药剂'),
    '大型回复药剂': drug.HealthRestoreDrug(restore_value=50,show_name='大型回复药剂'),
    '完美生命药剂': drug.HealthMaxRestoreDrug(),
    '小型PP回复剂': drug.PPRestoreDrug(restore_value=10,show_name='小型PP回复剂'),
    '大型PP回复剂': drug.PPRestoreDrug(restore_value=20,show_name='大型pp回复剂'),
    '完美pp回复剂': drug.ppRestoreMaxDrug(),
    '灼伤解除剂': drug.RemoveStatusDrug(status_code='ST001',show_name='灼伤解除剂'),
    '完美解除剂': drug.RemoveStatusDrug(show_name='完美解除剂'),
    '小型解毒剂': drug.RemoveDebuffDrug(remove_number=1,show_name='小型解毒剂'),
    '完美解毒剂': drug.RemoveDebuffDrug(remove_number=99,show_name='完美解毒剂'),
}

#背包概念 名称 数量
drug_bag_dict={
    #1:[drug_dict['小型回复药剂'],1],
    #2:[drug_dict['中型回复药剂'],2],
    #3:[drug_dict['大型回复药剂'],3],
}


def getDrug(drug_name,number = 1):
    print("获得 %s X %d !" % (drug_name,number))
    for key,value in drug_bag_dict.items():
        if value[0] == drug_dict[drug_name]:
            value[1] += number
            return True

    for key in range(1,101):
        if key not in drug_bag_dict:
            drug_bag_dict[key] = [drug_dict[drug_name],number]
            return True

    return False
