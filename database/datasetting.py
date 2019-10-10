import pymysql
def get_conn():
    db_conn = pymysql.connect(host='mydocker-3611683.lvs02.dev.ebayc3.com',
                          database='petManage',
                          user='root',
                          password='123456',
                          port=3306,
                          charset='utf8')
    return db_conn

def close_conn(db_conn):
    db_conn.close()


def get_pet(petNo):
    sql = "select * from petList where petNo=%d" % petNo
    db_conn = get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql)
    pet_data = cursor.fetchone()
    close_conn(db_conn)
    return pet_data

def insert_data(data):
    '''
    录入数据
    :return:
    '''
    sql = "insert into petList(petNo,name,url) values(%s,%s,%s)" % (data[0],data[1],data[2])
    db_conn = get_conn()
    cursor = db_conn.cursor()
    cursor.execute(sql)
    cursor.commit()
    cursor.close()
    close_conn(db_conn)