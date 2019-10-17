import pymysql
def get_conn():
    db_conn = pymysql.connect(host='10.169.162.96',
                          database='Noah',
                          user='root',
                          password='123',
                          port=3306,
                          charset='utf8')
    return db_conn

def close_conn(db_conn):
    db_conn.close()