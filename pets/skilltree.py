from battle import skilllistmap
import random


pet_skill_tree = {
    '016':{
        'init': ['N001'],
        5:'E003',
        9:'F001',
        13:'N013',
        17:'N014',
        21:'G001',
        25:'F005',
        29:'S002',
        33:'F002',
        37:'F006',
        41:'F007',
        45:'F008',
        49:'F003',
        53:'F009',
    },
    '017':{
        'init': ['N001','E003','F001'],
        5:'E003',
        9:'F001',
        13:'N013',
        17:'N014',
        22:'G001',
        27:'F005',
        32:'S002',
        37:'F002',
        42:'F006',
        47:'F007',
        52:'F008',
        57:'F003',
        62:'F009',
    },
    '018': {
        'init': ['N001', 'E003', 'F001','N013','F009'],
        5: 'E003',
        9: 'F001',
        13: 'N013',
        17: 'N014',
        22: 'G001',
        27: 'F005',
        32: 'S002',
        38: 'F002',
        44: 'F006',
        50: 'F007',
        56: 'F008',
        62: 'F003',
        68: 'F009',
    },
    '021':{
        'init': ['F010','N015'],
        4: 'N008',
        8: 'T005',
        11: 'N016',
        15: 'F011',
        18: 'F008',
        22: 'T006',
        25: 'S002',
        29: 'N017',
        32: 'F006',
        36: 'F012',
    },
    '022':{
        'init': ['F010','N015','F013','E004','N008','T005'],
        4: 'N008',
        8: 'T005',
        11: 'N016',
        15: 'F011',
        18: 'F008',
        23: 'T006',
        27: 'S002',
        32: 'N017',
        36: 'F006',
        41: 'F012',
        45: 'E004',
    },
    '023':{
        'init': ['N007','N008'],
        4: 'P004',
        9: 'T003',
        12: 'N009',
        17: 'N006',
        20: 'P005',
        25: ['N010','N011','N012'],
        28: 'P006',
        33: 'E002',
        36: 'P007',
        38: 'P008',
        41: 'I001',
        44: 'P009',
        49: 'P010',
    },
    '024': {
        'init': ['N007', 'N008','T004','I002','H001','A002','P004','T003'],
        'evolve':['T004'],
        4: 'P004',
        9: 'T003',
        12: 'N009',
        17: 'N006',
        20: 'P005',
        27: ['N010', 'N011', 'N012'],
        32: 'P006',
        39: 'E002',
        44: 'P007',
        48: 'P008',
        51: 'I001',
        56: 'P009',
        63: 'P010',
    },
    '026':{ '2' : 'N001',
            '5' : 'N002',
    },
    '041':{
        'init': ['B006'],
        5: 'N003',
        7: 'Q002',
        11: 'T003',
        13: 'F002',
        17: 'Q001',
        19: 'F004',
        23: 'N004',
        25: 'P002',
        29: 'N005',
        31: 'C003',
        35: 'I001',
        37: 'P003',
        41: 'F003',
    },
    '042':{
        'init':['B006','Q002','T003','N003','N006'],
        'evolve':['T004'],
        5:'N003',
        7: 'Q002',
        11: 'T003',
        13: 'F002',
        17: 'Q001',
        19: 'F004',
        24: 'N004',
        27: 'P002',
        32: 'N005',
        35: 'C003',
        40: 'I001',
        43: 'P003',
        48: 'F003',

    },
    '043':{
        'init':['B006','N018'],
        5:'N019',
        9:'P005',
        13:'P011',
        14:'B001',
        15:'B007',
        19:'B008',
        23:'N020',
        27:'Y001',
        31:'B009',
        35:'P001',
        39:'N021',
        43:'Y002',
        47:'B010',
        51:'B011',
    },
    '044': {
        'init': ['B006', 'N018','N019','P005'],
        5: 'N019',
        9: 'P005',
        13: 'P011',
        14: 'B001',
        15: 'B007',
        19: 'B008',
        24: 'N020',
        29: 'Y001',
        34: 'B009',
        39: 'P001',
        44: 'N021',
        49: 'B012',
        54: 'B010',
        59: 'B011',
    },
    '045': {
        'init': ['B008', 'B013', 'B0001', 'P011'],
        49: 'B012',
        59: 'B011',
        69: 'B014',
    },
    '069': {
        'init': ['B015'],
        7: 'N018',
        11: 'N007',
        13: 'B007',
        15: 'P011',
        17: 'B001',
        23: 'P005',
        27: 'T007',
        29: 'N019',
        35: 'P007',
        39: 'B002',
        41: 'P012',
        47: 'N022',
        50: 'N023',
    },
    '070': {
        'init': ['B015','N018','N007'],
        7: 'N018',
        11: 'N007',
        13: 'B007',
        15: 'P011',
        17: 'B001',
        24: 'P005',
        29: 'T007',
        32: 'N019',
        39: 'P007',
        44: 'B002',
        47: 'P012',
        54: 'N022',
        58: 'N023',
    },
    '071': {
        'init': ['B015', 'B016','B007','N010','N011','N012','B002','N019'],
        'evolve': ['B016'],
        32: 'B017',
        44: 'B018',
    },
    '072': {
        'init': ['P004'],
        4: 'N003',
        7: 'N024',
        10:'P005',
        13:'P013',
        16:'D004',
        19:'N007',
        22:'P006',
        25:'D005',
        28:'S003',
        31:'P012',
        34:'D006',
        37:'N006',
        40:'Q003',
        43:'P014',
        46:'D003',
        49:'N023',
    },
    '073': {
        'init': ['P004','N003','N024','P005','N023','N025'],
        4: 'N003',
        7: 'N024',
        10: 'P005',
        13: 'P013',
        16: 'D004',
        19: 'N007',
        22: 'P006',
        25: 'D005',
        28: 'S003',
        32: 'P012',
        36: 'D006',
        40: 'N006',
        44: 'Q003',
        48: 'P014',
        52: 'D003',
        56: 'N023',
    },
    '116':{
        'init': ['D002'],
        5: 'N026',
        9: 'N008',
        13:'D007',
        17:'G001',
        21:'D005',
        26:'N017',
        31:'D006',
        36:'S001',
        41:'G002',
        46:'G003',
        52:'D003',
    },
    '117':{
        'init': ['D002','N026','N008','D007','D003'],
        5: 'N026',
        9: 'N008',
        13:'D007',
        17:'G001',
        21:'D005',
        26:'N017',
        31:'D006',
        38:'S001',
        45:'G002',
        52:'G003',
        60:'D003',
    },
    '118':{
        'init': ['F010','N027','D008'],
        5: 'N003',
        8: 'N028',
        13:'N029',
        16:'D004',
        21:'D009',
        24:'N016',
        29:'S001',
        32:'D010',
        37:'N030',
        40:'D011',
        45:'C001',
    },
    '119':{
        'init': ['F010','N027','D008','C001','N003','P012'],
        5: 'N003',
        8: 'N028',
        13:'N029',
        16:'D004',
        21:'D009',
        24:'N016',
        29:'S001',
        32:'D010',
        40:'N030',
        46:'D011',
        54:'C001',
    },
    '120':{
        'init': ['N001','N031'],
        4: 'D007',
        7: 'N032',
        10:'N033',
        13:'S004',
        16:'N004',
        18:'D005',
        22:'N034',
        24:'X001',
        28:'D006',
        31:'N035',
        35:'N025',
        37:'R003',
        40:'Q001',
        42:'S005',
        46:'S006',
        49:'S007',
        53:'D003',
    },
    '121':{
        'init': ['D003','D007','N032','N033','N004'],
        40:'Q001',
    },

}


def getInitSkillList(pet_no):
    '''
    野生精灵初始技能~
    :param pet_no:
    :return:
    '''
    skill_init_list = pet_skill_tree[pet_no]['init'].copy()

    if skill_init_list.__len__() >= 4:
        skill_init_list = random.sample(skill_init_list,4)

    skill_list = {}

    for key in skill_init_list:
        for x in ['1','2','3','4']:
            if x not in skill_list:
                skill_list[x] = skilllistmap.skill_dict[key]()
                break

    return skill_list





