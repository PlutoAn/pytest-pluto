import pytest
import allure
from testcases.api_test.user import login_user, check_user
from testcases.conftest import api_data
from testcases.scenario_test.operation.logger import logger


@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class TestUserLogin():

    @allure.story("用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("http://10.5.15.151/zentao/bug-browse-3-0-unclosed-0-id_desc.html", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("http://10.5.15.151/zentao/bug-browse-3-0-unclosed-0-id_desc.html", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {username}，{password}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             api_data["test_login_user"])
    def test_login_user(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login_user(username, password)
        step_1(username)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        # print(except_code)
        assert result.response.json().get("code") == except_code
        # print(result.response.json()["code"])
        assert except_msg in result.message
        logger.info("***************用例执行结束***************")

    @allure.story("用例--检查登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("http://10.5.15.116/#/home", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("暂无", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {username}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username, except_result, except_code, except_msg",
                             api_data["test_check_user"])
    def test_check_user(self, username, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = check_user(username)
        step_1(username)
        assert result.success == except_result, result.error
        print(result.success)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.message
        logger.info("***************用例执行结束***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_login.py"])
