# -*- coding:utf-8 -*-
# @Time : 2021/6/7 14:56
# @Author: Pluto
# @File : Archive.py
from core.result_base import ResultBase
from api.user import user
from testcases.scenario_test.operation.logger import logger
from testcases.conftest import login_fixture
import json


def deleteArchive(idList, password, nameList, token):
    """
    删除档案表
    @param idList: id列表
    @param password: 用户密码
    @param nameList: 用户列表
    @param token:
    """
    result = ResultBase()
    payload = {
        "idList": idList,
        "password": password,
        "nameList": nameList
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = user.deleteArchive(data=json.dumps(payload, headers=header))
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
    else:
        result.error = "接口返回码是【{}】,返回信息:{}".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("删除用户 ==>> 返回结果 ==> {}".format(json.loads(json.dumps(res.response.text))))
    return 0


def insertArchiveTable(token, catTemplateId, checkNoRule, classId, code, departmentId, fileTemplateId, name, orderWay,
                       remark):
    """
       添加档案表
       :param catTemplateId: 档案表分组ID
       :param checkNoRule: 
       :param name：档案表名称
       :return: 自定义的关键字返回结果 result
       """
    result = ResultBase()
    payload = {
        "name": name,
        "code": code,
        "remark": remark,
        "classId": classId,
        "orderWay": orderWay,
        "catTemplateId": catTemplateId,
        "fileTemplateId": fileTemplateId,
        "checkNoRule": checkNoRule,
        "userList": [],
        "userRoles": [],
        "departmentId": departmentId
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = user.insertArchiveTable(data=json.dumps(payload), headers=header)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    # print(res.text)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(json.loads(json.dumps(result.response.text))))
    return result
