from battle import skilllistmap
import random


pet_skill_tree = {
    '001':{
        'init': ['N001'],
        3: 'N015',
        7: 'B019',
        9: 'B015',
        13:['P011','B007'],
        15:'N047',
        19:'B002',
        21:'N019',
        25:'N018',
        27:'N042',
        31:'B020',
        33:'B021',
        37:'B022',
    },
    '002':{
        'init': ['N001','N015','B019'],
        3: 'N015',
        7: 'B019',
        9: 'B015',
        13:['P011','B007'],
        15:'N047',
        20:'B002',
        23:'N019',
        28:'N018',
        31:'N042',
        36:'B020',
        39:'B021',
        44:'B014',
    },
    '003': {
        'init': ['N001', 'N015', 'B019','B011','B015'],
        'evolve': ['B011'],
        3: 'N015',
        7: 'B019',
        9: 'B015',
        13: ['P011', 'B007'],
        15: 'N047',
        20: 'B002',
        23: 'N019',
        28: 'N018',
        31: 'N042',
        39: 'B020',
        45: 'B021',
        50: 'B012',
        53: 'B014',
    },
    '004':{
        'init': ['N002','N015'],
        7: 'A001',
        10:'N026',
        16:'G004',
        19:'N045',
        25:'A002',
        28:'A003',
        34:'N046',
        37:'A005',
        43:'A004',
        46:'A006',
    },
    '005': {
        'init': ['N002', 'N015','A001'],
        7: 'A001',
        10: 'N026',
        17: 'G004',
        21: 'N045',
        28: 'A002',
        32: 'A003',
        39: 'N046',
        43: 'A005',
        50: 'A004',
        54: 'A006',
    },
    '006': {
        'init': ['N002', 'N015', 'A001','F002','A007','A008','G005','Q004','F003'],
        'evolve': ['F002'],
        7: 'A001',
        10: 'N026',
        17: 'G004',
        21: 'N045',
        28: 'A002',
        32: 'A003',
        41: 'N046',
        47: 'A005',
        56: 'A004',
        62: 'A006',
        71: 'A008',
        77: 'A007',
    },
    '007': {
        'init': ['N001'],
        4: 'N027',
        7: 'D007',
        10:'D012',
        13:'D002',
        16:'T003',
        19:'N032',
        22:'N048',
        25:'D004',
        28:'D013',
        31:'N049',
        34:'X006',
        37:'D014',
        40:'D003',
    },
    '008': {
        'init': ['N001','N027','D007'],
        4: 'N027',
        7: 'D007',
        10: 'D012',
        13: 'D002',
        17: 'T003',
        21: 'N032',
        25: 'N048',
        29: 'D004',
        33: 'D013',
        37: 'N049',
        41: 'X006',
        45: 'D014',
        49: 'D003',
    },
    '009': {
        'init': ['N001','N027','D007','D012','X005'],
        4: 'N027',
        7: 'D007',
        10: 'D012',
        13: 'D002',
        17: 'T003',
        21: 'N032',
        25: 'N048',
        29: 'D004',
        33: 'D013',
        40: 'N049',
        47: 'X006',
        54: 'D014',
        60: 'D003',
    },
    '010':{
        'init': ['N001','C002'],
        9: 'C005',
    },
    '011':{
        'init': ['N031'],
        'evolve': ['N031'],
    },
    '012':{
        'init': ['F001','S008'],
        'evolve': ['F001'],
        11:'S008',
        13:['P011','B001','B007'],
        17:'S009',
        19:'C006',
        23:'N003',
        25:'N051',
        29:'N014',
        31:'C007',
        37:'N052',
        41:'F007',
        43:'F003',
        47:'C008',
    },
    '013':{
        'init':['C002','P004']
    },
    '014':{
        'init': ['N031'],
        'evolve': ['N031'],
    },
    '015':{
        'init': ['C009','N016'],
        'evolve': ['C009'],
        11:'N016',
        14:'N054',
        17:'T005',
        20:'N017',
        23:'P003',
        26:'T006',
        29:'P013',
        32:'C010',
        35:'P012',
        38:'S002',
        41:'N053',
        44:'C011',
    },
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
    '019':{
        'init': ['N001','N027'],
        4: 'N013',
        7: 'N017',
        10:'T003',
        13:'T005',
        16:'N055',
        19:'T006',
        22:'T004',
        25:'N056',
        28:'N057',
        31:'N042',
        34:'N053',
    },
    '020':{
        'init': ['N058','N013','N017','N001','N027'],
        'evolve':['N045'],
        4: 'N013',
        7: 'N017',
        10:'T003',
        13:'T005',
        16:'N055',
        19:'T006',
        24:'T004',
        29:'N056',
        34:'N057',
        39:'N042',
        44:'N053',
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
    '025':{
        'init': ['H002','N027'],
        5: 'N015',
        7: 'N059',
        10:'N013',
        13:'H005',
        18:'H003',
        21:'N060',
        23:'N061',
        26:'H004',
        29:'H010',
        34:'H006',
        37:'N022',
        42:'H011',
        45:'S002',
        50:'H012',
        53:'S006',
        58:'H013',
    },
    '026':{
        'init': ['H002','N027','H002','H011'],
    },
    '027':{
        'init': ['N002','N044'],
        3: 'E003',
        5: 'P004',
        7: 'R005',
        9: 'N032',
        11:'C012',
        14:'E007',
        17:'N004',
        20:'N062',
        23:'E009',
        26:'N046',
        30:'E010',
        34:'X001',
        38:'N058',
        42:'R010',
        46:'E001',
    },
    '028':{
        'init': ['N002','N044','E003','P004','N063'],
        'evolve': ['N063'],
        3: 'E003',
        5: 'P004',
        7: 'R005',
        9: 'N032',
        11:'C012',
        14:'E007',
        17:'N004',
        20:'N062',
        24:'E009',
        28:'N046',
        33:'E010',
        38:'X001',
        43:'N058',
        48:'R010',
        53:'E001',
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
    '074':{
        'init': ['N001','N044'],
        4: 'E006',
        6: 'R004',
        10:'R005',
        12:'E007',
        16:'R001',
        18:'R006',
        22:'E008',
        24:'N041',
        28:'R009',
        30:'R008',
        34:'E001',
        36:'N043',
        40:'N042',
        42:'R007',
    },
    '075':{
        'init': ['N001','N044','E006','R004'],
        4: 'E006',
        6: 'R004',
        10:'R005',
        12:'E007',
        16:'R001',
        18:'R006',
        22:'E008',
        24:'N041',
        30:'R009',
        34:'R008',
        40:'E001',
        44:'N043',
        50:'N042',
        54:'R007',
    },
    '076':{
        'init': ['N001','N044','E006','R004'],
        4: 'E006',
        6: 'R004',
        10:'C004',
        12:'E007',
        16:'R001',
        18:'R006',
        22:'E008',
        24:'N041',
        30:'R009',
        34:'R008',
        40:'E001',
        44:'N043',
        50:'N042',
        54:'R007',
    },
    '081':{
        'init': ['N003','N001'],
        5: 'H002',
        7: 'H003',
        11:'X002',
        13:'S006',
        17:'N038',
        19:'H004',
        23:'X003',
        25:'X004',
        29:'H005',
        31:'X005',
        35:'N006',
        37:'H006',
        41:'N039',
        43:'H007',
        47:'X001',
        49:'H008',
    },
    '082':{
        'init': ['N003', 'N001','N040','H002','H003','H008','H009'],
        'evolve': ['N040'],
        5: 'H002',
        7: 'H003',
        11: 'X002',
        13: 'S006',
        17: 'N038',
        19: 'H004',
        23: 'X003',
        25: 'X004',
        29: 'H005',
        33: 'X005',
        39: 'N006',
        43: 'H006',
        49: 'N039',
        53: 'H007',
        59: 'X001',
        63: 'H008',
    },
    '088':{
        'init': ['N036','P015'],
        4: 'N031',
        7: 'E005',
        12:'N037',
        15:'P016',
        18:'E002',
        21:'N035',
        26:'T008',
        29:'P017',
        32:'P014',
        37:'N006',
        40:'P010',
        43:'P018',
        46:'P008',
        48:'T009',
    },
    '089':{
        'init': ['N036','P015','P019','N031','E005'],
        'evolve': ['P019'],
        4: 'N031',
        7: 'E005',
        12:'N037',
        15:'P016',
        18:'E002',
        21:'N035',
        26:'T008',
        29:'P017',
        32:'P014',
        37:'N006',
        40:'P010',
        46:'P018',
        52:'P008',
        57:'T009',
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
        36:'S002',
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
        38:'S002',
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
        29:'S002',
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
        29:'S002',
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





