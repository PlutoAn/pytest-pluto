import pytest
import allure
from testcases.api_test.user import login_user
from testcases.api_test.user import register_user
from testcases.conftest import api_data
from testcases.scenario_test.operation.logger import logger
from testcases.conftest import login_fixture


@allure.step("步骤1 ==>> 注册用户")
def step_1(username, nickName, departmentId, sysRoleId, oneCartoon, certificateType,
           certificateNum, phone, email, password, confirmPassword, userType):
    logger.info(
        "步骤1 ==>> 注册用户 ==>> {}, {}, {}, {}, {},{},{},{},{},{},{}".format(username, nickName, departmentId, sysRoleId,
                                                                         oneCartoon, certificateType, certificateNum,
                                                                         phone,
                                                                         email, password, confirmPassword, userType))


@allure.step("前置登录步骤 ==>> 管理员登录")
def step_login1(username, token):
    logger.info("前置登录步骤 ==>> 管理员 {} 登录 ==>> 返回的 token 为：{}".format(username, token))


# @  allure.step("前置登录步骤 ==>> 管理员登录")
# def step_login(admin_user, token):
#     logger.info("前置登录步骤 ==>> 管理员 ==>>返回的token为:{}".format(admin_user, token))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户注册模块")
class TestUserRegister():
    """用户注册/添加账号"""

    @allure.story("用例--注册用户信息")
    @allure.description("该用例是针对获取用户注册接口的测试")
    @allure.issue("http://10.5.15.116", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("http://10.5.15.116", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {username}，{nickName}，{departmentId}，{sysRoleId}，{sysRoleId}，{oneCartoon},{certificateType},"
        "{certificateNum},{phone},{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username,nickName,departmentId, sysRoleId, oneCartoon, certificateType, certificateNum, phone,\
                  email, password, confirmPassword, userType,except_result, except_code, except_msg",
                             api_data["test_register_user"])
    @pytest.mark.usefixtures("delete_register_user")
    def test_register_user(self, username, login_fixture, nickName, departmentId, sysRoleId, oneCartoon,
                           certificateType,
                           certificateNum, phone, email, password, confirmPassword, userType,
                           except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        user_info = login_fixture
        token = user_info
        result = register_user(username, token, nickName, departmentId, sysRoleId, oneCartoon, certificateType,
                               certificateNum,
                               phone, email, password, confirmPassword, userType)
        step_1(username, nickName, departmentId, sysRoleId, oneCartoon, certificateType, certificateNum, phone,
               email, password, confirmPassword, userType)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.message
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register.py"])
