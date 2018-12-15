from props import drug

drug_dict = {
    '小型回复药剂': drug.HealthRestoreDrug(restore_value=10,drug_show_name='小型回复药剂'),
    '中型回复药剂': drug.HealthRestoreDrug(restore_value=30,drug_show_name='中型回复药剂'),
    '大型回复药剂': drug.HealthRestoreDrug(restore_value=50,drug_show_name='大型回复药剂'),
}

#背包概念 名称 数量
drug_bag_dict={
    1:[drug_dict['小型回复药剂'],1],
    2:[drug_dict['中型回复药剂'],2],
    3:[drug_dict['大型回复药剂'],3],
}
