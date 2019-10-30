from database import datasetting

def get_pet(petNo,table_name):
    sql = "select * from %s where petNo=%d" % (table_name,petNo)
    db_conn = datasetting.get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql)
    pet_data = cursor.fetchone()
    cursor.close()
    datasetting.close_conn(db_conn)
    return pet_data

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





