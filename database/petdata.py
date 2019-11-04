from database import datasetting
import random

def get_pet(table_name,petNo):
    sql = "select * from %s where petNo=%d" % (table_name,petNo)
    db_conn = datasetting.DBconn()
    cursor = db_conn.get_conn()
    cursor.execute(sql)
    pet_data = cursor.fetchone()
    cursor.close()
    db_conn.close()
    return pet_data


def insert_data(data):

    sql = "insert into petMsg(petNo,name,url) values(%s,%s,%s)"

    db_conn = datasetting.DBconn()
    cursor = db_conn.get_conn()
    cursor.execute(sql % tuple((repr(e) for e in data)))
    cursor.close()
    db_conn.commit()
    db_conn.close()

def insertDetailData(list):


    sql="insert into petDetailMessage(" \
        "petNo,name,attr,talent,hid_talent,type," \
        "higth,weigth,hp,attack,defense,sp_attack,sp_defense," \
        "speed,total,restraint_relationship,eggs_group,incubation_steps," \
        "sex_ration,capture_degree,initial_closeness,full_experience_for_max_level,base_point) " \
        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    db_conn= datasetting.DBconn()
    cursor = db_conn.get_conn()
    cursor.execute(sql % tuple((repr(e) for e in list)))
    cursor.close()
    db_conn.commit()
    db_conn.close()

def insert_skill_data(datas):
    sql = 'insert into levelUpLearnSkill('\
            'petNo,learn_condition,skill_name,skill_prop,skill_type,skill_power,skill_hit,pp_value,form)'\
        'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    db_conn = datasetting.DBconn()
    cursor = db_conn.get_conn()
    for sub_datas in datas:
        for data in sub_datas:
            insert_data = tuple((repr(e) if e != '--' and e != '-' else 'NULL' for e in data.split('|')))
            cursor.execute(sql % insert_data)

    cursor.close()
    db_conn.commit()
    db_conn.close()

def insert_skill_url(datas):
    sql = 'insert into skillURL(type,url) values(%s,%s)'

    db_conn = datasetting.DBconn()
    cursor = db_conn.get_conn()
    for key,value in datas.items():
        cursor.execute(sql % (repr(key),repr(value)))

    cursor.close()
    db_conn.commit()
    db_conn.close()


def insert_all_skill_data(datas):

    sql = 'insert into skillInfo(skill_name,skill_prop,skill_type,skill_power,skill_hit,pp_value,comment,z_skill_power)'\
        'values (%s,%s,%s,%s,%s,%s,%s,%s)'

    db_conn = datasetting.DBconn()
    cursor = db_conn.get_conn()
    for data in datas:
        ins_data = tuple(repr(e) if e != '--' else 'NULL' for e in data.split('|'))
        try:
            cursor.execute(sql % ins_data)
        except:
            print("数据错误,忽视继续")
            continue

    cursor.close()
    db_conn.commit()
    db_conn.close()


def insert_talent_info(datas):
    sql = 'insert into talentInfo(ch_name,jp_name,eg_name,talent_comment) values(%s,%s,%s,%s)'

    db_conn = datasetting.DBconn()
    cursor = db_conn.get_conn()

    for data in datas:
        cursor.execute(sql % tuple(repr(e) for e in data))

    cursor.close()
    db_conn.commit()
    db_conn.close()

def get_data(sql):
    '''
    从数据库读数据
    :param sql:
    :return:
    '''
    db_conn = datasetting.DBconn()
    cursor = db_conn.get_conn()
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    db_conn.close()

    return datas

















