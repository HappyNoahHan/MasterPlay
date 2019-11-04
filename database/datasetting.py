import pymysql
'''
def get_conn():
    db_conn = pymysql.connect(host='10.169.162.96',
                          database='Noah',
                          user='root',
                          password='123',
                          port=3306,
                          charset='utf8')
    return db_conn.cursor()

def close_conn(db_conn):
    db_conn.close()
'''

class DBconn():
    def __init__(self):
        self.db_conn = pymysql.connect(host='10.169.162.96',
                                  database='Noah',
                                  user='root',
                                  password='123',
                                  port=3306,
                                  charset='utf8')
    def get_conn(self):
        return self.db_conn.cursor()

    def commit(self):
        return self.db_conn.commit()

    def close(self):
        self.db_conn.close()
