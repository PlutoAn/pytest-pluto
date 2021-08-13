# -*- coding:utf-8 -*-
# @Time : 2021/7/9 14:02
# @Author: Pluto
# @File : removedir.py
import os

report_path = os.getcwd()
print(report_path)
if os.path.exists(os.path.join(report_path, 'report')):
    resultpath = os.path.join(report_path, 'report')
    for i in os.listdir(resultpath):
        os.remove(os.path.join(resultpath, i))
    os.removedirs(resultpath)
# os.system('pytest test_allure.py --alluredir=allure-results')
# os.system('allure generate allure-results -o allure-report -c')
# os.system('allure open allure-report')
