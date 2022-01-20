# -*- coding:utf-8 -*-
# @Time : 2021/6/29 10:00
# @Author: Pluto
# @File : insertdb.py.py
import pymysql
from faker import Factory, Faker
import hashlib
import uuid
import random
import time
import redis
import re

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
faker1 = Faker("zh_CN")
fakerE = Faker("en_GB")
fakerJ = Faker("ja_JP")


def inserdb():
    db = pymysql.connect(host='10.5.15.254',
                         port=3306,
                         user='videt',
                         password='123456',
                         db='remote_use',
                         charset='utf8')
    # 创建游标对象cursor
    cursor = db.cursor()
    # 查询数据库版本
    cursor.execute("select version()")
    data = cursor.fetchone()
    print(" Database Version: %s" % data)
    # # 删除数据
    # sql = "delete from sys_user where id>=0"
    # cursor.execute(sql)
    # db.commit()
    # # 查看删除后的结果
    # sql = "select * from sys_user"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # print("删除后t_user表:{}".format(data))
    # # 插入数据
    start_num = int(input("输入开始插入数量:"))
    end_num = int(input("输入结束数量:"))
    # INSERT INTO `sys_user` VALUES (1410062870472822785, 1407878182907940865, 1407878182907940865, '2021-06-30 10:29:21', '2021-06-30 10:29:21', '0', NULL, 'testan', 'a0b923820dcc509a', '99', 'huangab ', NULL, NULL, NULL, 1, 2, 1, '管理员', NULL, NULL);

    sql = """INSERT IGNORE INTO sys_user (id, creator, modifier, create_time, update_time, deleted, remark, username, password, one_card_id,
            nickname, email, phone, `type` , status, role_name, gender, id_card)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    for i in range(start_num, end_num):
        username = "student" + str(i)
        nickname = str(faker1.name())
        ps = faker1.password()
        md5 = hashlib.md5()
        md5.update(ps.encode('utf-8'))  # 将字符串转换为MD5
        password = md5.hexdigest()
        email = faker1.email()  # 生成邮箱
        phone = faker1.phone_number()
        random_str = random.sample(string, 6)
        uuid_value = uuid.uuid1()
        uuid_str = uuid_value.hex
        id2 = uuid_str  # 生成uuid
        str1 = ''
        id = str1.join(random.choice('0123456789') for i in range(16))
        creator = str1.join(random.choice('0123456789') for i in range(16))
        modifier = creator
        create_time = time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time()))  # 创建时间
        update_time = create_time  # 更新时间
        deleted = 0
        remark = ''
        one_card_id = str1.join(random.choice('0123456789') for i in range(12))
        type = (random.randint(0, 1))  # 类型
        status = 1
        role = ['管理员用户', '普通用户']
        role_name = role[random.randint(0, 1) % 2]  # 用户角色
        gender = (random.randint(0, 1))  # 性别
        id_card = faker1.ssn()  # 身份证
        # ret = re.match(
        #     r'^\d{6}((19\d{2})|((200\d)|(201[0,8])))((0[13578]((0[1-9])|([1-2]\d)|30|31))|(0[2]((0[1-9])|([1-2]\d)))|(0[2469]((0[1-9])|([1-2]\d)|30))|(11((0[1-9])|([1-2]\d)|30))|(12((0[1-9])|([1-2]\d)|30|31)))\d{3}([0-9]|x)$',
        #     id_card)
        # if ret:
        #     print('姓名:{}该身份证有效:{}'.format(username, ret.group()))
        #
        # else:
        #     print('姓名:{}该身份证无效:{}'.format(username, id_card))
        try:
            cursor.execute(sql, (
                id, creator, modifier, create_time, update_time, deleted, remark, username, password, one_card_id,
                nickname, email, phone, type, status, role_name, gender, id_card))
            data2 = cursor.fetchall()
            print("【---------成功插入第{}条数据为{}--------】".format(i, (id, username, nickname, password, email, phone)))
            db.commit()  # 提交修改
        except:
            print("发生错误数据已回滚！")
            db.rollback()  # 发生错误回滚

    # 查看插入后的结果
    sql2 = "select * from sys_user"
    cursor.execute(sql2)
    results = cursor.fetchall()  # 获取所有数据
    for row in results:
        print("插入后t_user表：{}".format(row))
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    inserdb()
