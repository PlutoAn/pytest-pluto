# -*- coding:utf-8 -*-
# @Time : 2021/6/8 17:49
# @Author: Pluto
# @File : CaseExcel.py
import faker
import xlrd
import xlwt
from api.user import User

faker1 = faker.Faker()


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.height = height
    style.font = font
    font.colour_index = 4
    return style

def write_execl():
    """
    写测试数据放入的execl
    @return:
    """
    requestsite = ['insert', 'delete', 'update', 'change']
    f = xlwt.Workbook()
    for i in requestsite:
        # 遍历生成多个sheet存储不同接口数据
        sheet1 = f.add_sheet(i, cell_overwrite_ok=True)
        print('生成{}sheet成功'.format(i))
        apipath=User
        print(User)
        row0 = ['期望结果', '期望返回码', '期望返回信息']
        # column0 = ['False', '200', '密码错误！']
        # 写入第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        # for i in range(0, len(column0)):
        #     sheet1.write(i + 1, 0, column0[i], set_style('Times New Roman', 220, True))

    f.save('test.xls')


def read_write_execl(): 
    """
    读取数据execl
    @return:
    """
    global i
    wb = xlrd.open_workbook(filename='test.xls')
    sheet1 = wb.sheet_by_index(0)
    nrows = sheet1.nrows  # 最大行数
    ncols = sheet1.ncols  # 最大列数
    print("打印总行数:{}".format(nrows))
    DataList = []
    for i in range(1, nrows):
        cells=sheet1.row_values()
        DataList.append(sheet1.row_values(i))
        if DataList[0] == 0:
            DataList.append("True")
        print("当前正在执行第{}行执行数据为{}\n".format(i, DataList), end='')
    return DataList
    # rows1_values = sheet1.row_values(0)
    # cols = sheet1.col_values(3)
    # print("获取第一行的数据{}".format(rows1_values))
    # print(cols)


def read_execl():
    RequestList = read_write_execl()
    print(RequestList[0])


if __name__ == '__main__':
    write_execl()
