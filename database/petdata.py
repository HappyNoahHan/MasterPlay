from database import datasetting
import random

def get_pet(petNo,table_name):
    sql = "select * from %s where petNo=%d" % (table_name,petNo)
    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql)
    pet_data = cursor.fetchone()
    cursor.close()
    datasetting.close_conn(db_conn)
    return pet_data

def get_url():
    sql = 'select * from skillURL'
    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    datasetting.close_conn(db_conn)

    return datas


def insert_data(data):
    '''
    录入数据
    :return:
    '''
    sql = "insert into petMsg(petNo,name,url) values(%s,%s,%s)"

    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql % tuple((repr(e) for e in data)))
    cursor.close()
    db_conn.commit()
    datasetting.close_conn(db_conn)

def insertDetailData(list):
    '''
    插入源表
    :param list:
    :return:
    '''

    sql="insert into petDetailMessage(" \
        "petNo,name,attr,talent,hid_talent,type," \
        "higth,weigth,hp,attack,defense,sp_attack,sp_defense," \
        "speed,total,restraint_relationship,eggs_group,incubation_steps," \
        "sex_ration,capture_degree,initial_closeness,full_experience_for_max_level,base_point) " \
        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    db_conn= datasetting.get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql % tuple((repr(e) for e in list)))
    cursor.close()
    db_conn.commit()
    datasetting.close_conn(db_conn)

def insert_skill_data(datas):
    sql = 'insert into levelUpLearnSkill('\
            'petNo,learn_condition,skill_name,skill_prop,skill_type,skill_power,skill_hit,pp_value,form)'\
        'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()
    for sub_datas in datas:
        for data in sub_datas:
            insert_data = tuple((repr(e) if e != '--' and e != '-' else 'NULL' for e in data.split('|')))
            cursor.execute(sql % insert_data)

    cursor.close()
    db_conn.commit()
    datasetting.close_conn(db_conn)

def insert_skill_url(datas):
    sql = 'insert into skillURL(type,url) values(%s,%s)'

    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()
    for key,value in datas.items():
        cursor.execute(sql % (repr(key),repr(value)))

    cursor.close()
    db_conn.commit()
    datasetting.close_conn(db_conn)


def insert_all_skill_data(datas):
    '''
    存储所有类型的技能信息
    :param datas:
    :return:
    '''
    sql = 'insert into skillInfo(skill_name,skill_prop,skill_type,skill_power,skill_hit,pp_value,comment,z_skill_power)'\
        'values (%s,%s,%s,%s,%s,%s,%s,%s)'

    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()
    for data in datas:
        ins_data = tuple(repr(e) if e != '--' else 'NULL' for e in data.split('|'))
        try:
            cursor.execute(sql % ins_data)
        except:
            print("数据错误,忽视继续")
            continue

    cursor.close()
    db_conn.commit()
    datasetting.close_conn(db_conn)

def get_learn_skill(pet_no):
    print(pet_no)
    sql = 'select * from levelUpLearnSkill where petNo=%d' % pet_no
    sql += " and learn_condition like 'Lv.%'"
    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()

    cursor.execute(sql)

    skill_msg =cursor.fetchall()
    cursor.close()
    datasetting.close_conn(db_conn)

    return skill_msg

def insert_talent_info(datas):
    sql = 'insert into talentInfo(ch_name,jp_name,eg_name,talent_comment) values(%s,%s,%s,%s)'

    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()

    for data in datas:
        cursor.execute(sql % tuple(repr(e) for e in data))

    cursor.close()
    db_conn.commit()
    datasetting.close_conn(db_conn)

















