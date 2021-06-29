# -*- coding:utf-8 -*-
# @Time : 2021/6/29 10:00
# @Author: Pluto
# @File : insertdb.py.py
import pymysql
from faker import Factory, Faker
import hashlib
import uuid
import random

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
faker1 = Faker("zh_CN")
fakerE = Faker()
fakerJ = Faker("ja_JP")
db = pymysql.connect(host='10.5.9.239',
                     port=3306,
                     user='root',
                     password='root',
                     db='test',
                     charset='utf8')
# 创建游标对象cursor
cursor = db.cursor()
# 查询数据库版本
cursor.execute("select version()")
data = cursor.fetchone()
print(" Database Version: %s" % data)
# 删除数据
sql = "delete from t_user where id>=0"
cursor.execute(sql)
db.commit()
# 查看删除后的结果
sql = "select * from t_user"
cursor.execute(sql)
data = cursor.fetchall()
print("删除后t_user表:{}".format(data))
# 插入数据
start_num = int(input("输入开始插入数量:"))
end_num = int(input("输入结束数量:"))
sql = """INSERT IGNORE INTO t_user (id, username,nick_name,password,email,phone) values (%s, %s,%s,%s,%s,%s)"""
for i in range(start_num, end_num):
    username = "test00" + str(i)
    nick_name = str(fakerJ.name())
    ps = faker1.password()
    md5 = hashlib.md5()
    md5.update(ps.encode('utf-8'))  # 将字符串转换为MD5
    password = md5.hexdigest()
    email = faker1.email()
    phone = faker1.phone_number()
    random_str = random.sample(string, 6)
    uuid_value = uuid.uuid1()
    uuid_str = uuid_value.hex
    id = uuid_str

    try:
        cursor.execute(sql, ( id, username, nick_name, password, email, phone))
        data2 = cursor.fetchall()
        print("------成功插入第{}条数据为{}--------".format(i, (id, username, nick_name, password, email, phone)))
        db.commit()  # 提交修改
    except:
        db.rollback()  # 发生错误回滚
# 查看插入后的结果
sql2 = "select * from t_user"
cursor.execute(sql2)
results = cursor.fetchall()  # 获取所有数据
for row in results:
    print("插入后t_user表：{}".format(row))

# 关闭数据库连接
db.close()
