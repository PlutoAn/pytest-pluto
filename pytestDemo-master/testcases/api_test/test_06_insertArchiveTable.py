import pytest
import allure
from testcases.api_test.user import login_user
from testcases.api_test.user import register_user
from testcases.conftest import api_data
from testcases.api_test.Archive import insertArchiveTable
from testcases.scenario_test.operation.logger import logger
from testcases.conftest import login_fixture


@allure.step("步骤1 ==>> 添加档案表")
def step_1(name, code, remark, classId, orderWay, catTemplateId, fileTemplateId, checkNoRule,
           departmentId):
    logger.info(
        "步骤1 ==>> 添加档案表 ==>> {}, {}, {}, {}, {},{},{},{},{}".format(name, code, classId, remark, orderWay,
                                                                    catTemplateId
                                                                    , fileTemplateId, checkNoRule,
                                                                    departmentId))


@allure.step("前置登录步骤 ==>> 管理员登录")
def step_login1(username, token):
    logger.info("前置登录步骤 ==>> 管理员 {} 登录 ==>> 返回的 token 为：{}".format(username, token))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("添加档案表模块")
class TestinsertArchiveTable():
    """添加档案表"""

    @allure.story("用例--添加档案表")
    @allure.description("该用例是针对添加档案表的测试")
    @allure.issue("http://10.5.15.116", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("http://10.5.15.116", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {catTemplateId}，{checkNoRule}，{classId}，{code}，{remark}，{departmentId},{fileTemplateId},"
        "{name},{orderWay},{except_result},{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize(
        "catTemplateId, checkNoRule, classId, code,remark, departmentId, fileTemplateId,name, \
        orderWay,except_result,except_code,except_msg",
        api_data["test_insertArchiveTable"])
    @pytest.mark.usefixtures("delete_register_user")
    def test_insertArchiveTable(self, name, login_fixture, code, remark, classId, orderWay,
                                catTemplateId,
                                fileTemplateId, checkNoRule, departmentId,
                                except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        user_info = login_fixture
        token = user_info
        result = insertArchiveTable(token, catTemplateId, checkNoRule, classId, code, departmentId, fileTemplateId,
                                    name, orderWay,
                                    remark)
        step_1(catTemplateId, checkNoRule, classId, code, remark, departmentId, fileTemplateId, name, orderWay)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.message
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_06_insertArchiveTable.py"])
