import MySQLdb
import time
localtime = time.asctime(time.localtime(time.time()))


def connect():
    connect = MySQLdb.connect(host="127.0.0.1", port=3306,
                              db="db1", user="root", password="root", charset='utf8')
    print(localtime, "：数据库连接成功！")
    return connect


def insert(cursor, word, translate):
    cursor.execute("select * from english where word = %s", (word,))
    data = cursor.fetchall()
    if data:
        print(localtime, "：单词已存在！")
    else:
        cursor.execute(
            "insert into english(word, translate) values(%s, %s)", (word, translate))
        print(localtime, "：单词插入成功！")


def isEmpty(cursor):
    cursor.execute("select * from english")
    data = cursor.fetchall()
    if data == ():
        print(localtime, "：数据库为空！")
        createTable(cursor)
        print(localtime, "：id刷新成功！")
    else:
        print(localtime, "：数据库不为空！")


def createTable(cursor):
    # 更新id字段从1开始
    cursor.execute("truncate table english")
