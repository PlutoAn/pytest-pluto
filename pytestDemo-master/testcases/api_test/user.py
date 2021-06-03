from core.result_base import ResultBase
from api.user import user
from testcases.scenario_test.operation.logger import logger
import json


def get_all_user_info():
    """
    获取全部用户信息
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = user.list_all_users()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    return result


def get_one_user_info(username):
    """
    获取单个用户信息
    :param username:  用户名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = user.list_one_user(username)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "查询用户 ==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("查看单个用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def register_user(username, password, telephone, sex="", address=""):
    """
    注册用户信息
    :param username: 用户名
    :param password: 密码
    :param telephone: 手机号
    :param sex: 性别
    :param address: 联系地址
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "username": username,
        "password": password,
        "sex": sex,
        "telephone": telephone,
        "address": address
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.register(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def check_user(username):
    """
    检查用户登录
    :param username: 用户名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "username": username
    }
    header = {
        "Content-Type": "application/json"

    }
    res = user.check(data=json.dumps(payload), headers=header)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
        result.message = res.json()["message"]
        result.response = res
        logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def login_user(username, password):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "username": username,
        "password": password
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.login(data=json.dumps(payload), headers=header)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
        result.token = res.json()["data"]
        print(result.token)
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def update_user(id, password, confirmPassword, phone, token, email, username,
                nickname, userType, sysRoleld, oneCartoon, departmentId, ipRestrictions, certificateType, expireTime):
    """
    根据用户ID，修改用户信息
    :param id: 用户ID
    :param admin_user: 当前操作的管理员用户
    :param new_password: 新密码
    :param phone: 新手机号
    :param token: 当前管理员用户的token
    :param new_sex: 新性别
    :param new_address: 新联系地址
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    paylod = {

        "id": id,
        "password": password,
        "confirmPassword": confirmPassword,
        "phone": phone,
        "email": email,
        "username": username,
        "nickName": nickname,
        "userType": userType,
        "sysRoleId": sysRoleld,
        "oneCartoon": oneCartoon,
        "departmentId": departmentId,
        "ipRestrictions": ipRestrictions,
        "certificateNum": certificateType,
        "certificateType": certificateType,
        "expireTime": expireTime
    }
    res = user.update(user, json=json.dumps(paylod), headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("修改用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def delete_user(username, admin_user, token):
    """
    根据用户名，删除用户信息
    :param username: 用户名
    :param admin_user: 当前操作的管理员用户
    :param token: 当前管理员用户的token
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "admin_user": admin_user,
        "token": token,
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.delete(username, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("删除用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


if __name__ == '__main__':
    check_user("admin")