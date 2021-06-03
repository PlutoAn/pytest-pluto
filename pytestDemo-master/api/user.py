import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class User(RestClient):
    """
    定义一个接口请求路径的类
    存放接口地址
    """

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def list_all_users(self, **kwargs):
        return self.get("/users", **kwargs)

    def list_one_user(self, username, **kwargs):
        return self.get("/users/{}".format(username), **kwargs)

    def register(self, **kwargs):
        return self.post("/register", **kwargs)

    def login(self, **kwargs):
        return self.post("/user/login", **kwargs)

    def update(self, user_id, **kwargs):
        return self.post("/user/updateUserInfo{}".format(user_id), **kwargs)

    def delete(self, name, **kwargs):
        return self.post("/delete/user/{}".format(name), **kwargs)

    def get(self, url, **kwargs):
        return self.post("/user{}".format(user), **kwargs)

    def check(self,  **kwargs):
        return self.post("/user/checkUsername", **kwargs)


user = User(api_root_url)
