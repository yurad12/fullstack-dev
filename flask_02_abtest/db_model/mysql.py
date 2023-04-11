import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host = MYSQL_HOST,
    port = 3306,
    user = 'yujeong',
    passwd = 'yujungee',
    db = 'blog_ab',
    charset = 'utf8')

def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True) # 연결 끊기면 재연결
    return MYSQL_CONN