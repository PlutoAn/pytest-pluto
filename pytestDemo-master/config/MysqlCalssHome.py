# -*- coding:utf-8 -*-
# @Time : 2021/7/2 11:46
# @Author: Pluto
# @File : MysqlCalssHome.py
import pymysql
import re
class MysqlClass:
    SHOW_SQL = False

    def __init__(self, host, port, user, password, db,
                 charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    # 建立数据库连接
    def opendb(self):
        try:
            DB = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db, port=self.port,
                                 charset=self.charset)
            return DB
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)

    # 查询方法
    def select_all(self, sql):
        try:
            con = self.opendb()
            print(con)
            cur = con.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            fc = cur.fetchall()
            return fc
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            con.close()
        # 带条件查询

    def select_by_where(self, sql, data):
        try:
            con = self.opendb()
            d = (data,)
            cur = con.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql, d)
            fc = cur.fetchall()
            return fc
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    def dml_by_where(self, sql, params):
        try:
            con = self.opendb()
            cur = con.cursor()

            for d in params:
                if self.SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cur.execute(sql, d)
            con.commit()

        except pymysql.Error as e:
            con.rollback()
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 不带参数的更新方法
    def dml_nowhere(self, sql):
        try:
            con = self.opendb()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except pymysql.Error as e:
            con.rollback()
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def delete(self, sql):
        try:
            con = self.opendb()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except pymysql.Error as e:
            con.rollback()
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def insert(self, sql):
        try:
            con = self.opendb()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except pymysql.Error as e:
            con.rollback()
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            con.close()



# 开始测试函数


def select_all():
    sql = "select * from t_user "
    fc = db.select_all(sql)
    for row in fc:
        print("查询所有数据{}".format(row))
        # print(row['id'], row['username'])


def select_by_where():
    sql = "select * from dave where id=%s"
    data = [1]
    fc = db.select_by_where(sql, data)

    for row in fc:
        print(row['id'], row['url'])


def ins_by_param():
    sql = "insert into dave values(%s,%s)"
    data = [(1, 'http://www.cndba.cn'), (2, 'http://www.cndba.cn/dave')]
    db.dml_by_where(sql, data)


def del_by_where():
    sql = "delete from dave where id=%s"
    data = [1, 2]
    db.dml_by_where(sql, data)


def update_by_where():
    sql = "update dave set url=%s where id=%s"
    data = [('http://www.zhixintech.cc', 2)]
    db.dml_by_where(sql, data)


def del_nowhere():
    sql = "delete from dave"
    print(db.dml_nowhere(sql))


if __name__ == "__main__":
    db = MysqlClass('localhost', port=3306, user='root', password='root', db='test',
                    charset='utf8')

    # ins_by_param()
    # del_by_where()
    # update_by_where()
    # del_nowhere()
    select_all()
    # select_by_where()
