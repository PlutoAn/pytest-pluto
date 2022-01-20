import pytest
import allure
from testcases.api_test.user import get_all_user_info, get_one_user_info, get_user
from testcases.conftest import api_data
from testcases.scenario_test.operation.logger import logger


@allure.step("步骤1 ==>> 获取某个用户信息")
def step_1(user):
    logger.info("步骤1 ==>> 获取某个用户信息：{}".format(user))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class TestGetUserInfo():
    """获取用户信息模块"""

    @allure.story("用例--获取某个用户信息")
    @allure.description("该用例是针对获取单个用户信息接口的测试")
    @allure.issue("http://10.5.15.151/zentao/bug-browse-3-0-unclosed-0-id_desc.html", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("http://10.5.15.151/zentao/bug-browse-3-0-unclosed-0-id_desc.html", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【{except_result}，{except_code}，{except_msg} 】")
    @pytest.mark.single
    @pytest.mark.parametrize(" except_result, except_code, except_msg",
                             api_data["test_get_get_one_user_info"])
    def test_get_get_one_user_info(self, login_fixture, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        step_1(login_fixture)
        token = login_fixture
        result = get_user(token)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.message
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_get_user_info.py"])
