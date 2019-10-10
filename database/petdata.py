from database import datasetting

def get_pet(petNo):
    sql = "select * from petList where petNo=%d" % petNo
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

    db_conn= get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql % tuple((repr(e) for e in list)))
    cursor.close()
    db_conn.commit()
    close_conn(db_conn)

create table petDetailMessage(
 petNo int primary key
 ,name varchar(10) not null unique
 ,attr varchar(10)
 ,talent varchar(10)
 ,hid_talent varchar(10)
 ,type varchar(10)
 ,higth varchar(10)
 ,weigth varchar(10)
 ,hp int not null
 ,attack int not null
 ,defense int not null
 ,sp_attack int not null
 ,sp_defense int not null
 ,speed int not null
 ,total int not null
 ,restraint_relationship varchar(30) not null
 ,eggs_group varchar(10)
 ,incubation_steps varchar(10)
 ,sex_ration varchar(10)
 ,capture_degree int
 ,initial_closeness int
 ,full_experience_for_max_level bigint
 ,base_point varchar(20)
 )ENGINE=MyISAM DEFAULT CHARSET=utf8;
